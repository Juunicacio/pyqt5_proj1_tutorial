## ==> GUI FILE
from changing_images_main_code import *

class UIFunctions(MainWindow):    
    # creating some methods that will show a different picture for each button
    def show_pic1(self):
        # paste the line where I've the photo here
        self.ui.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG1)))

    def show_pic2(self):
        self.ui.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG2)))
    
    def show_pic3(self):
        self.ui.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG3)))
    
    def show_pic4(self):
        self.ui.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG4)))