from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# in the file tutorial, the function was_clicked had 
# no access to the label inside the window funtion.
# So we're gonna to rewrite that code into a class
# that all of the methods will access to everything

# that class we're gonna inherit from QMainWindow.
# meaning that we're gonna take all the properties
# that QMainWindow has, and we're gonna use them in
# MyWindow, changing, modifying and adding some things
class MyWindow(QMainWindow):
    # first write the init method, with self as atribute
    # that will run wherever atributes on MyWindow
    def __init__(self):
        # inside we're gonna call our parent constructor
        super(MyWindow, self).__init__()
        # inside the init method, we set the Geometry
        # of the window and its title
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("PyQt5 - test")
        # here is where we call the method initUI
        self.initUI()

    # the next method 
    def initUI(self):
        # we put here all the stuff we want in our window
        # like the label and the button we've created 
        # before. Changing the 'win' that now is actually
        # the MyWindow, so we write 'self'

        # creating a label, saying where it's gonna be
        self.label = QtWidgets.QLabel(self)
        # adding a label into the window
        self.label.setText("my first label")
        # to move the label, taking xy position
        self.label.move(50,50)

        # Adding a button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click here")
        # map this button click to an event
        self.b1.clicked.connect(self.was_clicked)

        # The reason of this, is that I want to be able
        # to access any label and b1 anywhere throughout
        # my class. So now when I click a button, I can
        # change the label text from inside of the function,
        # because it's a part of the class
    
    # Define method called was_clicked
    def was_clicked(self):
        self.label.setText("You pressed the button!")
        self.update()
        """ 
        the text is being cut off, and this is because
        when we modify some of the attributes, that are
        inside of our window, we need to change the size
        of them as well.
        To update the width of this text, we need to create
        a method called update
        """
            
    # Define update method, this will be called
    # everytime we click the button
    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    # the window here, needs to be an instance of MyWindow
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

# Calling the window
window()
