# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/node_gui/ui/widget/ConsoleGPIOWidget.ui'
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
        self.pushButton_2 = QtGui.QPushButton(self.gpio_buttons)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 5, 3, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.gpio_buttons)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox_2, 3, 2, 1, 2)
        self.pushButton = QtGui.QPushButton(self.gpio_buttons)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 5, 2, 1, 1)
        self.button_gpio_read = QtGui.QPushButton(self.gpio_buttons)
        self.button_gpio_read.setObjectName(_fromUtf8("button_gpio_read"))
        self.gridLayout_2.addWidget(self.button_gpio_read, 4, 3, 1, 1)
        self.button_gpio_read_2 = QtGui.QPushButton(self.gpio_buttons)
        self.button_gpio_read_2.setObjectName(_fromUtf8("button_gpio_read_2"))
        self.gridLayout_2.addWidget(self.button_gpio_read_2, 4, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(self.gpio_buttons)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.comboBox, 2, 2, 1, 2)
        self.select_gpio = QtGui.QComboBox(self.gpio_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_gpio.sizePolicy().hasHeightForWidth())
        self.select_gpio.setSizePolicy(sizePolicy)
        self.select_gpio.setObjectName(_fromUtf8("select_gpio"))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.select_gpio.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.select_gpio, 0, 2, 1, 2)
        self.gridLayout.addWidget(self.gpio_buttons, 0, 0, 1, 1)

        self.retranslateUi(ConsoleGPIOWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsoleGPIOWidget)

    def retranslateUi(self, ConsoleGPIOWidget):
        ConsoleGPIOWidget.setWindowTitle(_translate("ConsoleGPIOWidget", "Form", None))
        self.gpio_buttons.setTitle(_translate("ConsoleGPIOWidget", "GPIO", None))
        self.pushButton_2.setText(_translate("ConsoleGPIOWidget", "1", None))
        self.comboBox_2.setItemText(0, _translate("ConsoleGPIOWidget", "FLOAT", None))
        self.comboBox_2.setItemText(1, _translate("ConsoleGPIOWidget", "PULLUP", None))
        self.pushButton.setText(_translate("ConsoleGPIOWidget", "0", None))
        self.button_gpio_read.setText(_translate("ConsoleGPIOWidget", "Read", None))
        self.button_gpio_read_2.setText(_translate("ConsoleGPIOWidget", "Set", None))
        self.comboBox.setItemText(0, _translate("ConsoleGPIOWidget", "OUTPUT", None))
        self.comboBox.setItemText(1, _translate("ConsoleGPIOWidget", "INPUT", None))
        self.comboBox.setItemText(2, _translate("ConsoleGPIOWidget", "INT", None))
        self.select_gpio.setItemText(0, _translate("ConsoleGPIOWidget", "0: GPIO16", None))
        self.select_gpio.setItemText(1, _translate("ConsoleGPIOWidget", "1: GPIO5", None))
        self.select_gpio.setItemText(2, _translate("ConsoleGPIOWidget", "2: GPIO4", None))
        self.select_gpio.setItemText(3, _translate("ConsoleGPIOWidget", "3: GPIO0", None))
        self.select_gpio.setItemText(4, _translate("ConsoleGPIOWidget", "4: GPIO2", None))
        self.select_gpio.setItemText(5, _translate("ConsoleGPIOWidget", "5: GPIO14", None))
        self.select_gpio.setItemText(6, _translate("ConsoleGPIOWidget", "6: GPIO12", None))
        self.select_gpio.setItemText(7, _translate("ConsoleGPIOWidget", "7: GPIO13", None))
        self.select_gpio.setItemText(8, _translate("ConsoleGPIOWidget", "8: GPIO15", None))
        self.select_gpio.setItemText(9, _translate("ConsoleGPIOWidget", "9: GPIO3", None))
        self.select_gpio.setItemText(10, _translate("ConsoleGPIOWidget", "10: GPIO1", None))
        self.select_gpio.setItemText(11, _translate("ConsoleGPIOWidget", "11: GPIO9", None))
        self.select_gpio.setItemText(12, _translate("ConsoleGPIOWidget", "12: GPIO10", None))

