#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

import os
import sys

from PyQt4 import QtGui

def hex2QColor(c):
    # get hex color string
    c = str(c).lstrip('#')
    # parse red value
    r = int(c[0:2], 16)
    # parse green value
    g = int(c[2:4], 16)
    # parse blue value
    b = int(c[4:6], 16)
    # return QColor object
    return QtGui.QColor(r, g, b)

def scrollBuffer(buf, pos):
    # get buffer cursor
    cursor = buf.textCursor()
    # move cursor to position
    cursor.movePosition(pos)
    # set buffer cursor
    buf.setTextCursor(cursor)
    # ensure buffer cursor is visible
    buf.ensureCursorVisible()

def scrollToStart(buf):
    # scroll to start of buffer
    return scrollBuffer(buf, QtGui.QTextCursor.Start)

def scrollToEnd(buf):
    # scroll to end of buffer
    return scrollBuffer(buf, QtGui.QTextCursor.End)

def fileIsBinary(path):
    # determine text byte array
    text = bytearray([7, 8, 9, 10, 12, 13, 27]) + bytearray(range(0x20, 0x100))
    # return true if file is binary
    return bool(open(path, 'rb').read(1024).translate(None, text))


class dialog(object):
    @staticmethod
    def question(window, text, *args, **kwargs):
        title = kwargs.get('title', window._title)
        return QtGui.QMessageBox.question(window, title, text, *args, **kwargs)

    @staticmethod
    def warning(window, text, *args, **kwargs):
        title = kwargs.get('title', window._title + ' ' + window.tr("Warning"))
        return QtGui.QMessageBox.warning(window, title, text, *args, **kwargs)

    @staticmethod
    def critical(window, text, *args, **kwargs):
        title = kwargs.get('title', window._title + ' ' + window.tr("Error"))
        return QtGui.QMessageBox.critical(window, title, text, *args, **kwargs)
