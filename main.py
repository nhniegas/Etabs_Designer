import sys
import string
import pandas as pd

from PySide6.QtCore import Qt, QTimer, QObject, Signal
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

# This is the only "custom" import you need
from mainwindow_ui import Ui_MainWindow
from modules.etabs_api import ETABSConnector


class ETABSApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Redirect stdout to the GUI
        self.sys_stdout = EmittingStream()
        self.sys_stdout.textWritten.connect(self.append_log)

        sys.stdout = self.sys_stdout

        # Initialize the UI class
        self.ui = Ui_MainWindow()

        # Call setupUi to draw the designer layout on this window
        try:
            self.etabs = ETABSConnector()
            self.ui.setupUi(self)

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

        # Activate Auto-Tagger Functionality
        self.ui.btn_activate_auto_tagger.clicked.connect(
            lambda: self.activate_auto_tagger()
        )

        # De-activate Auto-Tagger Functionality
        self.ui.btn_deactivate_auto_tagger.clicked.connect(
            lambda: self.deactivate_auto_tagger()
        )

        # Generate Number Items for ComboBox
        number_list = [str(i) for i in range(1, 101)]
        self.ui.cmb_tag_number.addItems(number_list)
        self.ui.cmb_tag_number.view().setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.ui.cmb_tag_number.view().setAutoScroll(True)
        self.ui.cmb_tag_number.setStyleSheet("QComboBox { combobox-popup: 0; }")
        self.ui.cmb_tag_number.setMaxVisibleItems(10)

        # Open Etabs Model
        self.ui.menu_Open.triggered.connect(lambda: self.open_model())

    def activate_auto_tagger(self):
        """if self.check_etabs_connection() is False:
        return"""

        try:
            self.last_selection = []
            self.selection_timer = QTimer()
            self.selection_timer.setInterval(1000)
            self.selection_timer.timeout.connect(self.check_etabs_selection)
            self.selection_timer.start()
            print("Auto-Tagger Activated")

        except Exception as e:
            print(f"Error activating auto-tagger: {e}")

    def deactivate_auto_tagger(self):
        """if self.check_etabs_connection() is False:
        return"""

        try:
            self.selection_timer.stop()
            print("Auto-Tagger De-Activated")

        except Exception as e:
            print(f"Error deactivating auto-tagger: {e}")

    def check_etabs_selection(self):
        """if self.check_etabs_connection() is False:
        return"""

        try:
            self.last_selection = self.etabs.get_selected_frames()

            if self.last_selection == [] or self.last_selection is None:
                return
            else:
                print(f"New Selection Detected: {self.last_selection}")
                self.etabs.clear_selection()
                self.etabs.refresh_view()

                import pandas as pd

                df = pd.DataFrame(self.last_selection, columns=["Unique Name"])
                self.display_table(df)

        except:
            pass

    def open_model(self):
        from PySide6.QtWidgets import QFileDialog, QProgressDialog, QApplication
        from PySide6.QtCore import Qt

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open ETABS Model",
            r"C:\Users\Acer\Desktop\Etabs_Sample_API_Test",
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
