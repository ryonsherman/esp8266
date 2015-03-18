# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/node_gui/ui/widget/ConsoleWidget.ui'
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

class Ui_ConsoleWidget(object):
    def setupUi(self, ConsoleWidget):
        ConsoleWidget.setObjectName(_fromUtf8("ConsoleWidget"))
        ConsoleWidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(ConsoleWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.input = QtGui.QLineEdit(ConsoleWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input.setObjectName(_fromUtf8("input"))
        self.gridLayout.addWidget(self.input, 2, 0, 1, 1)
        self.button_send = QtGui.QPushButton(ConsoleWidget)
        self.button_send.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_send.setObjectName(_fromUtf8("button_send"))
        self.gridLayout.addWidget(self.button_send, 2, 1, 1, 1)
        self.button_clear = QtGui.QPushButton(ConsoleWidget)
        self.button_clear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_clear.setObjectName(_fromUtf8("button_clear"))
        self.gridLayout.addWidget(self.button_clear, 2, 2, 1, 1)
        self.view = QtGui.QHBoxLayout()
        self.view.setObjectName(_fromUtf8("view"))
        self.output = QtGui.QPlainTextEdit(ConsoleWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.output.setReadOnly(True)
        self.output.setObjectName(_fromUtf8("output"))
        self.view.addWidget(self.output)
        self.gridLayout.addLayout(self.view, 0, 0, 1, 3)

        self.retranslateUi(ConsoleWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleWidget)

    def retranslateUi(self, ConsoleWidget):
        ConsoleWidget.setWindowTitle(_translate("ConsoleWidget", "Form", None))
        self.button_send.setText(_translate("ConsoleWidget", "Send", None))
        self.button_clear.setText(_translate("ConsoleWidget", "Clear", None))
        self.button_clear.setShortcut(_translate("ConsoleWidget", "Ctrl+L", None))

