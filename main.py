import sys
import os
import string
import pandas as pd

from PySide6.QtCore import Qt, QTimer, QObject, Signal
from PySide6.QtGui import QPalette, QColor, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

# This is the only "custom" import you need
from mainwindow_ui import Ui_MainWindow
from modules.etabs_api import ETABSConnector


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class ETABSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # FORCE the initial state (Text + Icon)
        self.ui.btn_toggle_auto_tagger.setText("▶ ACTIVATE AUTO TAGGER")

        # Ensure it starts with the default gray style (not red)
        self.ui.btn_toggle_auto_tagger.setStyleSheet("")

        # Redirect stdout to the GUIsa
        self.sys_stdout = EmittingStream()
        self.sys_stdout.textWritten.connect(self.append_log)
        sys.stdout = self.sys_stdout

        self.setWindowIcon(QIcon(resource_path("Etabs_Logo.ico")))

        # Call setupUi to draw the designer layout on this window
        try:
            self.etabs = ETABSConnector()

            self.sample_material_data = pd.read_csv("sample/sample_material_data.csv")
            self.sample_frame_section_properties = pd.read_csv(
                "sample/sample_frame_section_properties.csv"
            )
            self.sample_frame_assignment = pd.read_csv(
                "sample/sample_frame_assignment.csv"
            )
            self.sample_beam_flexure_envelope = pd.read_csv(
                "sample/sample_beam_flexure_envelope.csv"
            )
            self.sample_beam_shear_envelope = pd.read_csv(
                "sample/sample_beam_shear_envelope.csv"
            )

        except Exception as e:
            print(f"Error loading sample data: {e}")

        # Connect buttons to functions
        self.ui.btn_material_data.clicked.connect(
            lambda: self.display_table(self.sample_material_data)
        )
        self.ui.btn_frame_property.clicked.connect(
            lambda: self.display_table(self.sample_frame_section_properties)
        )
        self.ui.btn_frame_assignment.clicked.connect(
            lambda: self.display_table(self.sample_frame_assignment)
        )
        self.ui.btn_flexure.clicked.connect(
            lambda: self.display_table(self.sample_beam_flexure_envelope)
        )
        self.ui.btn_shear.clicked.connect(
            lambda: self.display_table(self.sample_beam_shear_envelope)
        )

        # Navigte To Auto-Tagger Widget
        self.ui.btn_auto_tagger.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_auto_tagger)
        )
        self.ui.btn_auto_tagger.clicked.connect(
            lambda: self.animate_click(self.ui.btn_auto_tagger)
        )

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

        # Open Etabs Model
        self.ui.menu_Open.triggered.connect(lambda: self.open_model())

        self.update_ui_state(False)

        # Function to handle file paths when bundled in an EXE

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

            self.selection_timer.start(1000)  # Run every 1 second
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
                self.change_unique_name(self.last_selection)
                self.etabs.clear_selection()
                self.etabs.refresh_view()

        except:
            pass

    def change_unique_name(self, extracted_unique_name):
        try:
            current_unique_name = extracted_unique_name

            if self.ui.cmb_tag_letter.currentText() == "-":
                new_unique_name = f"{self.ui.txt_tag_name.text()}-{self.ui.cmb_tag_number.currentText()}"
            else:
                new_unique_name = f"{self.ui.txt_tag_name.text()}-{self.ui.cmb_tag_number.currentText()}{self.ui.cmb_tag_letter.currentText()}"

            ret = self.etabs.sap_model.FrameObj.ChangeName(
                current_unique_name, new_unique_name
            )

            if ret == 0:
                print(
                    f"Renamed {current_unique_name} to {new_unique_name} successfully."
                )

                self.ui.cmb_tag_number.blockSignals(True)
                self.ui.cmb_tag_letter.blockSignals(True)
                current_Index = self.ui.cmb_tag_letter.currentIndex()
                self.ui.cmb_tag_number.blockSignals(False)
                self.ui.cmb_tag_letter.blockSignals(False)

                if current_Index < self.ui.cmb_tag_letter.count() - 1:
                    self.ui.cmb_tag_letter.setCurrentIndex(current_Index + 1)

            else:
                print(f"Failed to rename {current_unique_name}. Error code: {ret}")

        except Exception as e:
            print(f"Exception occurred while renaming: {e}")

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
        except Exception as e:
            print(f"Error opening model: {e}")
        finally:
            loading.close()

    def check_etabs_connection(self):
        if not hasattr(self, "etabs") or self.etabs is None:
            return False

        try:
            if self.etabs.is_connected:
                return True

        except Exception as e:
            print(f"Error checking ETABS connection: {e}")
            return False

    def closeEvent(self, event):
        try:
            self.etabs.close_model()
            sys.stdout = sys.__stdout__
            super().closeEvent(event)
        except Exception as e:
            print(f"Error closing ETABS model: {e}")

    def display_table(self, df):
        self.ui.raw_data.setRowCount(0)

        table = df
        self.ui.raw_data.setRowCount(table.shape[0])
        self.ui.raw_data.setColumnCount(table.shape[1])

        headers = [str(col) for col in table.columns.tolist()]
        self.ui.raw_data.setHorizontalHeaderLabels(headers)

        for i in range(table.shape[0]):
            for j in range(table.shape[1]):
                value = str(table.iat[i, j])
                self.ui.raw_data.setItem(i, j, QTableWidgetItem(value))

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

        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)

        # Reset to PERFECT normal size when done
        self.anim.finished.connect(lambda: button.setIconSize(normal_size))

        self.anim.start()

    def append_log(self, text):
        # Move cursor to the end so it auto-scrolls
        cursor = self.ui.console_log.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.ui.console_log.setTextCursor(cursor)

        # Insert the text
        self.ui.console_log.insertPlainText(text)

        # Ensure the scrollbar follows the text
        self.ui.console_log.verticalScrollBar().setValue(
            self.ui.console_log.verticalScrollBar().maximum()
        )


class EmittingStream(QObject):
    textWritten = Signal(str)  # Define a signal that carries text

    def write(self, text):
        # When Python prints, it calls this function.
        # We emit a signal with the text instead of printing to console.
        self.textWritten.emit(str(text))

    def flush(self):
        # Needed for file-like compatibility
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 1. Force the "Fusion" style (Clean, professional look)
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

    # Now this line will work because the class is defined above!
    window = ETABSApp()
    window.showMaximized()

    sys.exit(app.exec())
