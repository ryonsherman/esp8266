# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/esp8266/gui/ui/ConsolePanelWidget.ui'
#
# Created: Mon Apr 20 13:02:40 2015
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

class Ui_ConsolePanelWidget(object):
    def setupUi(self, ConsolePanelWidget):
        ConsolePanelWidget.setObjectName(_fromUtf8("ConsolePanelWidget"))
        ConsolePanelWidget.resize(94, 16)
        self.verticalLayout = QtGui.QVBoxLayout(ConsolePanelWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 308, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(ConsolePanelWidget)
        QtCore.QMetaObject.connectSlotsByName(ConsolePanelWidget)

    def retranslateUi(self, ConsolePanelWidget):
        ConsolePanelWidget.setWindowTitle(_translate("ConsolePanelWidget", "Form", None))

