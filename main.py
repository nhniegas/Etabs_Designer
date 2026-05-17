# Standard imports for system operations
import sys
import os
import string

# Import PySide6 for GUI
from PySide6.QtCore import Qt, QTimer, QObject, Signal, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QListWidgetItem,
    QMessageBox,
    QHeaderView,
    QAbstractItemView,
)

# Import modules for custom GUI and ETABS API
from mainwindow_ui import Ui_MainWindow
from modules.etabs_api import ETABSConnector
from typing import Union

# Import for data handlinfg - concrete design and analysis module
import pandas as pd


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ETABSDataModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        # Ensure it's a DataFrame to avoid shape errors
        self._data = data if hasattr(data, "shape") else pd.DataFrame(data)

    # Use Union[QModelIndex, None] to satisfy Pylance's strict check
    def rowCount(self, parent: Union[QModelIndex, None] = QModelIndex()):
        return self._data.shape[0]

    def columnCount(self, parent: Union[QModelIndex, None] = QModelIndex()):
        return self._data.shape[1]

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if not index.isValid() or role != Qt.DisplayRole:
            return None
        # Fast iloc access for your Story/Label/UniqueName columns
        return str(self._data.iloc[index.row(), index.column()])

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return str(self._data.columns[section])
        return None


class DESIGNER_APP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.etabs = ETABSConnector()
        self.setWindowIcon(QIcon(resource_path("Etabs_Logo.ico")))

        self.AutoTaggerController = None
        self.BeamDesignController = None

        # REDIRECT STDOUT TO THE CONSOLE LOG IN THE UI
        self.sys_stdout = EmittingStream()
        self.sys_stdout.textWritten.connect(self.append_log)
        sys.stdout = self.sys_stdout

        # NAVIGATE TO AUTO-TAGGER WIDGET
        self.ui.btn_auto_tagger.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_auto_tagger)
        )
        self.ui.btn_auto_tagger.clicked.connect(
            lambda: self.animate_click(self.ui.btn_auto_tagger)
        )

        # NAVIGATE TO BEAM DESIGN WIDGET
        self.ui.beam_design.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_beam_design)
        )
        self.ui.beam_design.clicked.connect(
            lambda: self.animate_click(self.ui.beam_design)
        )

        # OPEN ETABS MODEL COMMAND
        self.ui.menu_Open.triggered.connect(lambda: self.open_model())

    def set_effective_design_forces(self):
        try:
            df = self.etabs.get_data("Design Forces - Beams")

        except Exception as e:
            print(f"Error setting effective design forces: {e}")

    def open_model(self):
        from PySide6.QtWidgets import QFileDialog, QProgressDialog, QApplication
        from PySide6.QtCore import Qt

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open ETABS Model",
            "",
            "ETABS Models (*.edb *.edb3)   ",
        )

        if not file_path:
            return

        loading = QProgressDialog("Opening Model...", "", 0, 0, self)
        loading.setWindowTitle("Please Wait")
        loading.setWindowModality(Qt.WindowModality.WindowModal)
        loading.setMinimumDuration(0)
        loading.setCancelButton(None)
        loading.show()
        QApplication.processEvents()

        try:
            print(f"Opening file: {file_path}")
            self.etabs.connect()
            self.etabs.open_model(file_path)
            self.etabs.run_analysis()

        except Exception as e:
            print(f"Error opening model: {e}")
        finally:
            self.auto_tagger = AutoTaggerController(self.ui, self.etabs)
            self.BeamDesignController = BeamDesignController(self.ui, self.etabs)
            loading.close()

    def closeEvent(self, event):
        try:
            self.etabs.close_model()
            sys.stdout = sys.__stdout__
            super().closeEvent(event)
        except Exception as e:
            print(f"Error closing ETABS model: {e}")

    def animate_click(self, button):
        from PySide6.QtCore import QPropertyAnimation, QSize, QEasingCurve

        # Don't ask the button for its size. TELL IT the size.
        # Change (64, 64) to whatever size your icons are in Qt Designer.
        target_width = 100
        target_height = 100

        normal_size = QSize(target_width, target_height)
        small_size = QSize(int(target_width * 0.8), int(target_height * 0.8))
        # -----------------------

        # 1. STOP any running animation to prevent conflicts
        if (
            hasattr(self, "anim")
            and self.anim.state() == QPropertyAnimation.State.Running
        ):
            self.anim.stop()

        self.anim = QPropertyAnimation(button, b"iconSize")
        self.anim.setDuration(100)

        # Always force the start value to be the correct normal size
        self.anim.setStartValue(normal_size)
        self.anim.setEndValue(small_size)

        self.anim.setEasingCurve(QEasingCurve.Loc.OutQuad)

        # Reset to PERFECT normal size when done
        self.anim.finished.connect(lambda: button.setIconSize(normal_size))

        self.anim.start()

    def append_log(self, text):
        # 1. AUTO SCROLL
        cursor = self.ui.console_log.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)

        # 2. REDUCE TEXT SIZE
        font_format = cursor.charFormat()
        font_format.setFontPointSize(8)
        cursor.setCharFormat(font_format)

        # 3. ADD SPACE BEFORE NEW STATEMENTS
        if self.ui.console_log.toPlainText().strip():
            text = f"\n{text}"

        # 4. INSERT THE NEW TEXT
        cursor.insertText(text)
        self.ui.console_log.setTextCursor(cursor)

        # 5. ENSURE SCROLL BAR FOLLOWS TEXT
        self.ui.console_log.verticalScrollBar().setValue(
            self.ui.console_log.verticalScrollBar().maximum()
        )


class BeamDesignController:
    def __init__(self, ui_instance, etabs_instance):
        self.ui = ui_instance
        self.etabs = etabs_instance

        self.property_data = self.PropertyDataController(self)
        self.overwrites = self.OverwritesController(self)
        self.design = self.DesignController(self)
        self.deflection_check = self.DeflectionController(self)
        self.export = self.ExportController(self)

    def display_table_data(self, dataframe, table_widget):
        try:
            # Create the model ONLY ONCE here
            self.force_model = ETABSDataModel(dataframe)
            table_widget.setModel(self.force_model)

            # 2. OPTIMIZATION: Avoid 'ResizeToContents' for large data
            header = table_widget.horizontalHeader()

            # Use Interactive so the user can drag, but the UI doesn't lag on load
            header.setSectionResizeMode(QHeaderView.Interactive)

        except Exception as e:
            print(f"Error displaying table data: {e}")

    class PropertyDataController:
        def __init__(self, parent):
            self.parent = parent

            # Connect buttons to functions
            self.parent.ui.btn_section_data.clicked.connect(
                lambda: self.parent.display_table_data(
                    self.parent.etabs.get_data(
                        "Frame Section Property Definitions - Concrete Rectangular"
                    ),
                    self.parent.ui.raw_data,
                )
            )
            self.parent.ui.btn_concrete_material.clicked.connect(
                lambda: self.parent.display_table_data(
                    self.parent.etabs.get_data("Material Properties - Concrete Data"),
                    self.parent.ui.raw_data,
                )
            )
            self.parent.ui.btn_rebar_material.clicked.connect(
                lambda: self.parent.display_table_data(
                    self.parent.etabs.get_data(
                        "Frame Section Property Definitions - Concrete Beam Reinforcing"
                    ),
                    self.parent.ui.raw_data,
                )
            )
            self.parent.ui.btn_frame_assignment.clicked.connect(
                lambda: self.parent.display_table_data(
                    self.parent.etabs.get_data(
                        "Frame Assignments - Section Properties"
                    ),
                    self.parent.ui.raw_data,
                )
            )

    class OverwritesController:
        def __init__(self, parent):
            self.parent = parent

            list = self.parent.etabs.get_data("Load Combination Definitions")[
                "Name"
            ].tolist()

            load_combos = []
            for i in range(len(list)):
                if list[i] not in load_combos:
                    load_combos.append(list[i])

            self.setup_list_with_header(
                self.parent.ui.combo_list,
                "Etabs Load Combinations",
                load_combos,
            )

            self.setup_list_with_header(
                self.parent.ui.beam_list,
                "Beam List",
                self.parent.etabs.get_data("Frame Assignments - Section Properties")[
                    "UniqueName"
                ].tolist(),
            )

            self.parent.ui.max_rho.stateChanged.connect(
                lambda state: self.parent.ui.max_rho.setText("✔" if state == 2 else "")
            )
            self.parent.ui.half_moment.stateChanged.connect(
                lambda state: self.parent.ui.half_moment.setText(
                    "✔" if state == 2 else ""
                )
            )
            self.parent.ui.fourth_moment.stateChanged.connect(
                lambda state: self.parent.ui.fourth_moment.setText(
                    "✔" if state == 2 else ""
                )
            )

            self.parent.ui.prob_shear.stateChanged.connect(
                lambda state: self.parent.ui.prob_shear.setText(
                    "✔" if state == 2 else ""
                )
            )

            self.setup_list_with_header(
                self.parent.ui.uls_combo_list, "ULS Load Combinations"
            )
            self.setup_list_with_header(
                self.parent.ui.sls_combo_list, "SLS Load Combinations"
            )
            self.setup_list_with_header(
                self.parent.ui.selected_beam_list, "Beams Selected for Design"
            )

            # Connect the ULS Add/Remove buttons
            self.parent.ui.add_uls.clicked.connect(
                lambda: (
                    self.move_data(
                        self.parent.ui.combo_list, self.parent.ui.uls_combo_list
                    ),
                    self.parent.ui.cmb_gravity_load_combo.addItems(
                        [
                            self.parent.ui.uls_combo_list.item(i).text()
                            for i in range(1, self.parent.ui.uls_combo_list.count())
                        ]
                    ),
                ),
            )

            self.parent.ui.remove_uls.clicked.connect(
                lambda: (
                    self.move_data(
                        self.parent.ui.uls_combo_list, self.parent.ui.combo_list
                    ),
                    self.parent.parent.ui.cmb_gravity_load_combo.clear(),
                    self.parent.ui.cmb_gravity_load_combo.addItems(
                        [
                            self.parent.ui.uls_combo_list.item(i).text()
                            for i in range(1, self.parent.ui.uls_combo_list.count())
                        ]
                    ),
                )
            )

            # Connect the Add/Remove Beams Button
            self.parent.ui.add_beams.clicked.connect(
                lambda: self.move_data(
                    self.parent.ui.beam_list, self.parent.ui.selected_beam_list
                )
            )

            self.parent.ui.remove_beams.clicked.connect(
                lambda: self.move_data(
                    self.parent.ui.selected_beam_list, self.parent.ui.beam_list
                )
            )

            # Connect the SLS Add/Remove buttons
            self.parent.ui.add_sls.clicked.connect(
                lambda: self.move_data(
                    self.parent.ui.combo_list, self.parent.ui.sls_combo_list
                )
            )
            self.parent.ui.remove_sls.clicked.connect(
                lambda: self.move_data(
                    self.parent.ui.sls_combo_list, self.parent.ui.combo_list
                )
            )

        def setup_list_with_header(self, list_widget, header_text, data_list=None):
            # 1. Clear existing items
            list_widget.clear()

            # 2. Create the Header Item
            header_item = QListWidgetItem(header_text)

            # 4. Make the Header Non-Selectable and Non-Editable
            # This prevents the header from being "moved" by your ADD buttons
            header_item.setFlags(Qt.NoItemFlags)
            header_item.setBackground(QColor(230, 230, 230))
            list_widget.addItem(header_item)

            # Only add data if it's provided (not at startup)
            if data_list:
                for item in data_list:
                    list_widget.addItem(item)

        def move_data(self, source, target):
            # 1. Get a list of all selected item objects
            selected_items = source.selectedItems()

            # 2. Loop through each selected item
            for item in selected_items:
                # Get the row index of the current item
                row = source.row(item)

                # 3. Safety Check: Index 0 is the Header
                # We skip the header so it remains in the source list
                if row > 0:
                    # Take the item out of the source
                    taken_item = source.takeItem(row)
                    # Add the text to the target list
                    target.addItem(taken_item.text())

    class DesignController:
        def __init__(self, parent):
            self.parent = parent

            self.parent.ui.extract_etabs_forces.clicked.connect(
                self.extract_design_forces
            )

        def extract_design_forces(self):
            uls_count = self.parent.ui.uls_combo_list.count() - 1
            sls_count = self.parent.ui.sls_combo_list.count() - 1

            # CHECK IF COMBO BOXES ARE EMPTY (ONLY HEADER)
            if uls_count <= 0 or sls_count <= 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Missing Load Combinations")
                msg.setInformativeText(
                    "Please add at least one ULS and one SLS load combination before proceeding."
                )
                msg.setWindowTitle("Input Required")
                msg.exec()
                return  # STOP EXECUTION IF COMBO BOXES ARE EMPTYU\

            from PySide6.QtWidgets import QProgressDialog, QApplication

            # POPS THE LOADING BOXES IF ALL COMBO BOXES HAVE AT LEAST 1 ITEM (EXCLUDING HEADER)
            loading = QProgressDialog(
                "Performing Concrete Design in ETABS...", "", 0, 0
            )
            loading.setWindowTitle("Please Wait")
            loading.setWindowModality(Qt.WindowModality.WindowModal)
            loading.setMinimumDuration(0)
            loading.setCancelButton(None)
            loading.show()
            QApplication.processEvents()

            try:
                self.parent.etabs.clear_load_combinations(
                    self.parent.etabs.get_data("Load Combination Definitions")[
                        "Name"
                    ].tolist()
                )

                # RETRIEVE ALL THE SELECTED LOAD COMBOS FOR DESIGN
                load_combos = []
                for i in range(1, self.parent.ui.uls_combo_list.count()):
                    combo_name = self.parent.ui.uls_combo_list.item(i).text()
                    load_combos.append(combo_name)

                for i in range(1, self.parent.ui.sls_combo_list.count()):
                    combo_name = self.parent.ui.sls_combo_list.item(i).text()
                    load_combos.append(combo_name)

                # RUN CONCRETE DESIGN
                self.parent.etabs.set_load_combinations(load_combos)
                ret = self.parent.etabs.run_concrete_design()

                # CHHECK IF CONCRETE DESIGN IS SUCCESSFUL
                if ret == True:
                    print(
                        "Concrete design completed successfully with selected combos."
                    )

                    # GETS THE DESIGN FORCES OF BEAMS
                    df = self.parent.etabs.get_data("Design Forces - Beams")

                    # ELIMINATE THE LAST TWO CHARACTERS OF COMBO NAME (I.E. "LC1-1" BECOMES "LC1")
                    df["Combo"] = df["Combo"].str[:-2]

                    print(df["Combo"])

                    # GETS THE DATA FOR STATION POINTS AND CORRESPONDING MOMENT
                    df["Station"] = pd.to_numeric(df["Station"], errors="coerce")
                    df["M3"] = pd.to_numeric(df["M3"], errors="coerce")

                    # SORT THE DATAFRAME BY STORY, BEAM, COMBO, AND STATION (FROM LEFT TO RIGHT) AND GETS THE BEAM LENGTH
                    df["BeamLength"] = df.groupby(["Story", "UniqueName", "Combo"])[
                        "Station"
                    ].transform("max")

                    # CLASSIFY THE RELATIVE POSITION OF STATION POINTS
                    df["RelStation"] = df["Station"] / df["BeamLength"]

                    # SET THE CATEGORY FOR LEFT, MIDDLE, AND, RIGHT ZONES
                    bins = [0, 0.25, 0.75, 1.0]
                    labels = ["Left", "Middle", "Right"]

                    # CLASSIFY STATION AS LEFT, MIDDLE, OR RIGHT ZONES
                    df["Zone"] = pd.cut(
                        df["RelStation"], bins=bins, labels=labels, include_lowest=True
                    )

                    # SORT THE DATA BASED BY SETTING THE LEFT, MIDDLE, AND RIGHT ZONES TO COLUMNS
                    # GETS THE MIN AND MAX MOMENT FOR EACH ZONES
                    df_grouped = (
                        df.groupby(
                            ["Story", "UniqueName", "Combo", "Zone"], observed=False
                        )["M3"]
                        .agg(
                            ["min", "max"]
                        )  # min = Top Steel tension, max = Bot Steel tension
                        .unstack()  # Moves Zone (Left/Middle/Right) to columns
                    )

                    # REAARRANGE THE DATAFRAME TO GET THE MAX MOMENT CRITICAL TOP AND BOTTOM OF CONCRETE BEAM
                    df_nested = df_grouped.stack(level=0)
                    df_nested.index.set_names("Loc", level=-1, inplace=True)
                    df_final = df_nested.reset_index()
                    df_final["Loc"] = df_final["Loc"].replace(
                        {"min": "Top", "max": "Bot"}
                    )
                    df_final["Loc"] = pd.Categorical(
                        df_final["Loc"], categories=["Top", "Bot"], ordered=True
                    )

                    # GET THE FINAL FORMAT OF THE DATAFFRAME WITH MOMENTS, BEAM LENGTH, AND ZONE CLASSIFICATION
                    df_final = df_final.sort_values(
                        by=["Story", "UniqueName", "Combo", "Loc"]
                    )

                    # APPEND THE LENGTH OF THE BEAM TO THE DATAFRAME
                    df_lengths = df[
                        ["Story", "UniqueName", "BeamLength"]
                    ].drop_duplicates()
                    df_final = df_final.merge(
                        df_lengths, on=["Story", "UniqueName"], how="left"
                    )
                    cols = list(df_final.columns)

                    # RELOCATE THE POSITION OF BEAM LENGTH COLUMN
                    cols.insert(3, cols.pop(cols.index("BeamLength")))
                    df_final = df_final[cols]
                    df_final = df_final.reset_index(drop=True)

                    # GETS THE DEPTH AND WIDTH FOR EACH BEAM
                    df_assign_lookup = self.parent.etabs.get_data(
                        "Frame Assignments - Section Properties"
                    )[["Story", "UniqueName", "SectProp"]].drop_duplicates()

                    df_prop_lookup = self.parent.etabs.get_data(
                        "Frame Section Property Definitions - Concrete Rectangular"
                    )[["Name", "t3", "t2"]].rename(columns={"Name": "SectProp"})

                    # APPEND THE DIMENSIONS OF THE BEAM TO THE DATAFRAME
                    df_final = df_final.merge(
                        df_assign_lookup, on=["Story", "UniqueName"], how="left"
                    )
                    df_final = df_final.merge(df_prop_lookup, on="SectProp", how="left")

                    cols = list(df_final.columns)

                    # RELOCATE THE POSITION OF DEPTH (t3) AND WIDTH (t2) COLUMNS
                    cols.insert(4, cols.pop(cols.index("t3")))
                    cols.insert(5, cols.pop(cols.index("t2")))

                    df = df.merge(
                        df_assign_lookup, on=["Story", "UniqueName"], how="left"
                    )
                    df = df.merge(df_prop_lookup, on="SectProp", how="left")

                    # CONVERT THE DIMENSIONS, BEAM LENGTH, STATION, AND SHEAR TO NUMERIC VALUES FOR CALCULATION
                    df["t3"] = pd.to_numeric(df["t3"], errors="coerce")
                    df["t2"] = pd.to_numeric(df["t2"], errors="coerce")
                    df["BeamLength"] = pd.to_numeric(df["BeamLength"], errors="coerce")
                    df["Station"] = pd.to_numeric(df["Station"], errors="coerce")
                    df["V2"] = pd.to_numeric(df["V2"], errors="coerce")
                    df["T"] = pd.to_numeric(df["T"], errors="coerce").abs()

                    # GETS THE MAX TORSION FOR EACH LOAD COMBO
                    df["MaxTorsion"] = df.groupby(["Story", "UniqueName", "Combo"])[
                        "T"
                    ].transform("max")

                    df_torsion_lookup = df[
                        ["Story", "UniqueName", "Combo", "MaxTorsion"]
                    ].drop_duplicates()

                    df_final = df_final.merge(
                        df_torsion_lookup,
                        on=["Story", "UniqueName", "Combo"],
                        how="left",
                    )

                    # GET MAX SHEAR VALUES AT CRITICAL ZONES
                    df["d_off"] = df["t3"] - 0.06
                    df["two_t3"] = df["t3"] * 2

                    # L_zero = 0
                    # L_d = df["d_off"]
                    # L_2t3 = df["two_t3"]

                    # R_zero = df["BeamLength"]
                    # R_d = df["BeamLength"] - df["d_off"]
                    # R_2t3 = df["BeamLength"] - df["two_t3"]

                    def get_max_v2(df_sub, start, end):
                        mask = (df_sub["Station"] >= start) & (df_sub["Station"] <= end)
                        return df_sub.loc[mask, "V2"].abs().max()

                    grouped = df.groupby(
                        ["Story", "UniqueName", "Combo"], observed=False
                    )

                    shear_zones = grouped.apply(
                        lambda x: pd.Series(
                            {
                                "Vdl": get_max_v2(x, 0, x["d_off"].iloc[0]),
                                "V2hl": get_max_v2(
                                    x, x["d_off"].iloc[0], x["two_t3"].iloc[0]
                                ),
                                "Vm": get_max_v2(
                                    x,
                                    x["two_t3"].iloc[0],
                                    x["BeamLength"].iloc[0] - x["two_t3"].iloc[0],
                                ),
                                "V2hr": get_max_v2(
                                    x,
                                    x["BeamLength"].iloc[0] - x["two_t3"].iloc[0],
                                    x["BeamLength"].iloc[0] - x["d_off"].iloc[0],
                                ),
                                "Vdr": get_max_v2(
                                    x,
                                    x["BeamLength"].iloc[0] - x["d_off"].iloc[0],
                                    x["BeamLength"].iloc[0],
                                ),
                            }
                        ),  # Closes pd.Series
                        include_groups=False,  # Required for newer Pandas versions
                    ).reset_index()

                    df_final = df_final.merge(
                        shear_zones, on=["Story", "UniqueName", "Combo"], how="left"
                    )

                    # GET THE FINAL FORMAT OF DATAFRAME CONTAINING CRITICAL VALUES FOR MOMENT, SHEAR, AND TORSION
                    desired_cols = [
                        "Story",
                        "UniqueName",
                        "BeamLength",
                        "t3",
                        "t2",
                        "Combo",
                        "Loc",  # Identifiers & Geometry
                        "Left",
                        "Middle",
                        "Right",  # Moments
                        "Vdl",
                        "V2hl",
                        "Vm",
                        "V2hr",
                        "Vdr",
                        "MaxTorsion",  # Shear Zones
                    ]

                    # THE FINAL STATE OF THE DATAFRAME ROUNDED TO 4 DECIMAL PLACES FOR BETTER READABILITY
                    df_final = df_final[desired_cols]
                    df_final = df_final.reset_index(drop=True)
                    df_final = df_final.round(4)

                    df_beam_conn = self.parent.etabs.get_data(
                        "Beam Object Connectivity"
                    )
                    df_col_conn = self.parent.etabs.get_data(
                        "Column Object Connectivity"
                    )

                    df_beam_conn = df_beam_conn.rename(
                        columns={"Unique Name": "UniqueName"}
                    )
                    df_col_conn = df_col_conn.rename(
                        columns={"Unique Name": "UniqueName"}
                    )

                    # CHECK IF BEAM IS CANTILEVER
                    def check_cantilever(row):
                        column_nodes = set(
                            df_col_conn["UniquePtI"].tolist()
                            + df_col_conn["UniquePtJ"].tolist()
                        )
                        # Find this specific beam in the connectivity table
                        beam_info = df_beam_conn[
                            (df_beam_conn["Story"] == row["Story"])
                            & (df_beam_conn["UniqueName"] == row["UniqueName"])
                        ]

                        if beam_info.empty:
                            return "N"

                        pt_i = beam_info["UniquePtI"].iloc[0]
                        pt_j = beam_info["UniquePtJ"].iloc[0]

                        # Logic: If point I OR point J is NOT in a column node, mark as Yes
                        if pt_i not in column_nodes or pt_j not in column_nodes:
                            return "Y"
                        else:
                            return "N"

                    df_final["Cantilever?"] = df_final.apply(check_cantilever, axis=1)

                    # INSERT THE CANTILEVER CLASSIFICATION COLUMN BEFORE THE MOMENT VALUES
                    cols = list(df_final.columns)
                    cols.insert(2, cols.pop(cols.index("Cantilever?")))
                    df_final = df_final[cols]

                    # DISPLAY THE FINAL DATAFRAME IN THE UI TABLE
                    self.parent.display_table_data(
                        df_final, self.parent.ui.design_forces
                    )
                    print(df)
                    print(df_final)

                    return df_final

                else:
                    print(f"Design failed with error code: {ret}")

            except Exception as e:
                print(f"An error occurred during design execution: {e}")
            finally:
                loading.close()

    class DeflectionController:
        def __init__(self, parent):
            self.parent = parent

    class ExportController:
        def __init__(self, parent):
            self.parent = parent


class AutoTaggerController:
    def __init__(self, ui_instance, etabs_instance):
        self.ui = ui_instance
        self.etabs = etabs_instance

        # Toggle Auto-Tagger Functionality
        self.ui.btn_toggle_auto_tagger.setFocus()
        self.ui.btn_toggle_auto_tagger.clicked.connect(
            lambda: self.toggle_auto_tagger()
        )

        self.ui.txt_tag_name.textChanged.connect(self.on_prefix_changed)
        self.ui.cmb_tag_number.currentIndexChanged.connect(self.on_number_changed)

        # Set Default Tag Name
        self.ui.txt_tag_name.clear()
        self.ui.txt_tag_name.setPlaceholderText("e.g. FTBX")

        # Set default states for combo boxes
        self.update_ui_state(False)

        # Generate Number Items for ComboBox
        number_list = [str(i) for i in range(1, 101)]
        alphabet_list = ["-"] + list(string.ascii_uppercase)
        self.ui.cmb_tag_number.addItems(number_list)
        self.ui.cmb_tag_letter.addItems(alphabet_list)
        self.ui.cmb_tag_number.view().setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        self.ui.cmb_tag_letter.view().setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.ui.cmb_tag_number.view().setAutoScroll(True)
        self.ui.cmb_tag_letter.view().setAutoScroll(True)
        self.ui.cmb_tag_number.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.ui.cmb_tag_letter.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.ui.cmb_tag_number.setMaxVisibleItems(10)
        self.ui.cmb_tag_letter.setMaxVisibleItems(10)

        self.ui.cmb_tag_number.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ui.cmb_tag_letter.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)

        # FORCE the initial state (Text + Icon)
        self.ui.btn_toggle_auto_tagger.setText("▶ ACTIVATE AUTO TAGGER")

        # Ensure it starts with the default gray style (not red)
        self.ui.btn_toggle_auto_tagger.setStyleSheet("")

    def update_ui_state(self, is_active):
        """
        Enables/Disables inputs based on whether the tool is active.
        """
        self.ui.txt_tag_name.setEnabled(is_active)
        self.ui.cmb_tag_number.setEnabled(is_active)
        self.ui.cmb_tag_letter.setEnabled(is_active)

        if not is_active:
            style = """
            QComboBox {
                background-color: white;
                color: black;
                border: 1px solid #AAA;
            }
            QComboBox:disabled {
                background-color: #F0F0F0;  /* Light Grey Background */
                color: #A0A0A0;             /* Dim Grey Text */
                border: 1px solid #D0D0D0;
            }
            """
            self.ui.cmb_tag_number.setStyleSheet(style)
            self.ui.cmb_tag_letter.setStyleSheet(style)

    def toggle_auto_tagger(self):
        """
        Switches between START and STOP modes based on current status.
        """
        # Check if the timer is currently running
        if hasattr(self, "selection_timer") and self.selection_timer.isActive():
            # --- CASE: IT IS RUNNING -> STOP IT ---
            self.selection_timer.stop()

            # 1. Update Button Appearance (Back to "Play")
            self.ui.btn_toggle_auto_tagger.setText("▶ ACTIVATE AUTO TAGGER")
            self.ui.btn_toggle_auto_tagger.setStyleSheet("")  # Reset to default color
            self.update_ui_state(False)

            # 2. Log and Feedback
            print("Auto-Tagger deactivated.")

        else:
            # --- CASE: IT IS STOPPED -> START IT ---

            # 1. Start the Timer (Reuse your existing start logic)
            # Make sure you have created the timer before calling start()
            if not hasattr(self, "selection_timer"):
                from PySide6.QtCore import QTimer

                self.selection_timer = QTimer()
                self.selection_timer.timeout.connect(
                    self.check_etabs_selection
                )  # Your scan function

            self.selection_timer.start(100)  # Run every 1 second
            self.update_ui_state(True)
            # 2. Update Button Appearance (Change to "Stop")
            self.ui.btn_toggle_auto_tagger.setText("■ STOP AUTO TAGGER")

            # 3. Change Button Color to Red (Visual Warning)
            self.ui.btn_toggle_auto_tagger.setStyleSheet("""
                background-color: #FFCDD2; 
                color: #C62828; 
                border: 1px solid #E57373;
                border-radius: 4px;
            """)

            # 4. Log
            print("Auto-Tagger activated.")

    def check_etabs_selection(self):
        """if self.check_etabs_connection() is False:
        return"""

        try:
            self.last_selection = self.etabs.get_unique_name()
            if self.last_selection == [] or self.last_selection is None:
                return
            else:
                print(f"New Selection Detected: {self.last_selection}")
                self.update_tagging(self.last_selection)
                self.etabs.clear_selection()
                self.etabs.refresh_view()

        except:
            pass

    def update_tagging(self, extracted_unique_name):
        try:
            ret = self.etabs.change_unique_name(
                extracted_unique_name,
                self.ui.txt_tag_name.text(),
                self.ui.cmb_tag_number.currentText(),
                self.ui.cmb_tag_letter.currentText(),
            )

            if ret == 0:
                self.ui.cmb_tag_number.blockSignals(True)
                self.ui.cmb_tag_letter.blockSignals(True)
                current_Index = self.ui.cmb_tag_letter.currentIndex()
                self.ui.cmb_tag_number.blockSignals(False)
                self.ui.cmb_tag_letter.blockSignals(False)

                if current_Index < self.ui.cmb_tag_letter.count() - 1:
                    self.ui.cmb_tag_letter.setCurrentIndex(current_Index + 1)

            else:
                print(f"Failed to rename {extracted_unique_name}. Error code: {ret}")

        except Exception as e:
            print(f"Exception occurred while renaming: {e}")

    def on_prefix_changed(self):
        """
        If Prefix changes (e.g. C -> B), reset Number and Letter to Index 0.
        """
        # Block signals temporarily if you want to prevent chain reactions,
        # but here we want a hard reset, so we just set them.
        self.ui.cmb_tag_number.setCurrentIndex(0)
        self.ui.cmb_tag_letter.setCurrentIndex(0)

    def on_number_changed(self):
        """
        If Number changes (e.g. 4 -> 5), reset Letter to Index 0 (-).
        """
        self.ui.cmb_tag_letter.setCurrentIndex(0)


class EmittingStream(QObject):
    textWritten = Signal(str)  # Define a signal that carries text

    def write(self, text):
        # When Python prints, it calls this function.
        # We emit a signal with the text instead of printing to console.
        self.textWritten.emit(str(text))

    def flush(self):
        # Needed for file-like compatibility
        pass


class LightThemePalette:
    @staticmethod
    def apply(app):
        # 1. Force the "Fusion" style
        app.setStyle("Fusion")

        # 2. Create a White/Light Palette
        palette = QPalette()

        # Window background (White)
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        palette.setColor(QPalette.WindowText, Qt.black)

        # Base background for inputs/tables (White)
        palette.setColor(QPalette.Base, QColor(255, 255, 255))
        palette.setColor(
            QPalette.AlternateBase, QColor(245, 245, 245)
        )  # Light grey for alternating rows
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.black)
        palette.setColor(QPalette.Text, Qt.black)

        # Buttons (Light Grey)
        palette.setColor(QPalette.Button, QColor(240, 240, 240))
        palette.setColor(QPalette.ButtonText, Qt.black)
        palette.setColor(QPalette.BrightText, Qt.red)

        # Highlight color (The ETABS blue selection color)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.white)

        # 3. Apply the palette to the app
        app.setPalette(palette)


if __name__ == "__main__":
    # SET THE UI THEME
    app = QApplication(sys.argv)
    LightThemePalette.apply(app)

    # RUN THE MAIN UI WINDOW
    window = DESIGNER_APP()
    window.showMaximized()
    sys.exit(app.exec())
