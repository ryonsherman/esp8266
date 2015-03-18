# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/node_gui/ui/widget/MainTabsWidget.ui'
#
# Created: Wed Mar 18 11:37:23 2015
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

class Ui_MainTabsWidget(object):
    def setupUi(self, MainTabsWidget):
        MainTabsWidget.setObjectName(_fromUtf8("MainTabsWidget"))
        MainTabsWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(MainTabsWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabs = QtGui.QTabWidget(MainTabsWidget)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.verticalLayout.addWidget(self.tabs)

        self.retranslateUi(MainTabsWidget)
        QtCore.QMetaObject.connectSlotsByName(MainTabsWidget)

    def retranslateUi(self, MainTabsWidget):
        MainTabsWidget.setWindowTitle(_translate("MainTabsWidget", "Form", None))

