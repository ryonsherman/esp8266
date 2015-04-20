# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/esp8266/gui/ui/ConsoleGPIOWidget.ui'
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

class Ui_ConsoleGPIOWidget(object):
    def setupUi(self, ConsoleGPIOWidget):
        ConsoleGPIOWidget.setObjectName(_fromUtf8("ConsoleGPIOWidget"))
        ConsoleGPIOWidget.resize(184, 192)
        self.gridLayout = QtGui.QGridLayout(ConsoleGPIOWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gpio_buttons = QtGui.QGroupBox(ConsoleGPIOWidget)
        self.gpio_buttons.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpio_buttons.sizePolicy().hasHeightForWidth())
        self.gpio_buttons.setSizePolicy(sizePolicy)
        self.gpio_buttons.setObjectName(_fromUtf8("gpio_buttons"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gpio_buttons)
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.button_high = QtGui.QPushButton(self.gpio_buttons)
        self.button_high.setObjectName(_fromUtf8("button_high"))
        self.gridLayout_2.addWidget(self.button_high, 5, 3, 1, 1)
        self.pu_mode_select = QtGui.QComboBox(self.gpio_buttons)
        self.pu_mode_select.setObjectName(_fromUtf8("pu_mode_select"))
        self.pu_mode_select.addItem(_fromUtf8(""))
        self.pu_mode_select.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.pu_mode_select, 3, 2, 1, 2)
        self.button_low = QtGui.QPushButton(self.gpio_buttons)
        self.button_low.setObjectName(_fromUtf8("button_low"))
        self.gridLayout_2.addWidget(self.button_low, 5, 2, 1, 1)
        self.button_read = QtGui.QPushButton(self.gpio_buttons)
        self.button_read.setObjectName(_fromUtf8("button_read"))
        self.gridLayout_2.addWidget(self.button_read, 4, 3, 1, 1)
        self.button_set = QtGui.QPushButton(self.gpio_buttons)
        self.button_set.setObjectName(_fromUtf8("button_set"))
        self.gridLayout_2.addWidget(self.button_set, 4, 2, 1, 1)
        self.mode_select = QtGui.QComboBox(self.gpio_buttons)
        self.mode_select.setObjectName(_fromUtf8("mode_select"))
        self.mode_select.addItem(_fromUtf8(""))
        self.mode_select.addItem(_fromUtf8(""))
        self.mode_select.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.mode_select, 2, 2, 1, 2)
        self.gpio_select = QtGui.QComboBox(self.gpio_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpio_select.sizePolicy().hasHeightForWidth())
        self.gpio_select.setSizePolicy(sizePolicy)
        self.gpio_select.setObjectName(_fromUtf8("gpio_select"))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gpio_select.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.gpio_select, 0, 2, 1, 2)
        self.gridLayout.addWidget(self.gpio_buttons, 0, 0, 1, 1)

        self.retranslateUi(ConsoleGPIOWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleGPIOWidget)
        ConsoleGPIOWidget.setTabOrder(self.gpio_select, self.mode_select)
        ConsoleGPIOWidget.setTabOrder(self.mode_select, self.pu_mode_select)
        ConsoleGPIOWidget.setTabOrder(self.pu_mode_select, self.button_set)
        ConsoleGPIOWidget.setTabOrder(self.button_set, self.button_read)
        ConsoleGPIOWidget.setTabOrder(self.button_read, self.button_low)
        ConsoleGPIOWidget.setTabOrder(self.button_low, self.button_high)

    def retranslateUi(self, ConsoleGPIOWidget):
        ConsoleGPIOWidget.setWindowTitle(_translate("ConsoleGPIOWidget", "Form", None))
        self.gpio_buttons.setTitle(_translate("ConsoleGPIOWidget", "GPIO", None))
        self.button_high.setText(_translate("ConsoleGPIOWidget", "1", None))
        self.pu_mode_select.setItemText(0, _translate("ConsoleGPIOWidget", "FLOAT", None))
        self.pu_mode_select.setItemText(1, _translate("ConsoleGPIOWidget", "PULLUP", None))
        self.button_low.setText(_translate("ConsoleGPIOWidget", "0", None))
        self.button_read.setText(_translate("ConsoleGPIOWidget", "Read", None))
        self.button_set.setText(_translate("ConsoleGPIOWidget", "Set", None))
        self.mode_select.setItemText(0, _translate("ConsoleGPIOWidget", "OUTPUT", None))
        self.mode_select.setItemText(1, _translate("ConsoleGPIOWidget", "INPUT", None))
        self.mode_select.setItemText(2, _translate("ConsoleGPIOWidget", "INT", None))
        self.gpio_select.setItemText(0, _translate("ConsoleGPIOWidget", "0: GPIO16", None))
        self.gpio_select.setItemText(1, _translate("ConsoleGPIOWidget", "1: GPIO5", None))
        self.gpio_select.setItemText(2, _translate("ConsoleGPIOWidget", "2: GPIO4", None))
        self.gpio_select.setItemText(3, _translate("ConsoleGPIOWidget", "3: GPIO0", None))
        self.gpio_select.setItemText(4, _translate("ConsoleGPIOWidget", "4: GPIO2", None))
        self.gpio_select.setItemText(5, _translate("ConsoleGPIOWidget", "5: GPIO14", None))
        self.gpio_select.setItemText(6, _translate("ConsoleGPIOWidget", "6: GPIO12", None))
        self.gpio_select.setItemText(7, _translate("ConsoleGPIOWidget", "7: GPIO13", None))
        self.gpio_select.setItemText(8, _translate("ConsoleGPIOWidget", "8: GPIO15", None))
        self.gpio_select.setItemText(9, _translate("ConsoleGPIOWidget", "9: GPIO3", None))
        self.gpio_select.setItemText(10, _translate("ConsoleGPIOWidget", "10: GPIO1", None))
        self.gpio_select.setItemText(11, _translate("ConsoleGPIOWidget", "11: GPIO9", None))
        self.gpio_select.setItemText(12, _translate("ConsoleGPIOWidget", "12: GPIO10", None))

