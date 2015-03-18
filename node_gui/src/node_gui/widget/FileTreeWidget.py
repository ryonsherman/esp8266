#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os
import mimetypes

from PyQt4 import QtCore, QtGui

from node_gui import util
from node_gui.ui.widget.FileTreeWidget import Ui_FileTreeWidget


class FileTreeWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_FileTreeWidget()
        self.ui.setupUi(self)

        # initially disable 'remote' tab
        self.ui.tabs.setTabEnabled(1, False)

        # initialize local view model
        self.local_model = QtGui.QFileSystemModel()
        # set local model root path to system root
        self.local_model.setRootPath(QtCore.QDir.rootPath())

        # set local file view model
        self.ui.local_files.setModel(self.local_model)
        # set local file view index to user home directory
        self.ui.local_files.setRootIndex(self.local_model.index(QtCore.QDir.homePath()))
        # remove unnecessary columns
        map(self.ui.local_files.hideColumn, (1, 2, 3))

        # connect to open local directory button click
        self.ui.button_open_local_dir.clicked.connect(self.onButtonOpenLocalDirClicked)
        # connect to open local file button click
        self.ui.button_open_local_file.clicked.connect(self.onButtonOpenLocalFileClicked)
        # connect to local file tree double click
        self.ui.local_files.doubleClicked.connect(self.onLocalFileDoubleClicked)

        # connect to local file tree context menu
        self.ui.local_files.customContextMenuRequested.connect(self.onLocalFilesCustomContextMenuRequested)

    def show(self):
        # refresh files
        print "FileTreeWidget::show()"
        # show widget
        QtGui.QWidget.show(self)

    def toggle(self, display):
        # show or hide widget
        self.show() if display else self.hide()

    def onButtonOpenLocalDirClicked(self):
        # determine current view path
        path = str(self.local_model.filePath(self.ui.local_files.rootIndex()))
        # retrieve path name from open dialog
        path = QtGui.QFileDialog.getExistingDirectory(self, self.tr("Open Path"), path)
        # return if no path was selected
        if not path: return
        # set local file view index to selected path
        self.ui.local_files.setRootIndex(self.local_model.index(path))

    def onButtonOpenLocalFileClicked(self):
        # determine current view path
        path = str(self.local_model.filePath(self.ui.local_files.rootIndex()))
        # retrieve path name from open dialog
        path = QtGui.QFileDialog.getOpenFileNames(self, self.tr("Open File"), path, '*.lua')
        # return if no path was selected
        if not path: return
        # open file path(s)
        self.window().onEditLocalFile(path)

    def onLocalFileDoubleClicked(self, index):
        # determine path of selected index
        path = str(self.local_model.filePath(index))
        # return if path is directory
        if os.path.isdir(path): return

        # open file path(s) if binary
        if util.fileIsBinary(path):
            self.window().onOpenLocalFile(path)
        # edit file path(s)
        else:
            self.window().onEditLocalFile(path)

    def onLocalFilesCustomContextMenuRequested(self, pos):
        # initialize menu
        menu = QtGui.QMenu()
        # retrieve selected local file indexes
        index = self.ui.local_files.selectedIndexes()
        # determine local file path(s)
        path = map(self.local_model.filePath, index)

        # initialize open action
        open_action = menu.addAction(self.tr("&Open"))
        # connection open action activated click
        open_action.activated.connect(lambda: self.window().onOpenLocalFile(path))

        # initialize edit action
        edit_action = menu.addAction(self.tr("&Edit"))
        # connection edit action activated click
        edit_action.activated.connect(lambda: self.window().onEditLocalFile(path))

        # initialize delete action
        delete_action = menu.addAction(self.tr("&Delete"))
        # connection delete action activated click
        delete_action.activated.connect(lambda: self.window().onDeleteLocalFile(path))

        # map context menu to mouse position
        menu.exec_(self.ui.local_files.viewport().mapToGlobal(pos))
