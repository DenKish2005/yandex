import sqlite3
import sys

from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from random import randint
from UI import Ui_MainWindow


class Circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setBrush( QColor(randint(0, 255), randint(0, 255), randint(0, 255)) )
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