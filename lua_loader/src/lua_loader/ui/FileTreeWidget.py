# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/lua_loader/ui/FileTreeWidget.ui'
#
# Created: Thu Feb 19 20:13:55 2015
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
        FileTreeWidget.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(FileTreeWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.file_view = QtGui.QTreeView(FileTreeWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_view.sizePolicy().hasHeightForWidth())
        self.file_view.setSizePolicy(sizePolicy)
        self.file_view.setFrameShape(QtGui.QFrame.StyledPanel)
        self.file_view.setFrameShadow(QtGui.QFrame.Sunken)
        self.file_view.setObjectName(_fromUtf8("file_view"))
        self.gridLayout.addWidget(self.file_view, 0, 0, 1, 1)

        self.retranslateUi(FileTreeWidget)
        QtCore.QMetaObject.connectSlotsByName(FileTreeWidget)

    def retranslateUi(self, FileTreeWidget):
        FileTreeWidget.setWindowTitle(_translate("FileTreeWidget", "Form", None))

