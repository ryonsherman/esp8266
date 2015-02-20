# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lua_loader/ui/ConsoleActionsWidget.ui'
#
# Created: Thu Feb 19 22:18:10 2015
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
        ConsoleActionsWidget.resize(202, 108)
        self.gridLayout = QtGui.QGridLayout(ConsoleActionsWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.actions_view = QtGui.QGroupBox(ConsoleActionsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actions_view.sizePolicy().hasHeightForWidth())
        self.actions_view.setSizePolicy(sizePolicy)
        self.actions_view.setObjectName(_fromUtf8("actions_view"))
        self.gridLayout_3 = QtGui.QGridLayout(self.actions_view)
        self.gridLayout_3.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.button_connect = QtGui.QPushButton(self.actions_view)
        self.button_connect.setObjectName(_fromUtf8("button_connect"))
        self.gridLayout_3.addWidget(self.button_connect, 0, 0, 1, 1)
        self.button_heap = QtGui.QPushButton(self.actions_view)
        self.button_heap.setEnabled(True)
        self.button_heap.setObjectName(_fromUtf8("button_heap"))
        self.gridLayout_3.addWidget(self.button_heap, 1, 2, 1, 1)
        self.button_info = QtGui.QPushButton(self.actions_view)
        self.button_info.setEnabled(True)
        self.button_info.setObjectName(_fromUtf8("button_info"))
        self.gridLayout_3.addWidget(self.button_info, 1, 0, 1, 1)
        self.button_restart = QtGui.QPushButton(self.actions_view)
        self.button_restart.setEnabled(True)
        self.button_restart.setObjectName(_fromUtf8("button_restart"))
        self.gridLayout_3.addWidget(self.button_restart, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.actions_view, 0, 0, 1, 1)

        self.retranslateUi(ConsoleActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleActionsWidget)

    def retranslateUi(self, ConsoleActionsWidget):
        ConsoleActionsWidget.setWindowTitle(_translate("ConsoleActionsWidget", "Form", None))
        self.actions_view.setTitle(_translate("ConsoleActionsWidget", "Actions", None))
        self.button_connect.setText(_translate("ConsoleActionsWidget", "Connect", None))
        self.button_heap.setText(_translate("ConsoleActionsWidget", "Heap", None))
        self.button_info.setText(_translate("ConsoleActionsWidget", "Info", None))
        self.button_restart.setText(_translate("ConsoleActionsWidget", "Restart", None))
        self.button_restart.setShortcut(_translate("ConsoleActionsWidget", "Ctrl+R", None))

