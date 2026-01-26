import sys
import pandas as pd

from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

# This is the only "custom" import you need
from mainwindow_ui import Ui_MainWindow


class ETABSApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 2. Initialize the UI class
        self.ui = Ui_MainWindow()

        # 3. Call setupUi to draw the designer layout on this window
        try:
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
            print(self.sample_frame_section_properties)

        except Exception as e:
            print(f"Error loading sample data: {e}")

        self.ui.btn_material_data.clicked.connect(self.display_material_data)
        self.ui.btn_frame_property.clicked.connect(
            self.display_frame_section_properties
        )
        self.ui.btn_frame_assignment.clicked.connect(self.display_frame_assignment)
        self.ui.btn_flexure.clicked.connect(self.display_frame_flexure_envelope)
        self.ui.btn_shear.clicked.connect(self.display_frame_shear_envelope)


    def display_table(self, table_name):
        self.ui.raw_data.setRowCount(0)
        df = table_name
        self.ui.raw_data.setRowCount(df.shape[0])
        self.ui.raw_data.setColumnCount(df.shape[1])

        headers = [str(col) for col in df.columns.tolist()]
        self.ui.raw_data.setHorizontalHeaderLabels(headers)

        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                value = str(df.iat[i, j])
                self.ui.raw_data.setItem(i, j, QTableWidgetItem(value))


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
