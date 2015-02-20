#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtCore, QtGui

from lua_loader.ui.FileTreeWidget import Ui_FileTreeWidget


class FileTreeWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QWidget.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_FileTreeWidget()
        self.ui.setupUi(self)

        # add widget to window file tree view
        self.window().ui.file_tree_view.addWidget(self)

        # connect serial data change to view update
        self.window().app.serial.signals.privateTextChanged.connect(self.onPrivateTextChanged)

        # hide widget by default
        self.hide()

    def show(self):
        # show widget
        QtGui.QWidget.show(self)
        # defer list files call until after view has been displayed
        QtCore.QTimer.singleShot(1, self.listFiles)

    def toggle(self, display):
        # show or hide widget
        self.show() if display else self.hide()

    def listFiles(self):
        # write list files command to serial
        self.window().app.serialWrite("""output = '<!--{"files":[' for k, v in pairs(file.list()) do output = output..'{"name":"'..k..'", "size":'..v..'},' end print(string.sub(output, 1, -2)..']}-->')""")

    def onPrivateTextChanged(self, data):
        files = data.get('files', None)
        if not files: return
        print files
