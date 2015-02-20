#!/usr/bin/env python2

__author__    = "Ryon Sherman"
__email__     = "ryon.sherman@gmail.com"
__copyright__ = "Copyright 2015, Ryon Sherman"
__license__   = "MIT"

from pygments import highlight
from pygments.lexers import LuaLexer
from pygments.formatter import Formatter

from PyQt4 import QtCore, QtGui

def hex2QColor(c):
    r = int(c[0:2], 16)
    g = int(c[2:4], 16)
    b = int(c[4:6], 16)
    return QtGui.QColor(r,g,b)

# TODO: need this?
def overrideEvent(obj, event, callback):
    event_name = event
    event = getattr(obj, event)
    setattr(obj, '_' + event_name, event)
    setattr(obj, event_name, callback)


class QFormatter(Formatter):
    def __init__(self):
        Formatter.__init__(self)
        self.styles = {}
        for token, style in self.style:
            text = QtGui.QTextCharFormat()
            if style['color']:
                text.setForeground(hex2QColor(style['color']))
            if style['bgcolor']:
                text.setBackground(hex2QColor(style['bgcolor']))
            if style['bold']:
                text.setFontWeight(QtGui.QFont.Bold)
            if style['italic']:
                text.setFontItalic(True)
            if style['underline']:
                text.setFontUnderline(True)
            self.styles[str(token)] = text

    def format(self, tokens, *args):
        self.data = []
        for token, value in tokens:
            self.data.extend([self.styles[str(token)]] * len(value))


class QSyntaxHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, *args, **kwargs):
        QtGui.QSyntaxHighlighter.__init__(self, *args, **kwargs)
        self.lexer = LuaLexer()
        self.formatter = QFormatter()

    def highlightBlock(self, text):
        pos = self.currentBlock().position()
        text = unicode(self.document().toPlainText()) + '\n'
        highlight(text, self.lexer, self.formatter)
        for i in range(len(unicode(text))):
            try:
                self.setFormat(i, 1, self.formatter.data[pos + i])
            except IndexError:
                pass
