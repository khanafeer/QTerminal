# -*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
from view.terminal import Ui_Form as terminal
import sys
from math import ceil
class Terminal(QWidget,terminal):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        for i in self.findChildren(QWidget):
            i.setAttribute(Qt.WA_StyledBackground)

