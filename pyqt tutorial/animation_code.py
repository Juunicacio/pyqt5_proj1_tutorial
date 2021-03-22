import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QPen, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from ui_animation_designer import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # SHOW WINDOW
        self.show()
    
    # to draw
    def paintEvent(self, event):
        painter = QPainter(self)

        # draw in the frame
        painter.begin(self)
        painter.setPen(QPen(QColor("#a5ffe7"), 5, Qt.SolidLine))

        # call the rectangle function
        self.drawRectangle(event, painter)
        print(painter)

        painter.end()

    def drawRectangle(self, event, painter):
        painter.drawRect(50, 50, 150, 50)

class Frame(QFrame):
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.red, 4))
        painter.drawRectangle(60, 60, 200, 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())