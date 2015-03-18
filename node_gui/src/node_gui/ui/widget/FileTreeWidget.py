# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/node_gui/ui/widget/FileTreeWidget.ui'
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

class Ui_FileTreeWidget(object):
    def setupUi(self, FileTreeWidget):
        FileTreeWidget.setObjectName(_fromUtf8("FileTreeWidget"))
        FileTreeWidget.resize(411, 569)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileTreeWidget.sizePolicy().hasHeightForWidth())
        FileTreeWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(FileTreeWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabs = QtGui.QTabWidget(FileTreeWidget)
        self.tabs.setEnabled(True)
        self.tabs.setUsesScrollButtons(True)
        self.tabs.setDocumentMode(False)
        self.tabs.setTabsClosable(False)
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.local_tab = QtGui.QWidget()
        self.local_tab.setObjectName(_fromUtf8("local_tab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.local_tab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.local_files = QtGui.QTreeView(self.local_tab)
        self.local_files.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.local_files.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.local_files.setUniformRowHeights(True)
        self.local_files.setItemsExpandable(True)
        self.local_files.setHeaderHidden(True)
        self.local_files.setExpandsOnDoubleClick(True)
        self.local_files.setObjectName(_fromUtf8("local_files"))
        self.verticalLayout_3.addWidget(self.local_files)
        self.local_buttons = QtGui.QHBoxLayout()
        self.local_buttons.setObjectName(_fromUtf8("local_buttons"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.local_buttons.addItem(spacerItem)
        self.button_open_local_dir = QtGui.QPushButton(self.local_tab)
        self.button_open_local_dir.setObjectName(_fromUtf8("button_open_local_dir"))
        self.local_buttons.addWidget(self.button_open_local_dir)
        self.button_open_local_file = QtGui.QPushButton(self.local_tab)
        self.button_open_local_file.setObjectName(_fromUtf8("button_open_local_file"))
        self.local_buttons.addWidget(self.button_open_local_file)
        self.verticalLayout_3.addLayout(self.local_buttons)
        self.tabs.addTab(self.local_tab, _fromUtf8(""))
        self.remote_tab = QtGui.QWidget()
        self.remote_tab.setObjectName(_fromUtf8("remote_tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.remote_tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.remote_files = QtGui.QTreeView(self.remote_tab)
        self.remote_files.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.remote_files.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.remote_files.setUniformRowHeights(True)
        self.remote_files.setObjectName(_fromUtf8("remote_files"))
        self.verticalLayout_2.addWidget(self.remote_files)
        self.remote_buttons = QtGui.QHBoxLayout()
        self.remote_buttons.setObjectName(_fromUtf8("remote_buttons"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.remote_buttons.addItem(spacerItem1)
        self.pushButton_2 = QtGui.QPushButton(self.remote_tab)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.remote_buttons.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.remote_tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.remote_buttons.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.remote_buttons)
        self.tabs.addTab(self.remote_tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabs)

        self.retranslateUi(FileTreeWidget)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FileTreeWidget)

    def retranslateUi(self, FileTreeWidget):
        FileTreeWidget.setWindowTitle(_translate("FileTreeWidget", "Form", None))
        self.button_open_local_dir.setText(_translate("FileTreeWidget", "Open &Path", None))
        self.button_open_local_file.setText(_translate("FileTreeWidget", "&Open File", None))
        self.tabs.setTabText(self.tabs.indexOf(self.local_tab), _translate("FileTreeWidget", "Local Files", None))
        self.pushButton_2.setText(_translate("FileTreeWidget", "&Refresh", None))
        self.pushButton.setText(_translate("FileTreeWidget", "&Upload File", None))
        self.tabs.setTabText(self.tabs.indexOf(self.remote_tab), _translate("FileTreeWidget", "Remote Files", None))

