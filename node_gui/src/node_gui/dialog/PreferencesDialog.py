#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from PyQt4 import QtCore, QtGui

from node_gui import util
from node_gui.ui.dialog.PreferencesDialog import Ui_PreferencesDialog


class PreferencesDialog(QtGui.QDialog):
    def __init__(self, *args, **kwargs):
        # initialize widget
        QtGui.QDialog.__init__(self, *args, **kwargs)

        # initialize user interface
        self.ui = Ui_PreferencesDialog()
        self.ui.setupUi(self)

        # connect console color select button clicks
        self.ui.button_console_bg.clicked.connect(lambda: self.onConsoleColorSelect('bg'))
        self.ui.button_console_fg.clicked.connect(lambda: self.onConsoleColorSelect('fg'))
        # connect console color changes to preview
        self.ui.console_bg.textChanged.connect(lambda: self.onConsoleColorChanged('bg'))
        self.ui.console_fg.textChanged.connect(lambda: self.onConsoleColorChanged('fg'))

        # connect to dialog accept click
        self.accepted.connect(self.save)

    def show(self):
        # initialize console colors
        self.setConsoleColor('bg', self.parent().ui.console.bg_color)
        self.setConsoleColor('fg', self.parent().ui.console.fg_color)
        # show dialog
        QtGui.QDialog.show(self)

    def save(self):
        # update settings
        settings = self.parent().app.settings
        settings.setValue('Interface/ConsoleBGColor', self.ui.console_bg.text())
        settings.setValue('Interface/ConsoleFGColor', self.ui.console_fg.text())

    def setConsoleColor(self, context, color):
        if type(color) in [str, QtCore.QString]: color = util.hex2QColor(color)
        self.setConsolePreview(context, color)
        color = '#' + str(color.name()).lstrip('#').upper()
        getattr(self.ui, 'console_' + context).setText(color)

    def setConsolePreview(self, context, color):
        role = 'background' if context == 'bg' else 'foreground'
        preview = self.ui.console_preview
        palette = preview.palette()
        palette.setColor(getattr(preview, '%sRole' % role)(), color)
        preview.setPalette(palette)

    def onConsoleColorSelect(self, context):
        color = QtGui.QColorDialog.getColor()
        if not color: return
        if not color.isValid():
            self.parent().ui.statusbar.showMessage(self.tr("Invalid color selection!"), 3000) # 3 seconds
            return
        self.setConsoleColor(context, color)

    def onConsoleColorChanged(self, context):
        color = getattr(self.ui, 'console_' + context).text()
        try: color = util.hex2QColor(color)
        except: color = QtCore.Qt.white if context == 'bg' else QtCore.Qt.black
        self.setConsolePreview(context, color)
