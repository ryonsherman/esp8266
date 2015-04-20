# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/esp8266/gui/ui/PreferencesDialog.ui'
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

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName(_fromUtf8("PreferencesDialog"))
        PreferencesDialog.resize(308, 274)
        PreferencesDialog.setSizeGripEnabled(False)
        PreferencesDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(PreferencesDialog)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabs = QtGui.QTabWidget(PreferencesDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab_serial = QtGui.QWidget()
        self.tab_serial.setObjectName(_fromUtf8("tab_serial"))
        self.tabs.addTab(self.tab_serial, _fromUtf8(""))
        self.tab_interface = QtGui.QWidget()
        self.tab_interface.setObjectName(_fromUtf8("tab_interface"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_interface)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.console_layout = QtGui.QGroupBox(self.tab_interface)
        self.console_layout.setObjectName(_fromUtf8("console_layout"))
        self.gridLayout_3 = QtGui.QGridLayout(self.console_layout)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.button_console_fg = QtGui.QToolButton(self.console_layout)
        self.button_console_fg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_console_fg.setObjectName(_fromUtf8("button_console_fg"))
        self.gridLayout_3.addWidget(self.button_console_fg, 1, 2, 1, 1)
        self.label_console_fg = QtGui.QLabel(self.console_layout)
        self.label_console_fg.setObjectName(_fromUtf8("label_console_fg"))
        self.gridLayout_3.addWidget(self.label_console_fg, 1, 0, 1, 1)
        self.label_console_preview = QtGui.QLabel(self.console_layout)
        self.label_console_preview.setObjectName(_fromUtf8("label_console_preview"))
        self.gridLayout_3.addWidget(self.label_console_preview, 2, 0, 1, 1)
        self.console_bg = QtGui.QLineEdit(self.console_layout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console_bg.sizePolicy().hasHeightForWidth())
        self.console_bg.setSizePolicy(sizePolicy)
        self.console_bg.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.console_bg.setObjectName(_fromUtf8("console_bg"))
        self.gridLayout_3.addWidget(self.console_bg, 0, 1, 1, 1)
        self.label_console_bg = QtGui.QLabel(self.console_layout)
        self.label_console_bg.setObjectName(_fromUtf8("label_console_bg"))
        self.gridLayout_3.addWidget(self.label_console_bg, 0, 0, 1, 1)
        self.button_console_bg = QtGui.QToolButton(self.console_layout)
        self.button_console_bg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_console_bg.setObjectName(_fromUtf8("button_console_bg"))
        self.gridLayout_3.addWidget(self.button_console_bg, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 3)
        self.console_fg = QtGui.QLineEdit(self.console_layout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console_fg.sizePolicy().hasHeightForWidth())
        self.console_fg.setSizePolicy(sizePolicy)
        self.console_fg.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.console_fg.setObjectName(_fromUtf8("console_fg"))
        self.gridLayout_3.addWidget(self.console_fg, 1, 1, 1, 1)
        self.console_preview = QtGui.QLineEdit(self.console_layout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console_preview.sizePolicy().hasHeightForWidth())
        self.console_preview.setSizePolicy(sizePolicy)
        self.console_preview.setFocusPolicy(QtCore.Qt.NoFocus)
        self.console_preview.setReadOnly(True)
        self.console_preview.setObjectName(_fromUtf8("console_preview"))
        self.gridLayout_3.addWidget(self.console_preview, 2, 1, 1, 2)
        self.gridLayout_2.addWidget(self.console_layout, 0, 0, 1, 1)
        self.tabs.addTab(self.tab_interface, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)
        self.buttons = QtGui.QDialogButtonBox(PreferencesDialog)
        self.buttons.setFocusPolicy(QtCore.Qt.TabFocus)
        self.buttons.setOrientation(QtCore.Qt.Horizontal)
        self.buttons.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.gridLayout.addWidget(self.buttons, 1, 0, 1, 1)

        self.retranslateUi(PreferencesDialog)
        self.tabs.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("accepted()")), PreferencesDialog.accept)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL(_fromUtf8("rejected()")), PreferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(_translate("PreferencesDialog", "Preferences", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_serial), _translate("PreferencesDialog", "Serial", None))
        self.console_layout.setTitle(_translate("PreferencesDialog", "Console", None))
        self.button_console_fg.setText(_translate("PreferencesDialog", "...", None))
        self.label_console_fg.setText(_translate("PreferencesDialog", "Foreground:", None))
        self.label_console_preview.setText(_translate("PreferencesDialog", "Preview:", None))
        self.label_console_bg.setText(_translate("PreferencesDialog", "Background:", None))
        self.button_console_bg.setText(_translate("PreferencesDialog", "...", None))
        self.console_preview.setText(_translate("PreferencesDialog", "Lorem ipsum dolor sit...", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_interface), _translate("PreferencesDialog", "Interface", None))

