#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtGui

from node_gui import widget, dialog
from node_gui.ui.window.MainWindow import Ui_MainWindow


class MainWindow(QtGui.QMainWindow):
    def __init__(self, app, *args, **kwargs):
        # initialize window
        QtGui.QMainWindow.__init__(self, *args, **kwargs)

        # set app instance
        self.app = app

        # set app version in window title
        self.setWindowTitle("%s v%s" % (self.windowTitle(), app.version))

        # initialize user interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize preferences dialog
        self.ui.prefs = dialog.PreferencesDialog(self)

        # initialize and insert local/remote file tree widget
        self.ui.file_tree = widget.FileTreeWidget(self)
        self.ui.main_widget.layout().insertWidget(0, self.ui.file_tree)

        # initialize and insert console tab widget
        self.ui.console = widget.ConsoleWidget(self)
        self.ui.tabs.addTab(self.ui.console, self.tr("Console"))

        # initialize and insert (hidden) log tab widget
        self.ui.log = widget.LogWidget(self)
        self.ui.tabs.addTab(self.ui.log, self.tr("Log"))
        self.ui.log.hide()

        # connect to 'File -> Open File' menu action click
        self.ui.menu_open_file.triggered.connect(self.ui.file_tree.onButtonOpenLocalFileClicked)
        # connect to 'File -> Open Path' menu action click
        self.ui.menu_open_dir.triggered.connect(self.ui.file_tree.onButtonOpenLocalDirClicked)

        # connect to 'Settings -> Preferences' menu action click
        self.ui.menu_prefs.triggered.connect(self.ui.prefs.show)
        # connect to 'View -> Actions' menu action click
        self.ui.menu_view_actions.triggered.connect(self.ui.console.ui.panel.toggle)
        # connect to 'View -> Files' menu action click
        self.ui.menu_view_files.triggered.connect(self.ui.file_tree.toggle)
        # connect to 'View -> Log' menu action click
        self.ui.menu_view_log.triggered.connect(self.ui.log.toggle)

        # set focus to console input
        self.ui.console.ui.input.setFocus(True)

    def onOpenLocalFile(self, paths):
        # normalize paths
        if type(paths) is not list:
            paths = [paths]
        # open file paths
        map(self.app.openLocalFile, paths)

    def onEditLocalFile(self, paths):
        # normalize paths
        if type(paths) is not list:
            paths = [paths]
        # iterate file paths
        for path in paths:
            print 'MainWindow::onEditLocalFile(%s)' % path

    def onDeleteLocalFile(self, paths):
        print 'MainWindow::onDeleteLocalFile()'

    def onOpenRemoteFile(self, paths):
        print 'MainWindow::onOpenRemoteFile()'

    def onEditRemoteFile(self, paths):
        print 'MainWindow::onEditRemoteFile()'

    def onDeleteRemoteFile(self, paths):
        print 'MainWindow::onDeleteRemoteFile()'

















