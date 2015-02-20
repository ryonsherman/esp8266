#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os

from PyQt4 import QtGui

from lua_loader.util import QSyntaxHighlighter

from lua_loader.ui.FileWidget import Ui_FileWidget

#
# TODO: PLEASE REVISIT THIS FILE!
#

class FileWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_FileWidget()
        self.ui.setupUi(self)

        # set syntax highlighter
        self.highlighter = QSyntaxHighlighter(self.ui.input.document())

        self.ui.input._keyPressEvent = self.ui.input.keyPressEvent
        self.ui.input.keyPressEvent = self.inputKeyPressEvent

        # connect 'close' button to file close
        self.ui.button_close.clicked.connect(self.closeFile)
        # connect 'save' button to file save dialog
        self.ui.button_save.clicked.connect(self.showSaveDialog)

    def inputKeyPressEvent(self, event):
        # TODO: this is kinda buggy, modifiers, etc
        self.ui.input._keyPressEvent(event)

        # ignore modifiers
        if event.modifiers(): return

        # file created
        if not self.ui.button_close.isEnabled():
            self.ui.button_close.setEnabled(True)
            self.ui.button_save.setEnabled(True)
            self.window().createFile()
            return

        # file changed
        tabs = self.window().ui.tab_view
        index = tabs.indexOf(self)
        if not str(tabs.tabText(index)).startswith('*'):
            tabs.setTabText(index, '*' + tabs.tabText(index))
        self.ui.button_save.setEnabled(True)

    def closeFile(self):
        tabs = self.window().ui.tab_view
        index = tabs.indexOf(self)

        if not self.ui.button_save.isEnabled():
            tabs.removeTab(index)
            return

        file_name = tabs.tabText(index)[1:]
        confirm = QtGui.QMessageBox().question(self, 'Save Changes', "Save changes to %s before closing?" % file_name,
            QtGui.QMessageBox.Discard, QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Save)

        if confirm == QtGui.QMessageBox.Discard:
            tabs.removeTab(index)
        elif confirm == QtGui.QMessageBox.Save:
            self.showSaveDialog()

    def showSaveDialog(self):
        path = os.path.expanduser('~')
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save File', path, '.lua')

        if not path: return

        with open(path, 'wb') as f:
            f.write(str(self.ui.input.toPlainText()).strip() + '\r\n')

        file_name = os.path.basename(str(path))
        tabs = self.window().ui.tab_view
        tabs.setTabText(tabs.indexOf(self), file_name)
        self.ui.button_save.setEnabled(False)










