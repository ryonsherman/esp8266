#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os
import sys

from PyQt4 import QtGui


class dialog(object):
    @staticmethod
    def question(window, text, *args, **kwargs):
        title = kwargs.get('title', "NodeGUI")
        return QtGui.QMessageBox.question(window, title, text, *args, **kwargs)

    @staticmethod
    def warning(window, text, *args, **kwargs):
        title = kwargs.get('title', "NodeGUI " + window.tr("Warning"))
        return QtGui.QMessageBox.warning(window, title, text, *args, **kwargs)

    @staticmethod
    def critical(window, text, *args, **kwargs):
        title = kwargs.get('title', "NodeGUI " + window.tr("Error"))
        return QtGui.QMessageBox.critical(window, title, text, *args, **kwargs)

def platformSupported():
    return bool(filter(sys.platform.startswith, ['win', 'darwin', 'linux']))

def hex2QColor(c):
    c = str(c).lstrip('#')
    r = int(c[0:2], 16)
    g = int(c[2:4], 16)
    b = int(c[4:6], 16)
    return QtGui.QColor(r, g, b)

def scrollToEnd(output):
    # get console cursor
    cursor = output.textCursor()
    # move cursor to end position
    cursor.movePosition(QtGui.QTextCursor.End)
    # set console cursor
    output.setTextCursor(cursor)
    # ensure console cursor is visible
    output.ensureCursorVisible()

def fileIsBinary(path):
    text = bytearray([7, 8, 9, 10, 12, 13, 27]) + bytearray(range(0x20, 0x100))
    return bool(open(path, 'rb').read(1024).translate(None, text))
