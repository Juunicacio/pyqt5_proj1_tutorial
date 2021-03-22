# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'toggle_bar_qt_designerKpesJr.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 700)
        MainWindow.setMinimumSize(QSize(600, 700))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_toggle = QPushButton(self.frame_toggle)
        self.button_toggle.setObjectName(u"button_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_toggle.sizePolicy().hasHeightForWidth())
        self.button_toggle.setSizePolicy(sizePolicy)
        self.button_toggle.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"border:0px solid;\n"
"")

        self.verticalLayout_2.addWidget(self.button_toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bnt_page_1 = QPushButton(self.frame_top_menus)
        self.bnt_page_1.setObjectName(u"bnt_page_1")
        self.bnt_page_1.setMinimumSize(QSize(0, 40))
        self.bnt_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.bnt_page_1)

        self.bnt_page_2 = QPushButton(self.frame_top_menus)
        self.bnt_page_2.setObjectName(u"bnt_page_2")
        self.bnt_page_2.setMinimumSize(QSize(0, 40))
        self.bnt_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.bnt_page_2)

        self.bnt_page_3 = QPushButton(self.frame_top_menus)
        self.bnt_page_3.setObjectName(u"bnt_page_3")
        self.bnt_page_3.setMinimumSize(QSize(0, 40))
        self.bnt_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.bnt_page_3)


        self.verticalLayout_3.addWidget(self.frame_top_menus)


        self.horizontalLayout_2.addWidget(self.frame_left_menu, 0, Qt.AlignTop)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(40)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"color:#FFF")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_1)

        self.pages_widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:#FFF")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.pages_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:#FFF")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.pages_widget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.pages_widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.bnt_page_1.setText(QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.bnt_page_2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.bnt_page_3.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
    # retranslateUi

