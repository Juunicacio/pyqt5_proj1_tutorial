# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animation_designerzqSuZP.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnChangeGraph = QPushButton(self.frame)
        self.btnChangeGraph.setObjectName(u"btnChangeGraph")
        self.btnChangeGraph.setGeometry(QRect(50, 500, 121, 61))
        self.btnChangeGraph.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border:none;\n"
"	border-radius:10px;\n"
"	color:#FFF\n"
"}")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnChangeGraph.setText(QCoreApplication.translate("MainWindow", u"Change Graph", None))
    # retranslateUi

