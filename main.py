import sqlite3
import sys

import os
from os import path

from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import randint


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Yellow Circles')
        self.flag = False
        self.button.clicked.connect(self.clicked)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(Qt.yellow)
        d = randint(30, 200)
        qp.drawEllipse(20, 100, d, d)
        self.flag = False

    def clicked(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec_())