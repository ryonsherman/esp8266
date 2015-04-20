# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/esp8266/gui/ui/MainWindow.ui'
#
# Created: Mon Apr 20 13:02:41 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1080, 720)
        self.main_widget = QtGui.QWidget(MainWindow)
        self.main_widget.setObjectName(_fromUtf8("main_widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.main_widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabs = QtGui.QTabWidget(self.main_widget)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.horizontalLayout.addWidget(self.tabs)
        MainWindow.setCentralWidget(self.main_widget)
        self.menu = QtGui.QMenuBar(MainWindow)
        self.menu.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_view = QtGui.QMenu(self.menu)
        self.menu_view.setEnabled(True)
        self.menu_view.setObjectName(_fromUtf8("menu_view"))
        self.menu_file = QtGui.QMenu(self.menu)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_settings = QtGui.QMenu(self.menu)
        self.menu_settings.setObjectName(_fromUtf8("menu_settings"))
        MainWindow.setMenuBar(self.menu)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menu_view_log = QtGui.QAction(MainWindow)
        self.menu_view_log.setCheckable(True)
        self.menu_view_log.setObjectName(_fromUtf8("menu_view_log"))
        self.menu_prefs = QtGui.QAction(MainWindow)
        self.menu_prefs.setObjectName(_fromUtf8("menu_prefs"))
        self.menu_view_actions = QtGui.QAction(MainWindow)
        self.menu_view_actions.setCheckable(True)
        self.menu_view_actions.setChecked(True)
        self.menu_view_actions.setObjectName(_fromUtf8("menu_view_actions"))
        self.menu_view_files = QtGui.QAction(MainWindow)
        self.menu_view_files.setCheckable(True)
        self.menu_view_files.setChecked(True)
        self.menu_view_files.setEnabled(True)
        self.menu_view_files.setObjectName(_fromUtf8("menu_view_files"))
        self.menu_open_file = QtGui.QAction(MainWindow)
        self.menu_open_file.setObjectName(_fromUtf8("menu_open_file"))
        self.menu_open_path = QtGui.QAction(MainWindow)
        self.menu_open_path.setObjectName(_fromUtf8("menu_open_path"))
        self.menu_prefs1 = QtGui.QAction(MainWindow)
        self.menu_prefs1.setObjectName(_fromUtf8("menu_prefs1"))
        self.menu_view.addAction(self.menu_view_actions)
        self.menu_view.addAction(self.menu_view_files)
        self.menu_view.addAction(self.menu_view_log)
        self.menu_file.addAction(self.menu_open_file)
        self.menu_file.addAction(self.menu_open_path)
        self.menu_settings.addAction(self.menu_prefs)
        self.menu.addAction(self.menu_file.menuAction())
        self.menu.addAction(self.menu_settings.menuAction())
        self.menu.addAction(self.menu_view.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ESP8266 NodeMCU GUI", None))
        self.menu_view.setTitle(_translate("MainWindow", "&View", None))
        self.menu_file.setTitle(_translate("MainWindow", "&File", None))
        self.menu_settings.setTitle(_translate("MainWindow", "&Settings", None))
        self.menu_view_log.setText(_translate("MainWindow", "&Log", None))
        self.menu_prefs.setText(_translate("MainWindow", "&Preferences", None))
        self.menu_prefs.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.menu_view_actions.setText(_translate("MainWindow", "&Actions", None))
        self.menu_view_files.setText(_translate("MainWindow", "&Files", None))
        self.menu_open_file.setText(_translate("MainWindow", "&Open File", None))
        self.menu_open_file.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.menu_open_path.setText(_translate("MainWindow", "Open &Path", None))
        self.menu_open_path.setShortcut(_translate("MainWindow", "Ctrl+Shift+O", None))
        self.menu_prefs1.setText(_translate("MainWindow", "&Preferences", None))

