# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/esp8266/gui/ui/ConsoleActionsWidget.ui'
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

class Ui_ConsoleActionsWidget(object):
    def setupUi(self, ConsoleActionsWidget):
        ConsoleActionsWidget.setObjectName(_fromUtf8("ConsoleActionsWidget"))
        ConsoleActionsWidget.resize(184, 90)
        self.gridLayout = QtGui.QGridLayout(ConsoleActionsWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.action_buttons = QtGui.QGroupBox(ConsoleActionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_buttons.sizePolicy().hasHeightForWidth())
        self.action_buttons.setSizePolicy(sizePolicy)
        self.action_buttons.setObjectName(_fromUtf8("action_buttons"))
        self.gridLayout_3 = QtGui.QGridLayout(self.action_buttons)
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.button_connect = QtGui.QPushButton(self.action_buttons)
        self.button_connect.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_connect.setObjectName(_fromUtf8("button_connect"))
        self.gridLayout_3.addWidget(self.button_connect, 0, 0, 1, 1)
        self.button_heap = QtGui.QPushButton(self.action_buttons)
        self.button_heap.setEnabled(True)
        self.button_heap.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_heap.setObjectName(_fromUtf8("button_heap"))
        self.gridLayout_3.addWidget(self.button_heap, 1, 2, 1, 1)
        self.button_info = QtGui.QPushButton(self.action_buttons)
        self.button_info.setEnabled(True)
        self.button_info.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_info.setObjectName(_fromUtf8("button_info"))
        self.gridLayout_3.addWidget(self.button_info, 1, 0, 1, 1)
        self.button_restart = QtGui.QPushButton(self.action_buttons)
        self.button_restart.setEnabled(True)
        self.button_restart.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_restart.setObjectName(_fromUtf8("button_restart"))
        self.gridLayout_3.addWidget(self.button_restart, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.action_buttons, 0, 0, 1, 1)

        self.retranslateUi(ConsoleActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleActionsWidget)

    def retranslateUi(self, ConsoleActionsWidget):
        ConsoleActionsWidget.setWindowTitle(_translate("ConsoleActionsWidget", "Form", None))
        self.action_buttons.setTitle(_translate("ConsoleActionsWidget", "Actions", None))
        self.button_connect.setText(_translate("ConsoleActionsWidget", "Connect", None))
        self.button_heap.setText(_translate("ConsoleActionsWidget", "Heap", None))
        self.button_info.setText(_translate("ConsoleActionsWidget", "Info", None))
        self.button_restart.setText(_translate("ConsoleActionsWidget", "Restart", None))
        self.button_restart.setShortcut(_translate("ConsoleActionsWidget", "Ctrl+R", None))

