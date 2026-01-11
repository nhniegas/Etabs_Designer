# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QHeaderView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 638)
        icon = QIcon()
        icon.addFile(u"icons/ETABS_Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionBeam = QAction(MainWindow)
        self.actionBeam.setObjectName(u"actionBeam")
        self.actionColumn = QAction(MainWindow)
        self.actionColumn.setObjectName(u"actionColumn")
        self.actionExcel = QAction(MainWindow)
        self.actionExcel.setObjectName(u"actionExcel")
        self.actionNew_2 = QAction(MainWindow)
        self.actionNew_2.setObjectName(u"actionNew_2")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentNew))
        self.actionNew_2.setIcon(icon1)
        self.actionNew_2.setMenuRole(QAction.MenuRole.NoRole)
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.setObjectName(u"actionOpen_2")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.actionOpen_2.setIcon(icon2)
        self.actionOpen_2.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.actionSave_2.setIcon(icon3)
        self.actionSave_2.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSaveAs))
        self.actionSave_As.setIcon(icon4)
        self.actionSave_As.setMenuRole(QAction.MenuRole.NoRole)
        self.actionImport_Data = QAction(MainWindow)
        self.actionImport_Data.setObjectName(u"actionImport_Data")
        icon5 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.ViewRefresh):
            icon5 = QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh)
        else:
            icon5.addFile(u"icons/icons8-import-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionImport_Data.setIcon(icon5)
        self.actionImport_Data.setMenuRole(QAction.MenuRole.NoRole)
        self.actionDesign = QAction(MainWindow)
        self.actionDesign.setObjectName(u"actionDesign")
        icon6 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.DocumentSend):
            icon6 = QIcon.fromTheme(QIcon.ThemeIcon.DocumentSend)
        else:
            icon6.addFile(u"icons/icons8-reinforced-concrete-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionDesign.setIcon(icon6)
        self.actionDesign.setMenuRole(QAction.MenuRole.NoRole)
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        icon7 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.MediaTape):
            icon7 = QIcon.fromTheme(QIcon.ThemeIcon.MediaTape)
        else:
            icon7.addFile(u"icons/icons8-export-excel-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.actionExport.setIcon(icon7)
        self.actionExport.setMenuRole(QAction.MenuRole.NoRole)
        self.actionNhel_Pogi_The_Creator = QAction(MainWindow)
        self.actionNhel_Pogi_The_Creator.setObjectName(u"actionNhel_Pogi_The_Creator")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(150, 542))
        self.groupBox.setStyleSheet(u"border: none;")
        self.beam_design = QPushButton(self.groupBox)
        self.beam_design.setObjectName(u"beam_design")
        self.beam_design.setGeometry(QRect(10, 10, 131, 31))
        self.beam_design.setMinimumSize(QSize(120, 0))
        self.beam_design.setMaximumSize(QSize(250, 16777215))
        self.beam_design.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: #e0e0e0; /* Highlight on hover */\n"
"    font-weight: bold;\n"
"}")
        self.column_design = QPushButton(self.groupBox)
        self.column_design.setObjectName(u"column_design")
        self.column_design.setGeometry(QRect(10, 50, 131, 31))
        self.column_design.setMinimumSize(QSize(120, 0))
        self.column_design.setMaximumSize(QSize(250, 16777215))
        self.column_design.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: #e0e0e0; /* Highlight on hover */\n"
"    font-weight: bold;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.groupBox)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_2 = QGridLayout(self.page_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tab_widget = QTabWidget(self.page_5)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_material_data = QPushButton(self.tab)
        self.btn_material_data.setObjectName(u"btn_material_data")
        self.btn_material_data.setMinimumSize(QSize(150, 0))
        self.btn_material_data.setMaximumSize(QSize(250, 16777215))
        self.btn_material_data.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: #e0e0e0; /* Highlight on hover */\n"
"    font-weight: bold;\n"
"}")

        self.gridLayout.addWidget(self.btn_material_data, 0, 0, 1, 1)

        self.btn_shear = QPushButton(self.tab)
        self.btn_shear.setObjectName(u"btn_shear")
        self.btn_shear.setMinimumSize(QSize(150, 0))
        self.btn_shear.setMaximumSize(QSize(250, 16777215))
        self.btn_shear.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: #e0e0e0; /* Highlight on hover */\n"
"    font-weight: bold;\n"
"}")

        self.gridLayout.addWidget(self.btn_shear, 0, 4, 1, 1)

        self.btn_frame_property = QPushButton(self.tab)
        self.btn_frame_property.setObjectName(u"btn_frame_property")
        self.btn_frame_property.setMinimumSize(QSize(150, 0))
        self.btn_frame_property.setMaximumSize(QSize(250, 16777215))
        self.btn_frame_property.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: #e0e0e0; /* Highlight on hover */\n"
"    font-weight: bold;\n"
"}")

        self.gridLayout.addWidget(self.btn_frame_property, 0, 1, 1, 1)

        self.btn_frame_assignment = QPushButton(self.tab)
        self.btn_frame_assignment.setObjectName(u"btn_frame_assignment")
        self.btn_frame_assignment.setMinimumSize(QSize(150, 0))
        self.btn_frame_assignment.setMaximumSize(QSize(250, 16777215))
        self.btn_frame_assignment.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: #e0e0e0; /* Highlight on hover */\n"
"    font-weight: bold;\n"
"}")

        self.gridLayout.addWidget(self.btn_frame_assignment, 0, 2, 1, 1)

        self.btn_flexure = QPushButton(self.tab)
        self.btn_flexure.setObjectName(u"btn_flexure")
        self.btn_flexure.setMinimumSize(QSize(150, 0))
        self.btn_flexure.setMaximumSize(QSize(250, 16777215))
        self.btn_flexure.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    color: black;\n"
"    background-color: #e0e0e0; /* Highlight on hover */\n"
"    font-weight: bold;\n"
"}")

        self.gridLayout.addWidget(self.btn_flexure, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.raw_data = QTableWidget(self.tab)
        self.raw_data.setObjectName(u"raw_data")

        self.gridLayout.addWidget(self.raw_data, 1, 0, 1, 6)

        self.tab_widget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.designer_data = QTableWidget(self.tab_2)
        self.designer_data.setObjectName(u"designer_data")

        self.gridLayout_3.addWidget(self.designer_data, 0, 0, 1, 1)

        self.tab_widget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.export_data = QTableWidget(self.tab_3)
        self.export_data.setObjectName(u"export_data")
        self.export_data.setGeometry(QRect(20, 20, 551, 481))
        self.tab_widget.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tab_widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1180, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuRaw_Data = QMenu(self.menubar)
        self.menuRaw_Data.setObjectName(u"menuRaw_Data")
        self.menuDesigner = QMenu(self.menubar)
        self.menuDesigner.setObjectName(u"menuDesigner")
        self.menuExport = QMenu(self.menubar)
        self.menuExport.setObjectName(u"menuExport")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QToolBar(MainWindow)
        self.toolBar_3.setObjectName(u"toolBar_3")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_3)
        self.toolBar_4 = QToolBar(MainWindow)
        self.toolBar_4.setObjectName(u"toolBar_4")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_4)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRaw_Data.menuAction())
        self.menubar.addAction(self.menuDesigner.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuDesigner.addAction(self.actionBeam)
        self.menuDesigner.addAction(self.actionColumn)
        self.menuExport.addAction(self.actionExcel)
        self.menuExport.addSeparator()
        self.menuExport.addSeparator()
        self.menuExport.addSeparator()
        self.menuAbout.addAction(self.actionNhel_Pogi_The_Creator)
        self.toolBar.addAction(self.actionNew_2)
        self.toolBar.addAction(self.actionOpen_2)
        self.toolBar.addAction(self.actionSave_2)
        self.toolBar.addAction(self.actionSave_As)
        self.toolBar_2.addAction(self.actionImport_Data)
        self.toolBar_3.addAction(self.actionDesign)
        self.toolBar_4.addAction(self.actionExport)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Etabs_Designer", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as ", None))
        self.actionBeam.setText(QCoreApplication.translate("MainWindow", u"Beam", None))
        self.actionColumn.setText(QCoreApplication.translate("MainWindow", u"Column ", None))
        self.actionExcel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.actionNew_2.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(tooltip)
        self.actionNew_2.setToolTip(QCoreApplication.translate("MainWindow", u"Create New File ", None))
#endif // QT_CONFIG(tooltip)
        self.actionOpen_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen_2.setToolTip(QCoreApplication.translate("MainWindow", u"Open File", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(tooltip)
        self.actionSave_2.setToolTip(QCoreApplication.translate("MainWindow", u"Save File", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
#if QT_CONFIG(tooltip)
        self.actionSave_As.setToolTip(QCoreApplication.translate("MainWindow", u"Save As", None))
#endif // QT_CONFIG(tooltip)
        self.actionImport_Data.setText(QCoreApplication.translate("MainWindow", u"Import Data", None))
#if QT_CONFIG(tooltip)
        self.actionImport_Data.setToolTip(QCoreApplication.translate("MainWindow", u"Import Data", None))
#endif // QT_CONFIG(tooltip)
        self.actionDesign.setText(QCoreApplication.translate("MainWindow", u"Design", None))
#if QT_CONFIG(tooltip)
        self.actionDesign.setToolTip(QCoreApplication.translate("MainWindow", u"Design Members", None))
#endif // QT_CONFIG(tooltip)
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export ", None))
#if QT_CONFIG(tooltip)
        self.actionExport.setToolTip(QCoreApplication.translate("MainWindow", u"Export File", None))
#endif // QT_CONFIG(tooltip)
        self.actionNhel_Pogi_The_Creator.setText(QCoreApplication.translate("MainWindow", u"Nhel Pogi The Creator", None))
        self.groupBox.setTitle("")
        self.beam_design.setText(QCoreApplication.translate("MainWindow", u"BEAMS", None))
        self.column_design.setText(QCoreApplication.translate("MainWindow", u"COLUMNS", None))
        self.btn_material_data.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_shear.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_frame_property.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_frame_assignment.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_flexure.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Raw Data", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Designer", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Export ", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRaw_Data.setTitle(QCoreApplication.translate("MainWindow", u"Import Data", None))
        self.menuDesigner.setTitle(QCoreApplication.translate("MainWindow", u"Designer ", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export ", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.toolBar_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_3", None))
        self.toolBar_4.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_4", None))
    # retranslateUi

