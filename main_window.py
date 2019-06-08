# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Sat Jun  8 18:13:56 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 784)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ressources/icons_famfamfam/world_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#mpc_title_frame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(1, 56, 126, 255), stop:1 rgba(59, 134, 209, 255));\n"
"color: #9DC6F3\n"
"}\n"
"\n"
"#mpc_plugins {\n"
"    background-color: #494F56;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #494F56, stop:1 #31353A);\n"
"color: white;\n"
"}\n"
"\n"
"#mpc_plugins_list {\n"
"    background-color:  qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #494F56, stop:1 #31353A);\n"
"    border: none;\n"
"}\n"
"\n"
"#mpc_plugins_list::item {\n"
"padding: 10px;\n"
"color: white;\n"
"background-color: #31353A;\n"
"}\n"
"#mpc_plugins_list::item:hover {\n"
"background-color: #494F56\n"
"}\n"
"\n"
"#ps_frame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(1, 56, 126, 255), stop:1 rgba(59, 134, 209, 255));\n"
"color: #9DC6F3;}\n"
"\n"
"QLabel {\n"
"color: #9DC6F3;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_plugin_chooser = QtWidgets.QWidget()
        self.main_plugin_chooser.setStyleSheet("#main_plugin_chooser {\n"
"    background-color: rgb(206, 206, 206);\n"
"}")
        self.main_plugin_chooser.setObjectName("main_plugin_chooser")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_plugin_chooser)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mpc_plugins = QtWidgets.QFrame(self.main_plugin_chooser)
        self.mpc_plugins.setMaximumSize(QtCore.QSize(300, 16777215))
        self.mpc_plugins.setStyleSheet("")
        self.mpc_plugins.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mpc_plugins.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mpc_plugins.setObjectName("mpc_plugins")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mpc_plugins)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.mpc_plugins)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.mpc_plugins)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.mpc_plugins_list = QtWidgets.QListWidget(self.mpc_plugins)
        self.mpc_plugins_list.setAlternatingRowColors(True)
        self.mpc_plugins_list.setObjectName("mpc_plugins_list")
        self.verticalLayout.addWidget(self.mpc_plugins_list)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.mpc_plugins)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mpc_title_frame = QtWidgets.QFrame(self.main_plugin_chooser)
        self.mpc_title_frame.setMinimumSize(QtCore.QSize(300, 200))
        self.mpc_title_frame.setMaximumSize(QtCore.QSize(600, 400))
        self.mpc_title_frame.setStyleSheet("")
        self.mpc_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mpc_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mpc_title_frame.setObjectName("mpc_title_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mpc_title_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mpc_title_frame_title = QtWidgets.QLabel(self.mpc_title_frame)
        self.mpc_title_frame_title.setMaximumSize(QtCore.QSize(16777215, 30))
        self.mpc_title_frame_title.setObjectName("mpc_title_frame_title")
        self.gridLayout_3.addWidget(self.mpc_title_frame_title, 0, 0, 1, 1)
        self.mpc_btn_import = QtWidgets.QPushButton(self.mpc_title_frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/ressources/icons_famfamfam/zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpc_btn_import.setIcon(icon1)
        self.mpc_btn_import.setObjectName("mpc_btn_import")
        self.gridLayout_3.addWidget(self.mpc_btn_import, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(382, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 2, 0, 1, 2)
        self.mpc_title_frame_text = QtWidgets.QLabel(self.mpc_title_frame)
        self.mpc_title_frame_text.setObjectName("mpc_title_frame_text")
        self.gridLayout_3.addWidget(self.mpc_title_frame_text, 1, 0, 1, 3)
        self.gridLayout_2.addWidget(self.mpc_title_frame, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.stackedWidget.addWidget(self.main_plugin_chooser)
        self.plugin_satus = QtWidgets.QWidget()
        self.plugin_satus.setObjectName("plugin_satus")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.plugin_satus)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(20, 113, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 1, 0, 1, 1)
        self.ps_frame = QtWidgets.QFrame(self.plugin_satus)
        self.ps_frame.setMinimumSize(QtCore.QSize(500, 500))
        self.ps_frame.setStyleSheet("")
        self.ps_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ps_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ps_frame.setObjectName("ps_frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.ps_frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.ps_frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 2)
        self.ps_plugin_scrollArea = QtWidgets.QScrollArea(self.ps_frame)
        self.ps_plugin_scrollArea.setMinimumSize(QtCore.QSize(400, 0))
        self.ps_plugin_scrollArea.setWidgetResizable(True)
        self.ps_plugin_scrollArea.setObjectName("ps_plugin_scrollArea")
        self.ps_plugin_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.ps_plugin_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 528))
        self.ps_plugin_scrollAreaWidgetContents.setObjectName("ps_plugin_scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ps_plugin_scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ps_plugin_language_frame = QtWidgets.QFrame(self.ps_plugin_scrollAreaWidgetContents)
        self.ps_plugin_language_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ps_plugin_language_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ps_plugin_language_frame.setObjectName("ps_plugin_language_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ps_plugin_language_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3.addWidget(self.ps_plugin_language_frame)
        self.ps_plugin_scrollArea.setWidget(self.ps_plugin_scrollAreaWidgetContents)
        self.gridLayout_5.addWidget(self.ps_plugin_scrollArea, 0, 3, 5, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 176, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem8, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ps_add_language_btn = QtWidgets.QPushButton(self.ps_frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/ressources/icons_famfamfam/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ps_add_language_btn.setIcon(icon2)
        self.ps_add_language_btn.setObjectName("ps_add_language_btn")
        self.verticalLayout_2.addWidget(self.ps_add_language_btn)
        self.ps_delete_language_btn = QtWidgets.QPushButton(self.ps_frame)
        self.ps_delete_language_btn.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/ressources/icons_famfamfam/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ps_delete_language_btn.setIcon(icon3)
        self.ps_delete_language_btn.setObjectName("ps_delete_language_btn")
        self.verticalLayout_2.addWidget(self.ps_delete_language_btn)
        self.line_2 = QtWidgets.QFrame(self.ps_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.ps_export_language_btn = QtWidgets.QPushButton(self.ps_frame)
        self.ps_export_language_btn.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/ressources/icons_famfamfam/application_go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ps_export_language_btn.setIcon(icon4)
        self.ps_export_language_btn.setObjectName("ps_export_language_btn")
        self.verticalLayout_2.addWidget(self.ps_export_language_btn)
        self.ps_export_plugin_btn = QtWidgets.QPushButton(self.ps_frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/ressources/icons_famfamfam/page_white_zip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ps_export_plugin_btn.setIcon(icon5)
        self.ps_export_plugin_btn.setObjectName("ps_export_plugin_btn")
        self.verticalLayout_2.addWidget(self.ps_export_plugin_btn)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 2, 0, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 175, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem9, 3, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(192, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 3, 2, 1, 1)
        self.ps_btn_back = QtWidgets.QPushButton(self.ps_frame)
        self.ps_btn_back.setMaximumSize(QtCore.QSize(20, 20))
        self.ps_btn_back.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/ressources/icons_famfamfam/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ps_btn_back.setIcon(icon6)
        self.ps_btn_back.setObjectName("ps_btn_back")
        self.gridLayout_5.addWidget(self.ps_btn_back, 4, 0, 1, 1)
        self.ps_plugin_name = QtWidgets.QLabel(self.ps_frame)
        self.ps_plugin_name.setAlignment(QtCore.Qt.AlignCenter)
        self.ps_plugin_name.setObjectName("ps_plugin_name")
        self.gridLayout_5.addWidget(self.ps_plugin_name, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ps_delete_plugin_btn = QtWidgets.QPushButton(self.ps_frame)
        self.ps_delete_plugin_btn.setIcon(icon3)
        self.ps_delete_plugin_btn.setObjectName("ps_delete_plugin_btn")
        self.horizontalLayout_2.addWidget(self.ps_delete_plugin_btn)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 4, 1, 1, 2)
        self.gridLayout_4.addWidget(self.ps_frame, 1, 1, 1, 2)
        spacerItem12 = QtWidgets.QSpacerItem(217, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 1, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 112, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem13, 2, 2, 1, 1)
        self.stackedWidget.addWidget(self.plugin_satus)
        self.text_edition = QtWidgets.QWidget()
        self.text_edition.setObjectName("text_edition")
        self.stackedWidget.addWidget(self.text_edition)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Plugins</span></p></body></html>", None, -1))
        self.mpc_title_frame_title.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Projet à la con</p></body></html>", None, -1))
        self.mpc_btn_import.setText(QtWidgets.QApplication.translate("MainWindow", "import plugin", None, -1))
        self.mpc_title_frame_text.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor i</p><p>ncididunt ut labore et dolore magna aliqua. Ut enim ad minim ven</span></p><p>iam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla</p><p>pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p></body></html>", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Plugin:</span></p></body></html>", None, -1))
        self.ps_add_language_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Add Language", None, -1))
        self.ps_delete_language_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Delete Language", None, -1))
        self.ps_export_language_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Export Language", None, -1))
        self.ps_export_plugin_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Export Plugin", None, -1))
        self.ps_plugin_name.setText(QtWidgets.QApplication.translate("MainWindow", "[PLUGINNAME]", None, -1))
        self.ps_delete_plugin_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Delete plugin", None, -1))

import ressources_rc
