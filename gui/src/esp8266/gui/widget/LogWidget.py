#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os
import shutil

from PyQt4 import QtCore, QtGui

from esp8266.gui import util
from esp8266.gui.log import log
from esp8266.gui.ui.LogWidget import Ui_LogWidget


class LogWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_LogWidget()
        self.ui.setupUi(self)

        # connect to widget events
        self.ui.button_close.clicked.connect(self.hide)
        self.ui.button_save.clicked.connect(self.onSaveClicked)

        # connect to log buffer output
        log.buffer.signal.connect(self.onLogBufferChanged)

    def show(self):
        # get window
        window = self.window()
        # get window tabs
        tabs = window.ui.tabs
        # insert log tab at index 1 (after console)
        tabs.insertTab(1, self, self.tr("Log"))
        # set tabs index to log tab
        tabs.setCurrentIndex(1)
        # check 'View -> Log' menu option
        window.ui.menu_view_log.setChecked(True)

    def hide(self):
        # get window
        window = self.window()
        # get window tabs
        tabs = window.ui.tabs
        # remove log tab
        tabs.removeTab(1)
        # set tabs index to console tab
        tabs.setCurrentIndex(0)
        # uncheck 'View -> Log' menu option
        window.ui.menu_view_log.setChecked(False)

    def toggle(self, display):
        # show or hide widget
        self.show() if display else self.hide()

    def onLogBufferChanged(self, data):
        # get output widget
        output = self.ui.output
        # append log data to output
        output.insertPlainText(data)
        # scroll output
        util.scrollToEnd(output)

    def onSaveClicked(self):
        # get window instance
        window = self.window()
        # get current log file path
        log_file = window.app.log_file
        # append log file name to home directory path
        path = os.path.join(os.path.expanduser('~'), os.path.basename(log_file))
        # get path from file save dialog
        path = QtGui.QFileDialog.getSaveFileName(self, self.tr("Save Log File"), path, '*.txt')
        # require path
        if not path: return
        # copy log file to destination
        if path != log_file:
            shutil.copy(log_file, path)
        # set window statusbar message
        window.ui.statusbar.showMessage(self.tr("Log file saved"), 3000) # 3 seconds
