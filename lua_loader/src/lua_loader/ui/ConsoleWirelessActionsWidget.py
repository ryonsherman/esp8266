# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lua_loader/ui/ConsoleWirelessActionsWidget.ui'
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

class Ui_ConsoleWirelessActionsWidget(object):
    def setupUi(self, ConsoleWirelessActionsWidget):
        ConsoleWirelessActionsWidget.setObjectName(_fromUtf8("ConsoleWirelessActionsWidget"))
        ConsoleWirelessActionsWidget.resize(368, 147)
        self.gridLayout_2 = QtGui.QGridLayout(ConsoleWirelessActionsWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.wireless_view = QtGui.QGroupBox(ConsoleWirelessActionsWidget)
        self.wireless_view.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wireless_view.sizePolicy().hasHeightForWidth())
        self.wireless_view.setSizePolicy(sizePolicy)
        self.wireless_view.setObjectName(_fromUtf8("wireless_view"))
        self.gridLayout = QtGui.QGridLayout(self.wireless_view)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.essid_input = QtGui.QLineEdit(self.wireless_view)
        self.essid_input.setObjectName(_fromUtf8("essid_input"))
        self.gridLayout.addWidget(self.essid_input, 0, 0, 1, 2)
        self.button_get_ip = QtGui.QPushButton(self.wireless_view)
        self.button_get_ip.setObjectName(_fromUtf8("button_get_ip"))
        self.gridLayout.addWidget(self.button_get_ip, 2, 1, 1, 1)
        self.button_survey = QtGui.QPushButton(self.wireless_view)
        self.button_survey.setObjectName(_fromUtf8("button_survey"))
        self.gridLayout.addWidget(self.button_survey, 1, 2, 1, 1)
        self.mode_select = QtGui.QComboBox(self.wireless_view)
        self.mode_select.setEnabled(True)
        self.mode_select.setObjectName(_fromUtf8("mode_select"))
        self.mode_select.addItem(_fromUtf8(""))
        self.mode_select.addItem(_fromUtf8(""))
        self.mode_select.addItem(_fromUtf8(""))
        self.mode_select.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.mode_select, 2, 0, 1, 1)
        self.button_connect = QtGui.QPushButton(self.wireless_view)
        self.button_connect.setObjectName(_fromUtf8("button_connect"))
        self.gridLayout.addWidget(self.button_connect, 2, 2, 1, 1)
        self.password_entry = QtGui.QLineEdit(self.wireless_view)
        self.password_entry.setEchoMode(QtGui.QLineEdit.Normal)
        self.password_entry.setObjectName(_fromUtf8("password_entry"))
        self.gridLayout.addWidget(self.password_entry, 1, 0, 1, 2)
        self.button_set_ap = QtGui.QPushButton(self.wireless_view)
        self.button_set_ap.setObjectName(_fromUtf8("button_set_ap"))
        self.gridLayout.addWidget(self.button_set_ap, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.wireless_view, 0, 0, 1, 1)

        self.retranslateUi(ConsoleWirelessActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleWirelessActionsWidget)

    def retranslateUi(self, ConsoleWirelessActionsWidget):
        ConsoleWirelessActionsWidget.setWindowTitle(_translate("ConsoleWirelessActionsWidget", "Form", None))
        self.wireless_view.setTitle(_translate("ConsoleWirelessActionsWidget", "Wireless", None))
        self.essid_input.setPlaceholderText(_translate("ConsoleWirelessActionsWidget", "ESSID", None))
        self.button_get_ip.setText(_translate("ConsoleWirelessActionsWidget", "Get IP", None))
        self.button_survey.setText(_translate("ConsoleWirelessActionsWidget", "Survey", None))
        self.mode_select.setItemText(0, _translate("ConsoleWirelessActionsWidget", "Mode", None))
        self.mode_select.setItemText(1, _translate("ConsoleWirelessActionsWidget", "STATION", None))
        self.mode_select.setItemText(2, _translate("ConsoleWirelessActionsWidget", "SOFTAP", None))
        self.mode_select.setItemText(3, _translate("ConsoleWirelessActionsWidget", "STATIONAP", None))
        self.button_connect.setText(_translate("ConsoleWirelessActionsWidget", "Connect", None))
        self.password_entry.setPlaceholderText(_translate("ConsoleWirelessActionsWidget", "Password", None))
        self.button_set_ap.setText(_translate("ConsoleWirelessActionsWidget", "Set AP", None))

