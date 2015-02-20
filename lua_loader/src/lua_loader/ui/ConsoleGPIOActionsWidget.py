# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lua_loader/ui/ConsoleGPIOActionsWidget.ui'
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

class Ui_ConsoleGPIOActionsWidget(object):
    def setupUi(self, ConsoleGPIOActionsWidget):
        ConsoleGPIOActionsWidget.setObjectName(_fromUtf8("ConsoleGPIOActionsWidget"))
        ConsoleGPIOActionsWidget.resize(216, 81)
        self.gridLayout = QtGui.QGridLayout(ConsoleGPIOActionsWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gpio_view = QtGui.QGroupBox(ConsoleGPIOActionsWidget)
        self.gpio_view.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpio_view.sizePolicy().hasHeightForWidth())
        self.gpio_view.setSizePolicy(sizePolicy)
        self.gpio_view.setObjectName(_fromUtf8("gpio_view"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gpio_view)
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gpio_pin_select = QtGui.QComboBox(self.gpio_view)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gpio_pin_select.sizePolicy().hasHeightForWidth())
        self.gpio_pin_select.setSizePolicy(sizePolicy)
        self.gpio_pin_select.setObjectName(_fromUtf8("gpio_pin_select"))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gpio_pin_select.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.gpio_pin_select, 0, 0, 1, 1)
        self.gpio_button_read = QtGui.QPushButton(self.gpio_view)
        self.gpio_button_read.setObjectName(_fromUtf8("gpio_button_read"))
        self.gridLayout_2.addWidget(self.gpio_button_read, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.gpio_view, 0, 0, 1, 1)

        self.retranslateUi(ConsoleGPIOActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleGPIOActionsWidget)

    def retranslateUi(self, ConsoleGPIOActionsWidget):
        ConsoleGPIOActionsWidget.setWindowTitle(_translate("ConsoleGPIOActionsWidget", "Form", None))
        self.gpio_view.setTitle(_translate("ConsoleGPIOActionsWidget", "GPIO", None))
        self.gpio_pin_select.setItemText(0, _translate("ConsoleGPIOActionsWidget", "0: GPIO16", None))
        self.gpio_pin_select.setItemText(1, _translate("ConsoleGPIOActionsWidget", "1: GPIO5", None))
        self.gpio_pin_select.setItemText(2, _translate("ConsoleGPIOActionsWidget", "2: GPIO4", None))
        self.gpio_pin_select.setItemText(3, _translate("ConsoleGPIOActionsWidget", "3: GPIO0", None))
        self.gpio_pin_select.setItemText(4, _translate("ConsoleGPIOActionsWidget", "4: GPIO2", None))
        self.gpio_pin_select.setItemText(5, _translate("ConsoleGPIOActionsWidget", "5: GPIO14", None))
        self.gpio_pin_select.setItemText(6, _translate("ConsoleGPIOActionsWidget", "6: GPIO12", None))
        self.gpio_pin_select.setItemText(7, _translate("ConsoleGPIOActionsWidget", "7: GPIO13", None))
        self.gpio_pin_select.setItemText(8, _translate("ConsoleGPIOActionsWidget", "8: GPIO15", None))
        self.gpio_pin_select.setItemText(9, _translate("ConsoleGPIOActionsWidget", "9: GPIO3", None))
        self.gpio_pin_select.setItemText(10, _translate("ConsoleGPIOActionsWidget", "10: GPIO1", None))
        self.gpio_pin_select.setItemText(11, _translate("ConsoleGPIOActionsWidget", "11: GPIO9", None))
        self.gpio_pin_select.setItemText(12, _translate("ConsoleGPIOActionsWidget", "12: GPIO10", None))
        self.gpio_button_read.setText(_translate("ConsoleGPIOActionsWidget", "Read", None))

