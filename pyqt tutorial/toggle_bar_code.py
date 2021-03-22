import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from ui_toggle_bar_qt_designer import Ui_MainWindow

# IMPORT FUNCTIONS
from toggle_bar_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # When button_toggle is clicked, execute our toggleMenu function
        # give the maxwidth in px that our menu will be expanded at, when true
        self.ui.button_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 200, True))

        # Link the page buttons to the pages
        # Page 1
        # use lambda to avoid errors when executing a function
        # when the button is clicked, it'll go to the stackedWidget (pages_widget) and bring up the page we choose
        self.ui.bnt_page_1.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_1))
        
        # Repeat for Page 2 and 3
        self.ui.bnt_page_2.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_2))
        
        # Page 3
        self.ui.bnt_page_3.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_3))
        


      
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())