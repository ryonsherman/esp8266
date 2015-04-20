# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/esp8266/gui/ui/ConsoleWifiWidget.ui'
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

class Ui_ConsoleWifiWidget(object):
    def setupUi(self, ConsoleWifiWidget):
        ConsoleWifiWidget.setObjectName(_fromUtf8("ConsoleWifiWidget"))
        ConsoleWifiWidget.resize(184, 258)
        self.gridLayout_2 = QtGui.QGridLayout(ConsoleWifiWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.wifi_buttons = QtGui.QGroupBox(ConsoleWifiWidget)
        self.wifi_buttons.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifi_buttons.sizePolicy().hasHeightForWidth())
        self.wifi_buttons.setSizePolicy(sizePolicy)
        self.wifi_buttons.setObjectName(_fromUtf8("wifi_buttons"))
        self.gridLayout = QtGui.QGridLayout(self.wifi_buttons)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.essid_input = QtGui.QLineEdit(self.wifi_buttons)
        self.essid_input.setObjectName(_fromUtf8("essid_input"))
        self.gridLayout.addWidget(self.essid_input, 1, 0, 1, 5)
        self.password_input = QtGui.QLineEdit(self.wifi_buttons)
        self.password_input.setEchoMode(QtGui.QLineEdit.Normal)
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.gridLayout.addWidget(self.password_input, 2, 0, 1, 5)
        self.button_console_bg = QtGui.QToolButton(self.wifi_buttons)
        self.button_console_bg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_console_bg.setObjectName(_fromUtf8("button_console_bg"))
        self.gridLayout.addWidget(self.button_console_bg, 0, 4, 1, 1)
        self.button_survey = QtGui.QPushButton(self.wifi_buttons)
        self.button_survey.setObjectName(_fromUtf8("button_survey"))
        self.gridLayout.addWidget(self.button_survey, 6, 0, 1, 2)
        self.button_set_ap = QtGui.QPushButton(self.wifi_buttons)
        self.button_set_ap.setObjectName(_fromUtf8("button_set_ap"))
        self.gridLayout.addWidget(self.button_set_ap, 5, 0, 1, 2)
        self.mode_select = QtGui.QComboBox(self.wifi_buttons)
        self.mode_select.setEnabled(True)
        self.mode_select.setObjectName(_fromUtf8("mode_select"))
        self.mode_select.addItem(_fromUtf8(""))
        self.mode_select.addItem(_fromUtf8(""))
        self.mode_select.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.mode_select, 0, 0, 1, 4)
        self.button_connect = QtGui.QPushButton(self.wifi_buttons)
        self.button_connect.setObjectName(_fromUtf8("button_connect"))
        self.gridLayout.addWidget(self.button_connect, 5, 2, 1, 3)
        self.button_get_ip = QtGui.QPushButton(self.wifi_buttons)
        self.button_get_ip.setObjectName(_fromUtf8("button_get_ip"))
        self.gridLayout.addWidget(self.button_get_ip, 6, 2, 1, 3)
        self.ap_input = QtGui.QWidget(self.wifi_buttons)
        self.ap_input.setObjectName(_fromUtf8("ap_input"))
        self.verticalLayout = QtGui.QVBoxLayout(self.ap_input)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ap_essid_input = QtGui.QLineEdit(self.ap_input)
        self.ap_essid_input.setObjectName(_fromUtf8("ap_essid_input"))
        self.verticalLayout.addWidget(self.ap_essid_input)
        self.ap_password_input = QtGui.QLineEdit(self.ap_input)
        self.ap_password_input.setEchoMode(QtGui.QLineEdit.Normal)
        self.ap_password_input.setObjectName(_fromUtf8("ap_password_input"))
        self.verticalLayout.addWidget(self.ap_password_input)
        self.gridLayout.addWidget(self.ap_input, 4, 0, 1, 5)
        self.gridLayout_2.addWidget(self.wifi_buttons, 0, 0, 1, 1)

        self.retranslateUi(ConsoleWifiWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleWifiWidget)
        ConsoleWifiWidget.setTabOrder(self.mode_select, self.essid_input)
        ConsoleWifiWidget.setTabOrder(self.essid_input, self.password_input)
        ConsoleWifiWidget.setTabOrder(self.password_input, self.ap_essid_input)
        ConsoleWifiWidget.setTabOrder(self.ap_essid_input, self.ap_password_input)
        ConsoleWifiWidget.setTabOrder(self.ap_password_input, self.button_set_ap)
        ConsoleWifiWidget.setTabOrder(self.button_set_ap, self.button_connect)
        ConsoleWifiWidget.setTabOrder(self.button_connect, self.button_survey)
        ConsoleWifiWidget.setTabOrder(self.button_survey, self.button_get_ip)

    def retranslateUi(self, ConsoleWifiWidget):
        ConsoleWifiWidget.setWindowTitle(_translate("ConsoleWifiWidget", "Form", None))
        self.wifi_buttons.setTitle(_translate("ConsoleWifiWidget", "Wireless", None))
        self.essid_input.setPlaceholderText(_translate("ConsoleWifiWidget", "ESSID", None))
        self.password_input.setPlaceholderText(_translate("ConsoleWifiWidget", "Password", None))
        self.button_console_bg.setText(_translate("ConsoleWifiWidget", "Info", None))
        self.button_survey.setText(_translate("ConsoleWifiWidget", "Survey", None))
        self.button_set_ap.setText(_translate("ConsoleWifiWidget", "Set AP", None))
        self.mode_select.setItemText(0, _translate("ConsoleWifiWidget", "STATION", None))
        self.mode_select.setItemText(1, _translate("ConsoleWifiWidget", "SOFTAP", None))
        self.mode_select.setItemText(2, _translate("ConsoleWifiWidget", "STATIONAP", None))
        self.button_connect.setText(_translate("ConsoleWifiWidget", "Connect", None))
        self.button_get_ip.setText(_translate("ConsoleWifiWidget", "Get IP", None))
        self.ap_essid_input.setPlaceholderText(_translate("ConsoleWifiWidget", "AP ESSID", None))
        self.ap_password_input.setPlaceholderText(_translate("ConsoleWifiWidget", "AP Password", None))

