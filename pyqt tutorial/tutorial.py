from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

"""
When we're working with PyQt, the first thing we need
to do when we're creating an app or creating a GUI, is
define an application. Create a function, called window,
that will do it for us and we're gonna run that function
at the end of our code. Passing sys.argv as argument, that
gives some kind of config setup for a QApp, so it knows
what os it's running on, how to display the window.

The next thing to do is create come kind of window or 
some kind of widget, that we're gonna show in our App.
In this case we're gonna use QMainWindow, but some cases,
people use QWidget, it's kind similar.

Next thing is set the size and title of our window, so
if you wanna set the size and actually the position of
it on the screen, we need to call a method called "set
geometry, giving 4 arg: the xpos, ypos, width and height"

Now, we're gonna set the window title.

To show our window, we need to call win.show()
and then, after that, we need to write one line that makes
sure that our window shows up and we'll exit when we click
the x button. A clean exit.

Then we can put some stuff iside our window.
"""
# Definning a function to trigger when the button 
# was clicked
def was_clicked():
    # first we'll print something just to make sure that
    # everything is working
    #print("clicked")
    # but, just showing a print is not what we wanna do,
    # maybe we can change the content of that label


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 500, 500)
    win.setWindowTitle("PyQt5 - test")

    # Adding a label
    # creating a label, saying where it's gonna be
    label = QtWidgets.QLabel(win)
    # adding a label into the window
    label.setText("my first label")
    # to move the label, taking xy position
    label.move(50,50)

    # Adding a button
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click here")
    # map this button click to an event, something that
    # will happens when we click this button
    # first we need to create a function, that will
    # trigger when that button was clicked. The name
    # of the function inside the () without its ().
    b1.clicked.connect(was_clicked)
    # to change the label with a click, this line above,
    # needs to be map to a function and that was_clicked
    # function has no access to the label.
    # now, we need to rewrite that code into a class, 
    # that all of the methods will access to everything
    # see rewriting_tutorial_file.py


    win.show()
    sys.exit(app.exec_())

# Calling the window
window()

