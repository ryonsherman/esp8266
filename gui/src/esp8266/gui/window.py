#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from esp8266.gui.dialog import PreferencesDialog
from esp8266.gui.widget.LogWidget import LogWidget
from esp8266.gui.widget.ConsoleWidget import ConsoleWidget
from esp8266.gui.widget.FileTreeWidget import FileTreeWidget

from esp8266.gui.ui.MainWindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self, app, *args, **kwargs):
        # initialize window
        QtGui.QMainWindow.__init__(self, *args, **kwargs)

        # set app instance
        self.app = app

        # initialize user interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        
        # set app version in window title
        self._title = self.windowTitle()
        self.setWindowTitle("%s v%s" % (self._title, app.version))
        # connect last window close event to application exit
        app.lastWindowClosed.connect(app.exit)

        # initialize preferences dialog
        self.ui.prefs = PreferencesDialog(self)

        # initialize and insert file tree widget
        self.ui.file_tree = FileTreeWidget(self)
        self.ui.main_widget.layout().insertWidget(0, self.ui.file_tree)

        # initialize and insert console tab widget
        self.ui.console = ConsoleWidget(self)
        self.ui.console.ui.input.setFocus(True)
        self.ui.tabs.addTab(self.ui.console, self.tr("Console"))

        # initialize and insert (hidden) log tab widget
        self.ui.log = LogWidget(self)
        self.ui.tabs.addTab(self.ui.log, self.tr("Log"))
        self.ui.log.hide()

        # 'File -> Open File' - show open local file dialog
        self.ui.menu_open_file.triggered.connect(
            self.ui.file_tree.ui.button_open_local_file.click)
        # 'File -> Open Path' - show open local path dialog
        self.ui.menu_open_path.triggered.connect(
            self.ui.file_tree.ui.button_open_local_path.click)

        # 'Settings -> Preferences' - show preferences dialog
        self.ui.menu_prefs.triggered.connect(self.ui.prefs.show)

        # 'View -> Actions' - toggle console actions widget
        self.ui.menu_view_actions.triggered.connect(self.ui.console.ui.panel.toggle)
        # 'View -> Files' - toggle file tree widget
        self.ui.menu_view_files.triggered.connect(self.ui.file_tree.toggle)
        # 'View -> Log' - toggle log widget
        self.ui.menu_view_log.triggered.connect(self.ui.log.toggle)
