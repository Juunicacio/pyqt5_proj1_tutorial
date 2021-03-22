from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, QRectF)
from PyQt5.QtGui import (QTextDocument, QPen, QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import os

## QPixmap only works with absolute Path
## add os.path.dirname(__file__) and then join it with the path of the folder and the image

# IMAGES PATH
FILEPATH = os.path.dirname(__file__)
TURTLE_IMG = "assets\\Tartaruga.png"
IMG1 = "assets\\mod_deep_sea_2d_1.jpg"
IMG2 = "assets\\deep_sea_2d_2.jpg"
IMG3 = "assets\\deep_sea_2d_3.jpeg"
IMG4 = "assets\\deep_sea_2d_4.png"

# GRAPH VARIABLES
MARGIN_WIDTH = 90
MARGIN_HEIGHT = 20

# DEFINITIONS FOR THE GRAPH - RIGHT HORIZONTAL LINE
START_RIGHT_LINES = MARGIN_WIDTH-5
WIDTH_LINES = 8

# DEFINITIONS FOR THE GRAPH - LEFT HORIZONTAL LINE
START_LEFT_LINES = MARGIN_WIDTH-12.5

# DEFINITIONS FOR THE LABELS TEXT
RIGHT_TEXT_OFFSET = 6 # higher the text goes left
LEFT_TEXT_OFFSET = 4
UP_OFFSET_LEFT_TEXT = 8
UP_OFFSET_RIGTH_TEXT = 5

# DEFINITIONS FOR THE LABELS
# or 135 OR LAYERS_LEVEL[0]
RECT_LAYERS_START = 80
RECT_LAYERS_HEIGHT = 35

LAYERS_OFFSET = 2

LAYERS_LEVEL = []

class MyCustomLabel(QLabel):
    def __init__(self,parent):
        #Initialize QLabel with its parent
        super().__init__(parent)       

    # define a function to return the label width
    def get_width(self):
        return self.frameGeometry().width()

    # define a function to return the label height
    def get_height(self):
        return self.frameGeometry().height()

    # define a function to give the label width a margin
    def widthMargin(self):        
        return self.get_width() - (MARGIN_WIDTH*2)
    
    # define a function to give the label height a margin
    def heightMargin(self):        
        return self.get_height() - (MARGIN_HEIGHT*2)

    def widthMarginLine(self):
        return self.get_width() + (-START_RIGHT_LINES)

    # If I want to draw a line above the first layer
    #def minimumWindowWidthLayers(self):
        #return self.get_width() - (START_RIGHT_LINES)      

    def drawLayer(self, color, i, meters_deep):
        # Layers Rectangles
        layer = QPainter(self)
        layer.setPen(QPen(QColor(color), 2, Qt.SolidLine))
        layer.setBrush(QBrush(QColor(color), Qt.SolidPattern))
        layer.drawRect(MARGIN_WIDTH+LAYERS_OFFSET, LAYERS_LEVEL[i], self.widthMargin()-LAYERS_OFFSET*1.5, RECT_LAYERS_HEIGHT)

    #def drawHorizontalLine(self, i):
        horizontal_line = QPainter(self)
        horizontal_line.setPen(QPen(Qt.black, 3, Qt.SolidLine))        
        # Right Side
        if i <= 10:
            horizontal_line.drawLine(self.widthMarginLine(), LAYERS_LEVEL[i], self.widthMarginLine()+WIDTH_LINES, LAYERS_LEVEL[i])
        # Left Side
        horizontal_line.drawLine(START_LEFT_LINES, LAYERS_LEVEL[i], START_LEFT_LINES+WIDTH_LINES, LAYERS_LEVEL[i]) 

    #def drawVerticalLine(self, i):
        if i != 11:
            vertical_line = QPainter(self)
            vertical_line.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        # Right Side
            if i <= 9:
                vertical_line.drawLine(self.widthMarginLine()+WIDTH_LINES, LAYERS_LEVEL[i], self.widthMarginLine()+WIDTH_LINES, LAYERS_LEVEL[i+1])
        # Left Side
            vertical_line.drawLine(START_LEFT_LINES, LAYERS_LEVEL[i], START_LEFT_LINES, LAYERS_LEVEL[i+1])        
        
        # Draw Left Text
        layers_left_text = QPainter(self)
        # Draw Text with QTextDocument
        doc_left_text = QTextDocument(self)
        rect1 = QRectF(0,0,70,50)        
        doc_left_text.setTextWidth(rect1.width())
        if i <= 9: 
            doc_left_text.setHtml(f"<font size=-1><b><p align=center>{meters_deep}<br> meters</b></font></p> ")
            layers_left_text.translate(LEFT_TEXT_OFFSET,LAYERS_LEVEL[i]+1)
        elif i == 10:
            doc_left_text.setHtml(f"<font size=-1><b><p align=center>below<br>{meters_deep}<br>meters</b></font></p>")
            layers_left_text.translate(LEFT_TEXT_OFFSET,LAYERS_LEVEL[i]-2)
        else:
            doc_left_text.setHtml(f"<font size=+1><b><p align=center>{meters_deep}</b></font></p>")
            layers_left_text.translate(LEFT_TEXT_OFFSET-1,LAYERS_LEVEL[i]+UP_OFFSET_LEFT_TEXT)
        doc_left_text.drawContents(layers_left_text, rect1)

        # Draw Rigth Text
        if i <= 9:
            layers_right_text = QPainter(self)
            # Draw Text with QTextDocument
            doc_rigth_text = QTextDocument(self)
            rect2 = QRectF(0,0,100,50) 
            doc_rigth_text.setTextWidth(rect2.width())
            doc_rigth_text.setHtml(f"<font size=+1><b><p align=center>Layer {i+1}</b></font></p>")
            if i <=8:
                layers_right_text.translate(self.widthMarginLine()-RIGHT_TEXT_OFFSET,LAYERS_LEVEL[i]+UP_OFFSET_RIGTH_TEXT)#+TEXT_DISTANCES)
            else:
                layers_right_text.translate(self.widthMarginLine()-RIGHT_TEXT_OFFSET+2,LAYERS_LEVEL[i]+UP_OFFSET_RIGTH_TEXT)#+TEXT_DISTANCES)
            doc_rigth_text.drawContents(layers_right_text, rect2)

    def paintEvent(self, event):
        super().paintEvent(event)
        #print("paint label")
        # Draw Layers
        self.drawLayer('#c9f2e7', 0, "0-5")
        self.drawLayer('#a5e1e7', 1, "6-10")
        self.drawLayer('#75c8dc', 2, "11-20")
        self.drawLayer('#41b2dc', 3, "21-30")
        self.drawLayer('#1d9af2', 4, "31-40")
        self.drawLayer('#0078f2', 5, "41-50")
        self.drawLayer('#005df2', 6, "51-70")
        self.drawLayer('#093aff', 7, "71-90")
        self.drawLayer('#091bff', 8, "91-110")
        self.drawLayer('#0014cc', 9, "111-4095")
        self.drawLayer('#0502b0', 10, "4096")
        self.drawLayer('#5e512e', 11, "Seabed") 

        # Draw Border of the Graph
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        painter.drawRect(MARGIN_WIDTH, MARGIN_HEIGHT, self.widthMargin(), self.heightMargin())

        # Draw Image
        turtle_width = 50
        turtle_heigth = 40
        painter.drawImage(QRectF((self.get_width()/2 - turtle_width/2 +3),LAYERS_LEVEL[0]-2,turtle_width,turtle_heigth), QtGui.QImage(os.path.join(FILEPATH , TURTLE_IMG)), QRectF(0,0,turtle_width,turtle_heigth))             

class MyCustomMainWindow(QMainWindow):    
    def __init__(self):
        super().__init__()
        #print(LAYERS_LEVEL)        
        self.WINDOWHEIGHT = LAYERS_LEVEL[-1] +1+ MARGIN_HEIGHT # layers_level[-1](532) + offset(1) + margin_height(20)
        self.MAXWINDOWWIDTH = 500
        self.MINWINDOWWIDTH = 400

        self.setObjectName("MainWindow")
        #self.resize(800, 600)        
        self.setMinimumSize(self.MINWINDOWWIDTH, self.WINDOWHEIGHT)
        self.setMaximumSize(self.MAXWINDOWWIDTH, self.WINDOWHEIGHT)
        self.setupUi()

        # remove window frame
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        
    def setupUi(self):
        #Create and configure wall
        self.wall = QtWidgets.QWidget(self)
        self.wall.setObjectName("wall")        
        
        #Create and configure wall image
        self.LB_image = MyCustomLabel(self.wall)
        self.LB_image.setGeometry(QtCore.QRect(0, 0, 831, 451))
        self.LB_image.setText("")
        # copy that line bellow, to change the photo when we click the buttons
        self.LB_image.setPixmap(QtGui.QPixmap(os.path.join(FILEPATH , IMG1))) # use os.path.join to join the path and the folder
        self.LB_image.setScaledContents(True)
        self.LB_image.setObjectName("label")
        
        ##Create abd configure wall buttons
        # self.button1 = QtWidgets.QPushButton(self.wall)
        # self.button1.setGeometry(QtCore.QRect(100, 470, 121, 51))
        # self.button1.setObjectName("button1")
        # self.button2 = QtWidgets.QPushButton(self.wall)
        # self.button2.setGeometry(QtCore.QRect(260, 470, 121, 51))
        # self.button2.setObjectName("button2")
        # self.button3 = QtWidgets.QPushButton(self.wall)
        # self.button3.setGeometry(QtCore.QRect(420, 470, 121, 51))
        # self.button3.setObjectName("button3")
        # self.button4 = QtWidgets.QPushButton(self.wall)
        # self.button4.setGeometry(QtCore.QRect(580, 470, 121, 51))
        # self.button4.setObjectName("button4")

        self.setCentralWidget(self.wall)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MyCustomMainWindow"))
        
        # self.button1.setText(_translate("MainWindow", "1"))        
        # self.button2.setText(_translate("MainWindow", "2"))
        # self.button3.setText(_translate("MainWindow", "3"))
        # self.button4.setText(_translate("MainWindow", "4"))

        #QtCore.QMetaObject.connectSlotsByName(self)

        ## link our buttons with those pic methods
        # self.button1.clicked.connect(self.show_pic1)
        # self.button2.clicked.connect(self.show_pic2)
        # self.button3.clicked.connect(self.show_pic3)
        # self.button4.clicked.connect(self.show_pic4)

    ## creating some methods that will show a different picture for each button
    def show_pic1(self):
        ## paste the line where I've the photo here
        self.LB_image.setPixmap(QtGui.QPixmap(os.path.join(FILEPATH , IMG1)))

    def show_pic2(self):
        self.LB_image.setPixmap(QtGui.QPixmap(os.path.join(FILEPATH , IMG2)))
    
    def show_pic3(self):
        self.LB_image.setPixmap(QtGui.QPixmap(os.path.join(FILEPATH , IMG3)))
    
    def show_pic4(self):
        self.LB_image.setPixmap(QtGui.QPixmap(os.path.join(FILEPATH , IMG4)))

    # Resize image with window
    def resizeEvent(self, event):
        self.LB_image.resize(self.width(), self.height())
    
    #def paintEvent(self, event):
        #print("test")

if __name__ == "__main__":
    import sys

    ## after the first layer, each next one have to be the layers_height + 1 the previous one      
    for i in range(13):
        LAYERS_LEVEL.append(RECT_LAYERS_START + (RECT_LAYERS_HEIGHT+1)*i)
    #print(LAYERS_LEVEL)

    app = QtWidgets.QApplication(sys.argv)
    myMainWindow = MyCustomMainWindow()
    myMainWindow.show()
    sys.exit(app.exec_())
    
