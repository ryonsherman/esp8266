# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lua_loader/ui/LogWidget.ui'
#
# Created: Thu Feb 19 20:13:55 2015
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

class Ui_LogWidget(object):
    def setupUi(self, LogWidget):
        LogWidget.setObjectName(_fromUtf8("LogWidget"))
        LogWidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(LogWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.output = QtGui.QPlainTextEdit(LogWidget)
        self.output.setReadOnly(True)
        self.output.setObjectName(_fromUtf8("output"))
        self.gridLayout.addWidget(self.output, 0, 0, 1, 3)
        self.button_close = QtGui.QPushButton(LogWidget)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.gridLayout.addWidget(self.button_close, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(197, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.button_save = QtGui.QPushButton(LogWidget)
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.gridLayout.addWidget(self.button_save, 1, 2, 1, 1)

        self.retranslateUi(LogWidget)
        QtCore.QMetaObject.connectSlotsByName(LogWidget)

    def retranslateUi(self, LogWidget):
        LogWidget.setWindowTitle(_translate("LogWidget", "Form", None))
        self.button_close.setText(_translate("LogWidget", "Close", None))
        self.button_close.setShortcut(_translate("LogWidget", "Ctrl+W", None))
        self.button_save.setText(_translate("LogWidget", "Save", None))
        self.button_save.setShortcut(_translate("LogWidget", "Ctrl+S", None))

