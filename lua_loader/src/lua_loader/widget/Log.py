#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os

from PyQt4 import QtGui

from lua_loader.ui.LogWidget import Ui_LogWidget


class LogWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_LogWidget()
        self.ui.setupUi(self)

        # add log tab to window tab view
        self.window().ui.tab_view.addTab(self, 'Log')

        # connect 'close' button to close log tab
        self.ui.button_close.clicked.connect(self.hide)
        # connect 'save' button to log save dialog
        self.ui.button_save.clicked.connect(self.onSaveClicked)

        # hide log tab by default
        self.hide()

    def show(self):
        # insert log tab into tab view at index 1 (after console)
        self.window().ui.tab_view.insertTab(1, self, 'Log')
        # set tab view index to newly inserted log tab
        self.window().ui.tab_view.setCurrentIndex(1)

    def hide(self):
        # remove log tab at index 1 (after console)
        self.window().ui.tab_view.removeTab(1)
        # set tab view to console index since log tab is gone
        self.window().ui.tab_view.setCurrentIndex(0)

    def onSaveClicked(self):
        # get path to home directory
        path = os.path.expanduser('~')
        # get path from file save dialog
        path = QtGui.QFileDialog.getSaveFileName(self, 'Save Log File', path, '.txt')
        # return if no path was provided
        if not path: return
        # write log output to file
        with open(path, 'wb') as f:
            f.write(str(self.ui.output.toPlainText()).strip() + '\r\n')
