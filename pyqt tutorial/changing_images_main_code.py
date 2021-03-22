import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import os

# GUI FILE
from changing_images_code import Ui_MainWindow

# IMPORT FUNCTIONS
from changing_images_function import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # When button_toggle is clicked, execute our toggleMenu function
        # give the maxwidth in px that our menu will be expanded at, when true
        #self.ui.button_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        # link our buttons with those pic methods
        self.ui.button1.clicked.connect(lambda: UIFunctions.show_pic1(self))
        self.ui.button2.clicked.connect(lambda: UIFunctions.show_pic2(self))
        self.ui.button3.clicked.connect(lambda: UIFunctions.show_pic3(self))
        self.ui.button4.clicked.connect(lambda: UIFunctions.show_pic4(self))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())