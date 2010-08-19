# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/about.ui'
#
# Created: Wed Aug 18 17:57:10 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(352, 326)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setMinimumSize(QtCore.QSize(352, 326))
        About.setMaximumSize(QtCore.QSize(352, 326))
        About.setBaseSize(QtCore.QSize(352, 326))
        self.centralwidget = QtGui.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TopLay = QtGui.QHBoxLayout()
        self.TopLay.setObjectName("TopLay")
        self.LogoFrame = QtGui.QFrame(self.centralwidget)
        self.LogoFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.LogoFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.LogoFrame.setObjectName("LogoFrame")
        self.Logo = QtGui.QGraphicsView(self.LogoFrame)
        self.Logo.setGeometry(QtCore.QRect(0, 0, 64, 64))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logo.sizePolicy().hasHeightForWidth())
        self.Logo.setSizePolicy(sizePolicy)
        self.Logo.setMinimumSize(QtCore.QSize(64, 64))
        self.Logo.setMaximumSize(QtCore.QSize(64, 64))
        self.Logo.setBaseSize(QtCore.QSize(64, 64))
        self.Logo.setStyleSheet("background-image: url(:/img/icon.png);")
        self.Logo.setFrameShape(QtGui.QFrame.NoFrame)
        self.Logo.setObjectName("Logo")
        self.TopLay.addWidget(self.LogoFrame)
        self.Title = QtGui.QLabel(self.centralwidget)
        self.Title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Title.setObjectName("Title")
        self.TopLay.addWidget(self.Title)
        self.verticalLayout_2.addLayout(self.TopLay)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Text = QtGui.QLabel(self.centralwidget)
        self.Text.setObjectName("Text")
        self.verticalLayout.addWidget(self.Text)
        spacerItem = QtGui.QSpacerItem(20, 65, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.ButtonsLay = QtGui.QHBoxLayout()
        self.ButtonsLay.setObjectName("ButtonsLay")
        self.Ok = QtGui.QPushButton(self.centralwidget)
        self.Ok.setObjectName("Ok")
        self.ButtonsLay.addWidget(self.Ok)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ButtonsLay.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.ButtonsLay)
        About.setCentralWidget(self.centralwidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.Title.setText(QtGui.QApplication.translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600;\">About</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.Text.setText(QtGui.QApplication.translate("About", "This Program is written by Tom Sleebe.\n"
"It\'s written in Python with the PyQT Gui Framework.\n"
"It\'s primarely written to scratch my own itch,\n"
"to learn more about python and pyqt.\n"
"Please read the Copying file included \n"
"by this program.", None, QtGui.QApplication.UnicodeUTF8))
        self.Ok.setText(QtGui.QApplication.translate("About", "Ok, Thanks", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
