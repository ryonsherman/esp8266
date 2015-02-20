# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lua_loader/ui/ConsoleWidget.ui'
#
# Created: Thu Feb 19 20:13:54 2015
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
        ConsoleWidget.resize(684, 443)
        self.gridLayout_4 = QtGui.QGridLayout(ConsoleWidget)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.output = QtGui.QPlainTextEdit(ConsoleWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setStyleSheet(_fromUtf8("QPlainTextEdit {\n"
"color: #CFD0C2;\n"
"background-color: #48483E;\n"
"}\n"
"QScrollBar {\n"
"background: none\n"
"}"))
        self.output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.output.setReadOnly(True)
        self.output.setObjectName(_fromUtf8("output"))
        self.gridLayout_4.addWidget(self.output, 0, 0, 1, 1)
        self.action_view = QtGui.QWidget(ConsoleWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_view.sizePolicy().hasHeightForWidth())
        self.action_view.setSizePolicy(sizePolicy)
        self.action_view.setObjectName(_fromUtf8("action_view"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.action_view)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_4.addWidget(self.action_view, 0, 1, 1, 1)
        self.input_view = QtGui.QHBoxLayout()
        self.input_view.setObjectName(_fromUtf8("input_view"))
        self.input = QtGui.QLineEdit(ConsoleWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setObjectName(_fromUtf8("input"))
        self.input_view.addWidget(self.input)
        self.button_send = QtGui.QPushButton(ConsoleWidget)
        self.button_send.setObjectName(_fromUtf8("button_send"))
        self.input_view.addWidget(self.button_send)
        self.button_clear = QtGui.QPushButton(ConsoleWidget)
        self.button_clear.setObjectName(_fromUtf8("button_clear"))
        self.input_view.addWidget(self.button_clear)
        self.gridLayout_4.addLayout(self.input_view, 1, 0, 1, 1)

        self.retranslateUi(ConsoleWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleWidget)

    def retranslateUi(self, ConsoleWidget):
        ConsoleWidget.setWindowTitle(_translate("ConsoleWidget", "Form", None))
        self.button_send.setText(_translate("ConsoleWidget", "Send", None))
        self.button_clear.setText(_translate("ConsoleWidget", "Clear", None))
        self.button_clear.setShortcut(_translate("ConsoleWidget", "Ctrl+L", None))

