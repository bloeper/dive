# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/about.ui'
#
# Created: Fri Aug 20 13:45:49 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(452, 191)
        self.centralwidget = QtGui.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top = QtGui.QHBoxLayout()
        self.Top.setObjectName("Top")
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(64, 64))
        self.frame.setMaximumSize(QtCore.QSize(64, 64))
        self.frame.setBaseSize(QtCore.QSize(64, 64))
        self.frame.setStyleSheet("background-image: url(:/img/icon.png);")
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Top.addWidget(self.frame)
        self.LTitle = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LTitle.sizePolicy().hasHeightForWidth())
        self.LTitle.setSizePolicy(sizePolicy)
        self.LTitle.setMinimumSize(QtCore.QSize(0, 64))
        self.LTitle.setMaximumSize(QtCore.QSize(16777215, 64))
        self.LTitle.setBaseSize(QtCore.QSize(0, 64))
        self.LTitle.setObjectName("LTitle")
        self.Top.addWidget(self.LTitle)
        self.verticalLayout.addLayout(self.Top)
        self.Text = QtGui.QLabel(self.centralwidget)
        self.Text.setWordWrap(True)
        self.Text.setObjectName("Text")
        self.verticalLayout.addWidget(self.Text)
        self.Button = QtGui.QHBoxLayout()
        self.Button.setObjectName("Button")
        self.Ok = QtGui.QPushButton(self.centralwidget)
        self.Ok.setObjectName("Ok")
        self.Button.addWidget(self.Ok)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Button.addItem(spacerItem)
        self.verticalLayout.addLayout(self.Button)
        About.setCentralWidget(self.centralwidget)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.LTitle.setText(QtGui.QApplication.translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">About Diving Logbook</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.Text.setText(QtGui.QApplication.translate("About", "This program has been written by Tom Sleebe.\n"
"It was written pure out of love for diving and programming.\n"
"Please read the COPYING file for information about the license.\n"
"This program is written in python with the PyQT GUI FrameWork.", None, QtGui.QApplication.UnicodeUTF8))
        self.Ok.setText(QtGui.QApplication.translate("About", "Ok, Thanks!", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
