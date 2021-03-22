## ==> GUI FILE
from toggle_bar_code import *

class UIFunctions(MainWindow):

    # function to expand and collapse the menu bar
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # Get width
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            # set the default width that would be 70px
            standart = 70

            # Set max width
            if width == 70:
                # check if the menu is 70px, if yes, it'll expand, if not, collapse
                widthExtended = maxExtend
            else:
                widthExtended = standart

            # Code responsible for the animation. propertyName will be "minimumWidth"
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            # animation duration in milliseconds
            self.animation.setDuration(400)
            # set the current frame width of frame_left_menu
            self.animation.setStartValue(width)
            # to the new frame width
            self.animation.setEndValue(widthExtended)
            
            # define an animation curve for our menu
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

            self.animation.start()

