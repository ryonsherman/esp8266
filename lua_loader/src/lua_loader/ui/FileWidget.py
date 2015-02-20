# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lua_loader/ui/FileWidget.ui'
#
# Created: Thu Feb 19 22:18:11 2015
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

class Ui_FileWidget(object):
    def setupUi(self, FileWidget):
        FileWidget.setObjectName(_fromUtf8("FileWidget"))
        FileWidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(FileWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.input = QtGui.QPlainTextEdit(FileWidget)
        self.input.setObjectName(_fromUtf8("input"))
        self.gridLayout.addWidget(self.input, 0, 0, 1, 4)
        self.button_close = QtGui.QPushButton(FileWidget)
        self.button_close.setEnabled(False)
        self.button_close.setObjectName(_fromUtf8("button_close"))
        self.gridLayout.addWidget(self.button_close, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(197, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.button_save = QtGui.QPushButton(FileWidget)
        self.button_save.setEnabled(False)
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.gridLayout.addWidget(self.button_save, 1, 3, 1, 1)
        self.button_save_2 = QtGui.QPushButton(FileWidget)
        self.button_save_2.setEnabled(False)
        self.button_save_2.setObjectName(_fromUtf8("button_save_2"))
        self.gridLayout.addWidget(self.button_save_2, 1, 2, 1, 1)

        self.retranslateUi(FileWidget)
        QtCore.QMetaObject.connectSlotsByName(FileWidget)

    def retranslateUi(self, FileWidget):
        FileWidget.setWindowTitle(_translate("FileWidget", "Form", None))
        self.button_close.setText(_translate("FileWidget", "Close", None))
        self.button_close.setShortcut(_translate("FileWidget", "Ctrl+W", None))
        self.button_save.setText(_translate("FileWidget", "Save", None))
        self.button_save.setShortcut(_translate("FileWidget", "Ctrl+S", None))
        self.button_save_2.setText(_translate("FileWidget", "Upload", None))
        self.button_save_2.setShortcut(_translate("FileWidget", "Ctrl+S", None))

