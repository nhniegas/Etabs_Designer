# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1361, 777)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../../.designer/backup/icons/ETABS_Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.menu_Open = QAction(MainWindow)
        self.menu_Open.setObjectName(u"menu_Open")
        self.actionBeam = QAction(MainWindow)
        self.actionBeam.setObjectName(u"actionBeam")
        self.actionColumn = QAction(MainWindow)
        self.actionColumn.setObjectName(u"actionColumn")
        self.actionExcel = QAction(MainWindow)
        self.actionExcel.setObjectName(u"actionExcel")
        self.actionOpenEtabs = QAction(MainWindow)
        self.actionOpenEtabs.setObjectName(u"actionOpenEtabs")
        icon1 = QIcon()
        icon1.addFile(u"../../.designer/backup/icons/OPEN.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionOpenEtabs.setIcon(icon1)
        self.actionOpenEtabs.setMenuRole(QAction.MenuRole.NoRole)
        self.actionReloadData = QAction(MainWindow)
        self.actionReloadData.setObjectName(u"actionReloadData")
        icon2 = QIcon()
        icon2.addFile(u"../../.designer/backup/icons/RELOAD.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionReloadData.setIcon(icon2)
        self.actionReloadData.setMenuRole(QAction.MenuRole.NoRole)
        self.ActionRunDesign = QAction(MainWindow)
        self.ActionRunDesign.setObjectName(u"ActionRunDesign")
        icon3 = QIcon()
        icon3.addFile(u"../../.designer/backup/icons/RUN.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ActionRunDesign.setIcon(icon3)
        self.ActionRunDesign.setMenuRole(QAction.MenuRole.NoRole)
        self.actionNhel_Pogi_The_Creator = QAction(MainWindow)
        self.actionNhel_Pogi_The_Creator.setObjectName(u"actionNhel_Pogi_The_Creator")
        self.ActionDownload = QAction(MainWindow)
        self.ActionDownload.setObjectName(u"ActionDownload")
        icon4 = QIcon()
        icon4.addFile(u"../../.designer/backup/icons/DOWNLOAD.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ActionDownload.setIcon(icon4)
        self.ActionDownload.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1357, 740))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 450))
        self.groupBox.setMaximumSize(QSize(200, 16777215))
        self.groupBox.setStyleSheet(u"border: none;\n"
"\n"
"background-color: #f6f9ff;  /* Super Light Blue */\n"
"border-radius: 6px;")
        self.beam_design = QPushButton(self.groupBox)
        self.beam_design.setObjectName(u"beam_design")
        self.beam_design.setGeometry(QRect(25, 160, 151, 121))
        self.beam_design.setMinimumSize(QSize(120, 0))
        self.beam_design.setMaximumSize(QSize(250, 16777215))
        self.beam_design.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    /* Hover State: Very light gray/almost white */\n"
"    background-color: #f5f5f5; \n"
"    border: 1px solid #cccccc;\n"
"    /* Change text to dark gray so it's visible on the light background */\n"
"    color: #333333; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Pressed State: Standard mid-gray */\n"
"    background-color: #d0d0d0; \n"
"    color: #000000;\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icons/BEAM.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.beam_design.setIcon(icon5)
        self.beam_design.setIconSize(QSize(65, 65))
        self.column_design = QPushButton(self.groupBox)
        self.column_design.setObjectName(u"column_design")
        self.column_design.setGeometry(QRect(25, 309, 151, 121))
        self.column_design.setMinimumSize(QSize(120, 0))
        self.column_design.setMaximumSize(QSize(250, 16777215))
        self.column_design.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    /* Hover State: Very light gray/almost white */\n"
"    background-color: #f5f5f5; \n"
"    border: 1px solid #cccccc;\n"
"    /* Change text to dark gray so it's visible on the light background */\n"
"    color: #333333; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Pressed State: Standard mid-gray */\n"
"    background-color: #d0d0d0; \n"
"    color: #000000;\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"icons/COLUMN.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.column_design.setIcon(icon6)
        self.column_design.setIconSize(QSize(100, 100))
        self.btn_auto_tagger = QPushButton(self.groupBox)
        self.btn_auto_tagger.setObjectName(u"btn_auto_tagger")
        self.btn_auto_tagger.setGeometry(QRect(24, 20, 151, 121))
        self.btn_auto_tagger.setMinimumSize(QSize(120, 0))
        self.btn_auto_tagger.setMaximumSize(QSize(250, 16777215))
        self.btn_auto_tagger.setStyleSheet(u"QPushButton {\n"
"    border: none;             /* No button border */\n"
"    background: transparent;  /* No grey background */\n"
"    text-align: center;         /* Align text like a label */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    /* Hover State: Very light gray/almost white */\n"
"    background-color: #f5f5f5; \n"
"    border: 1px solid #cccccc;\n"
"    /* Change text to dark gray so it's visible on the light background */\n"
"    color: #333333; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Pressed State: Standard mid-gray */\n"
"    background-color: #d0d0d0; \n"
"    color: #000000;\n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"icons/AUTO TAGGER.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_auto_tagger.setIcon(icon7)
        self.btn_auto_tagger.setIconSize(QSize(100, 100))

        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1000, 450))
        self.page_beam_design = QWidget()
        self.page_beam_design.setObjectName(u"page_beam_design")
        self.gridLayout_2 = QGridLayout(self.page_beam_design)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tab_widget = QTabWidget(self.page_beam_design)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_section_data = QPushButton(self.tab)
        self.btn_section_data.setObjectName(u"btn_section_data")
        self.btn_section_data.setMinimumSize(QSize(150, 0))
        self.btn_section_data.setMaximumSize(QSize(250, 16777215))
        self.btn_section_data.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")

        self.gridLayout.addWidget(self.btn_section_data, 0, 0, 1, 1)

        self.btn_concrete_material = QPushButton(self.tab)
        self.btn_concrete_material.setObjectName(u"btn_concrete_material")
        self.btn_concrete_material.setMinimumSize(QSize(150, 0))
        self.btn_concrete_material.setMaximumSize(QSize(250, 16777215))
        self.btn_concrete_material.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")

        self.gridLayout.addWidget(self.btn_concrete_material, 0, 1, 1, 1)

        self.btn_rebar_material = QPushButton(self.tab)
        self.btn_rebar_material.setObjectName(u"btn_rebar_material")
        self.btn_rebar_material.setMinimumSize(QSize(150, 0))
        self.btn_rebar_material.setMaximumSize(QSize(250, 16777215))
        self.btn_rebar_material.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")

        self.gridLayout.addWidget(self.btn_rebar_material, 0, 2, 1, 1)

        self.btn_frame_assignment = QPushButton(self.tab)
        self.btn_frame_assignment.setObjectName(u"btn_frame_assignment")
        self.btn_frame_assignment.setMinimumSize(QSize(150, 0))
        self.btn_frame_assignment.setMaximumSize(QSize(250, 16777215))
        self.btn_frame_assignment.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")

        self.gridLayout.addWidget(self.btn_frame_assignment, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 4, 1, 1)

        self.raw_data = QTableView(self.tab)
        self.raw_data.setObjectName(u"raw_data")

        self.gridLayout.addWidget(self.raw_data, 1, 0, 1, 5)

        self.tab_widget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox_3 = QGroupBox(self.tab_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(9, 9, 500, 311))
        self.groupBox_3.setMinimumSize(QSize(500, 300))
        self.groupBox_3.setMaximumSize(QSize(500, 16777215))
        self.combo_list = QListWidget(self.groupBox_3)
        self.combo_list.setObjectName(u"combo_list")
        self.combo_list.setGeometry(QRect(10, 10, 191, 291))
        self.combo_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.add_uls = QPushButton(self.groupBox_3)
        self.add_uls.setObjectName(u"add_uls")
        self.add_uls.setGeometry(QRect(210, 60, 81, 26))
        self.add_uls.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")
        self.add_sls = QPushButton(self.groupBox_3)
        self.add_sls.setObjectName(u"add_sls")
        self.add_sls.setGeometry(QRect(210, 200, 81, 26))
        self.add_sls.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")
        self.sls_combo_list = QListWidget(self.groupBox_3)
        self.sls_combo_list.setObjectName(u"sls_combo_list")
        self.sls_combo_list.setGeometry(QRect(300, 160, 191, 141))
        self.sls_combo_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.uls_combo_list = QListWidget(self.groupBox_3)
        self.uls_combo_list.setObjectName(u"uls_combo_list")
        self.uls_combo_list.setGeometry(QRect(300, 10, 191, 141))
        self.uls_combo_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.remove_uls = QPushButton(self.groupBox_3)
        self.remove_uls.setObjectName(u"remove_uls")
        self.remove_uls.setGeometry(QRect(210, 90, 81, 26))
        self.remove_uls.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")
        self.remove_sls = QPushButton(self.groupBox_3)
        self.remove_sls.setObjectName(u"remove_sls")
        self.remove_sls.setGeometry(QRect(210, 230, 81, 26))
        self.remove_sls.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")
        self.groupBox_5 = QGroupBox(self.tab_4)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 327, 500, 271))
        self.groupBox_5.setMinimumSize(QSize(500, 250))
        self.remove_beams = QPushButton(self.groupBox_5)
        self.remove_beams.setObjectName(u"remove_beams")
        self.remove_beams.setGeometry(QRect(210, 130, 81, 26))
        self.remove_beams.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")
        self.beam_list = QListWidget(self.groupBox_5)
        self.beam_list.setObjectName(u"beam_list")
        self.beam_list.setGeometry(QRect(10, 10, 191, 251))
        self.beam_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.selected_beam_list = QListWidget(self.groupBox_5)
        self.selected_beam_list.setObjectName(u"selected_beam_list")
        self.selected_beam_list.setGeometry(QRect(300, 10, 191, 251))
        self.selected_beam_list.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.add_beams = QPushButton(self.groupBox_5)
        self.add_beams.setObjectName(u"add_beams")
        self.add_beams.setGeometry(QRect(210, 100, 81, 26))
        self.add_beams.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")
        self.groupBox_4 = QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(530, 4, 561, 191))
        font = QFont()
        font.setPointSize(9)
        self.groupBox_4.setFont(font)
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(25, 29, 81, 16))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(25, 59, 211, 16))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(25, 90, 161, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(25, 120, 101, 16))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 156, 121, 16))
        self.label_6.setFont(font)
        self.cmb_gravity_load_combo = QComboBox(self.groupBox_4)
        self.cmb_gravity_load_combo.setObjectName(u"cmb_gravity_load_combo")
        self.cmb_gravity_load_combo.setGeometry(QRect(400, 154, 131, 26))
        self.max_rho = QCheckBox(self.groupBox_4)
        self.max_rho.setObjectName(u"max_rho")
        self.max_rho.setGeometry(QRect(511, 25, 31, 24))
        self.max_rho.setStyleSheet(u"/* Make the default internal box invisible so it doesn't clash */\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 1px solid black;\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* When checked, we just change the box background slightly */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #f0f0f0; \n"
"    image: none; /* Ensure no broken red hatch shows up */\n"
"}\n"
"\n"
"/* Style the text (the Label part) to look like a checkmark */\n"
"QCheckBox {\n"
"    font-size: 16px;\n"
"    color: black;\n"
"    /* This 'pulls' the checkmark character into the box area */\n"
"    spacing: -17px; \n"
"    padding-left: 2px;\n"
"}")
        self.half_moment = QCheckBox(self.groupBox_4)
        self.half_moment.setObjectName(u"half_moment")
        self.half_moment.setGeometry(QRect(511, 55, 31, 24))
        self.half_moment.setStyleSheet(u"/* Make the default internal box invisible so it doesn't clash */\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 1px solid black;\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* When checked, we just change the box background slightly */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #f0f0f0; \n"
"    image: none; /* Ensure no broken red hatch shows up */\n"
"}\n"
"\n"
"/* Style the text (the Label part) to look like a checkmark */\n"
"QCheckBox {\n"
"    font-size: 16px;\n"
"    color: black;\n"
"    /* This 'pulls' the checkmark character into the box area */\n"
"    spacing: -17px; \n"
"    padding-left: 2px;\n"
"}")
        self.fourth_moment = QCheckBox(self.groupBox_4)
        self.fourth_moment.setObjectName(u"fourth_moment")
        self.fourth_moment.setGeometry(QRect(511, 85, 31, 24))
        self.fourth_moment.setStyleSheet(u"/* Make the default internal box invisible so it doesn't clash */\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 1px solid black;\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* When checked, we just change the box background slightly */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #f0f0f0; \n"
"    image: none; /* Ensure no broken red hatch shows up */\n"
"}\n"
"\n"
"/* Style the text (the Label part) to look like a checkmark */\n"
"QCheckBox {\n"
"    font-size: 16px;\n"
"    color: black;\n"
"    /* This 'pulls' the checkmark character into the box area */\n"
"    spacing: -17px; \n"
"    padding-left: 2px;\n"
"}")
        self.prob_shear = QCheckBox(self.groupBox_4)
        self.prob_shear.setObjectName(u"prob_shear")
        self.prob_shear.setGeometry(QRect(511, 115, 31, 24))
        self.prob_shear.setStyleSheet(u"/* Make the default internal box invisible so it doesn't clash */\n"
"QCheckBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border: 1px solid black;\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* When checked, we just change the box background slightly */\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #f0f0f0; \n"
"    image: none; /* Ensure no broken red hatch shows up */\n"
"}\n"
"\n"
"/* Style the text (the Label part) to look like a checkmark */\n"
"QCheckBox {\n"
"    font-size: 16px;\n"
"    color: black;\n"
"    /* This 'pulls' the checkmark character into the box area */\n"
"    spacing: -17px; \n"
"    padding-left: 2px;\n"
"}")
        self.groupBox_6 = QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(210, 210, 331, 211))
        self.groupBox_6.setFont(font)
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 44, 81, 16))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 74, 211, 16))
        self.label_8.setFont(font)
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 105, 161, 16))
        self.label_9.setFont(font)
        self.label_10 = QLabel(self.groupBox_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 135, 101, 16))
        self.label_10.setFont(font)
        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(35, 171, 121, 16))
        self.label_11.setFont(font)
        self.comboBox_2 = QComboBox(self.groupBox_6)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(199, 169, 111, 26))
        self.checkBox_5 = QCheckBox(self.groupBox_6)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(290, 40, 21, 24))
        self.checkBox_6 = QCheckBox(self.groupBox_6)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(290, 70, 21, 24))
        self.checkBox_7 = QCheckBox(self.groupBox_6)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(290, 100, 21, 24))
        self.checkBox_8 = QCheckBox(self.groupBox_6)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(290, 130, 21, 24))
        self.groupBox_9 = QGroupBox(self.tab_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(530, 199, 561, 121))
        self.groupBox_9.setFont(font)
        self.label_13 = QLabel(self.groupBox_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 41, 211, 16))
        self.label_13.setFont(font)
        self.groupBox_10 = QGroupBox(self.groupBox_9)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(210, 210, 331, 211))
        self.groupBox_10.setFont(font)
        self.label_17 = QLabel(self.groupBox_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 44, 81, 16))
        self.label_17.setFont(font)
        self.label_18 = QLabel(self.groupBox_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 74, 211, 16))
        self.label_18.setFont(font)
        self.label_19 = QLabel(self.groupBox_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 105, 161, 16))
        self.label_19.setFont(font)
        self.label_20 = QLabel(self.groupBox_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 135, 101, 16))
        self.label_20.setFont(font)
        self.label_21 = QLabel(self.groupBox_10)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(35, 171, 121, 16))
        self.label_21.setFont(font)
        self.comboBox_4 = QComboBox(self.groupBox_10)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(199, 169, 111, 26))
        self.checkBox_13 = QCheckBox(self.groupBox_10)
        self.checkBox_13.setObjectName(u"checkBox_13")
        self.checkBox_13.setGeometry(QRect(290, 40, 21, 24))
        self.checkBox_14 = QCheckBox(self.groupBox_10)
        self.checkBox_14.setObjectName(u"checkBox_14")
        self.checkBox_14.setGeometry(QRect(290, 70, 21, 24))
        self.checkBox_15 = QCheckBox(self.groupBox_10)
        self.checkBox_15.setObjectName(u"checkBox_15")
        self.checkBox_15.setGeometry(QRect(290, 100, 21, 24))
        self.checkBox_16 = QCheckBox(self.groupBox_10)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setGeometry(QRect(290, 130, 21, 24))
        self.comboBox_5 = QComboBox(self.groupBox_9)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(440, 40, 89, 26))
        self.comboBox_6 = QComboBox(self.groupBox_9)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(440, 72, 89, 26))
        self.label_15 = QLabel(self.groupBox_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 73, 211, 16))
        self.label_15.setFont(font)
        self.extract_etabs_forces = QPushButton(self.tab_4)
        self.extract_etabs_forces.setObjectName(u"extract_etabs_forces")
        self.extract_etabs_forces.setGeometry(QRect(535, 330, 550, 29))
        self.extract_etabs_forces.setMinimumSize(QSize(250, 0))
        self.extract_etabs_forces.setMaximumSize(QSize(550, 16777215))
        self.extract_etabs_forces.setStyleSheet(u"QPushButton {\n"
"    /* Lighter grey background to match the window theme */\n"
"    background-color: #f0f0f0; \n"
"    /* Subtle border to match the QListWidget headers */\n"
"    border: 1px solid #dcdcdc; \n"
"    border-radius: 4px;\n"
"    /* Darker text for readability on light background */\n"
"    color: #333333; \n"
"    padding: 6px;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Lighter, softer red for the light theme */\n"
"    background-color: #ef9a9a; \n"
"    border: 1px solid #e57373;\n"
"    color: #333333; /* Switching to dark text for better contrast on light red */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Slightly deeper red when clicked */\n"
"    background-color: #ee5253; \n"
"}")
        self.tab_widget.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout = QVBoxLayout(self.tab_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.design_forces = QTableView(self.tab_6)
        self.design_forces.setObjectName(u"design_forces")

        self.verticalLayout.addWidget(self.design_forces)

        self.tab_widget.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.reinforcement_design = QTableWidget(self.tab_2)
        self.reinforcement_design.setObjectName(u"reinforcement_design")

        self.gridLayout_3.addWidget(self.reinforcement_design, 0, 0, 1, 1)

        self.tab_widget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_widget.addTab(self.tab_5, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.export_data = QTableWidget(self.tab_3)
        self.export_data.setObjectName(u"export_data")
        self.export_data.setGeometry(QRect(20, 20, 551, 481))
        self.tab_widget.addTab(self.tab_3, "")

        self.gridLayout_2.addWidget(self.tab_widget, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_beam_design)
        self.page_auto_tagger = QWidget()
        self.page_auto_tagger.setObjectName(u"page_auto_tagger")
        self.btn_toggle_auto_tagger = QPushButton(self.page_auto_tagger)
        self.btn_toggle_auto_tagger.setObjectName(u"btn_toggle_auto_tagger")
        self.btn_toggle_auto_tagger.setGeometry(QRect(400, 110, 341, 41))
        self.groupBox_2 = QGroupBox(self.page_auto_tagger)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(240, 180, 661, 151))
        self.lbl_input_tag = QLabel(self.groupBox_2)
        self.lbl_input_tag.setObjectName(u"lbl_input_tag")
        self.lbl_input_tag.setGeometry(QRect(50, 40, 171, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.lbl_input_tag.setFont(font1)
        self.txt_tag_name = QLineEdit(self.groupBox_2)
        self.txt_tag_name.setObjectName(u"txt_tag_name")
        self.txt_tag_name.setEnabled(True)
        self.txt_tag_name.setGeometry(QRect(250, 50, 151, 41))
        self.txt_tag_name.setFont(font1)
        self.txt_tag_name.setStyleSheet(u"QLineEdit {\n"
"    placeholder-text-color: #888888; /* Forces the hint text to be Dark Grey */\n"
"}")
        self.txt_tag_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cmb_tag_number = QComboBox(self.groupBox_2)
        self.cmb_tag_number.setObjectName(u"cmb_tag_number")
        self.cmb_tag_number.setEnabled(True)
        self.cmb_tag_number.setGeometry(QRect(470, 50, 72, 41))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cmb_tag_number.sizePolicy().hasHeightForWidth())
        self.cmb_tag_number.setSizePolicy(sizePolicy2)
        self.cmb_tag_number.setFont(font1)
        self.cmb_tag_number.setStyleSheet(u"")
        self.cmb_tag_number.setEditable(True)
        self.cmb_tag_letter = QComboBox(self.groupBox_2)
        self.cmb_tag_letter.setObjectName(u"cmb_tag_letter")
        self.cmb_tag_letter.setEnabled(True)
        self.cmb_tag_letter.setGeometry(QRect(550, 50, 71, 41))
        self.cmb_tag_letter.setFont(font1)
        self.cmb_tag_letter.setEditable(True)
        self.lbl_input_tag_2 = QLabel(self.groupBox_2)
        self.lbl_input_tag_2.setObjectName(u"lbl_input_tag_2")
        self.lbl_input_tag_2.setGeometry(QRect(420, 40, 41, 41))
        font2 = QFont()
        font2.setPointSize(50)
        self.lbl_input_tag_2.setFont(font2)
        self.stackedWidget.addWidget(self.page_auto_tagger)

        self.gridLayout_5.addWidget(self.stackedWidget, 0, 1, 4, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Monospac821 BT"])
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"border: none;\n"
"background: transparent;")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.console_log = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.console_log.setObjectName(u"console_log")
        self.console_log.setMinimumSize(QSize(0, 170))
        self.console_log.setMaximumSize(QSize(200, 200))
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(10)
        font4.setItalic(False)
        self.console_log.setFont(font4)
        self.console_log.setStyleSheet(u"border: 1px solid #A0A0A0; /* A thin, solid gray border */\n"
"border-radius: 4px;        /* Optional: Rounds the corners slightly */\n"
"padding: 4px;              /* Optional: Adds space between text and border */\n"
"\n"
"   /* 1. The Font Chain: Try Consolas first, fail over to Courier New */\n"
"   font-family: \"Consolas\", \"Courier New\", monospace;\n"
"    \n"
"   /* 2. Size: Logs are usually slightly smaller than normal text */\n"
"   font-size: 10pt; \n"
"    ")
        self.console_log.setReadOnly(True)

        self.gridLayout_5.addWidget(self.console_log, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 44, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1361, 33))
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

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRaw_Data.menuAction())
        self.menubar.addAction(self.menuDesigner.menuAction())
        self.menubar.addAction(self.menuExport.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.menu_Open)
        self.menuDesigner.addAction(self.actionBeam)
        self.menuDesigner.addAction(self.actionColumn)
        self.menuExport.addAction(self.actionExcel)
        self.menuExport.addSeparator()
        self.menuExport.addSeparator()
        self.menuExport.addSeparator()
        self.menuAbout.addAction(self.actionNhel_Pogi_The_Creator)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tab_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Etabs_Designer", None))
        self.menu_Open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.menu_Open.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.actionBeam.setText(QCoreApplication.translate("MainWindow", u"Beam", None))
        self.actionColumn.setText(QCoreApplication.translate("MainWindow", u"Column ", None))
        self.actionExcel.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.actionOpenEtabs.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpenEtabs.setToolTip(QCoreApplication.translate("MainWindow", u"Open File", None))
#endif // QT_CONFIG(tooltip)
        self.actionReloadData.setText(QCoreApplication.translate("MainWindow", u"Import Data", None))
#if QT_CONFIG(tooltip)
        self.actionReloadData.setToolTip(QCoreApplication.translate("MainWindow", u"Import Data", None))
#endif // QT_CONFIG(tooltip)
        self.ActionRunDesign.setText(QCoreApplication.translate("MainWindow", u"Design", None))
#if QT_CONFIG(tooltip)
        self.ActionRunDesign.setToolTip(QCoreApplication.translate("MainWindow", u"Design Members", None))
#endif // QT_CONFIG(tooltip)
        self.actionNhel_Pogi_The_Creator.setText(QCoreApplication.translate("MainWindow", u"Nhel Pogi The Creator", None))
        self.ActionDownload.setText(QCoreApplication.translate("MainWindow", u"Download", None))
#if QT_CONFIG(tooltip)
        self.ActionDownload.setToolTip(QCoreApplication.translate("MainWindow", u"Download Excel", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle("")
        self.beam_design.setText("")
        self.column_design.setText("")
        self.btn_auto_tagger.setText("")
        self.btn_section_data.setText(QCoreApplication.translate("MainWindow", u"Section Data", None))
        self.btn_concrete_material.setText(QCoreApplication.translate("MainWindow", u"Concrete Material", None))
        self.btn_rebar_material.setText(QCoreApplication.translate("MainWindow", u"Rebar Material", None))
        self.btn_frame_assignment.setText(QCoreApplication.translate("MainWindow", u"Frame Assignement", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Property Data", None))
        self.groupBox_3.setTitle("")
        self.add_uls.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.add_sls.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.remove_uls.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.remove_sls.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.groupBox_5.setTitle("")
        self.remove_beams.setText(QCoreApplication.translate("MainWindow", u"<<<", None))
        self.add_beams.setText(QCoreApplication.translate("MainWindow", u">>>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Seismic", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"A. Max 0.025", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"B. One-Half (+) M * (-) M", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"C. One-Fourth Mmax", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"D. Probable Shear", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Factored Gravity Load", None))
        self.max_rho.setText("")
        self.half_moment.setText("")
        self.fourth_moment.setText("")
        self.prob_shear.setText("")
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Seismic", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"A. Max 0.025", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"B. One-Half (+) M * (-) M", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"C. One-Fourth Mmax", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"D. Probable Shear", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Factored Gravity Load", None))
        self.checkBox_5.setText("")
        self.checkBox_6.setText("")
        self.checkBox_7.setText("")
        self.checkBox_8.setText("")
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Material Property", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"A. Main Bar Size", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Seismic", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"A. Max 0.025", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"B. One-Half (+) M * (-) M", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"C. One-Fourth Mmax", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"D. Probable Shear", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Factored Gravity Load", None))
        self.checkBox_13.setText("")
        self.checkBox_14.setText("")
        self.checkBox_15.setText("")
        self.checkBox_16.setText("")
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"28", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"32", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"28", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"32", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"B. Stirrups Bar  Size", None))
        self.extract_etabs_forces.setText(QCoreApplication.translate("MainWindow", u"Extract Etabs Design Forces", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Overwrites", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Design Forces", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Reinforcement Design", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Deflection Check", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Export ", None))
        self.btn_toggle_auto_tagger.setText(QCoreApplication.translate("MainWindow", u"ACTIVATE AUTO TAGGER", None))
        self.groupBox_2.setTitle("")
        self.lbl_input_tag.setText(QCoreApplication.translate("MainWindow", u"MEMBER TAG:", None))
        self.lbl_input_tag_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CONSOLE LOG", None))
        self.console_log.setPlainText("")
        self.console_log.setPlaceholderText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRaw_Data.setTitle(QCoreApplication.translate("MainWindow", u"Import Data", None))
        self.menuDesigner.setTitle(QCoreApplication.translate("MainWindow", u"Designer ", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export ", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

