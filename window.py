# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/main.ui'
#
# Created: Sun Aug 15 13:14:33 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Logbook(object):
    def setupUi(self, Logbook):
        Logbook.setObjectName("Logbook")
        Logbook.resize(800, 600)
        Logbook.setMinimumSize(QtCore.QSize(800, 600))
        Logbook.setMaximumSize(QtCore.QSize(800, 600))
        Logbook.setBaseSize(QtCore.QSize(200, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/programming/dive/img/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Logbook.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Logbook)
        self.centralwidget.setObjectName("centralwidget")
        self.logbookImage = QtGui.QGraphicsView(self.centralwidget)
        self.logbookImage.setGeometry(QtCore.QRect(200, 0, 200, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.logbookImage.sizePolicy().hasHeightForWidth())
        self.logbookImage.setSizePolicy(sizePolicy)
        self.logbookImage.setMinimumSize(QtCore.QSize(200, 200))
        self.logbookImage.setMaximumSize(QtCore.QSize(200, 200))
        self.logbookImage.setSizeIncrement(QtCore.QSize(200, 200))
        self.logbookImage.setBaseSize(QtCore.QSize(200, 200))
        self.logbookImage.setStyleSheet("background-image: url(:/data/programming/dive/img/img/log.png);")
        self.logbookImage.setObjectName("logbookImage")
        self.LNumber = QtGui.QLabel(self.centralwidget)
        self.LNumber.setGeometry(QtCore.QRect(410, 10, 91, 18))
        self.LNumber.setObjectName("LNumber")
        self.INumber = QtGui.QLabel(self.centralwidget)
        self.INumber.setGeometry(QtCore.QRect(550, 10, 241, 18))
        self.INumber.setObjectName("INumber")
        self.LLocation = QtGui.QLabel(self.centralwidget)
        self.LLocation.setGeometry(QtCore.QRect(410, 50, 91, 18))
        self.LLocation.setObjectName("LLocation")
        self.ILocation = QtGui.QLabel(self.centralwidget)
        self.ILocation.setGeometry(QtCore.QRect(550, 50, 241, 18))
        self.ILocation.setObjectName("ILocation")
        self.LTimeIn = QtGui.QLabel(self.centralwidget)
        self.LTimeIn.setGeometry(QtCore.QRect(410, 70, 91, 18))
        self.LTimeIn.setObjectName("LTimeIn")
        self.LTimeOut = QtGui.QLabel(self.centralwidget)
        self.LTimeOut.setGeometry(QtCore.QRect(410, 90, 91, 18))
        self.LTimeOut.setObjectName("LTimeOut")
        self.ITimeIn = QtGui.QLabel(self.centralwidget)
        self.ITimeIn.setGeometry(QtCore.QRect(550, 70, 241, 18))
        self.ITimeIn.setObjectName("ITimeIn")
        self.ITimeOut = QtGui.QLabel(self.centralwidget)
        self.ITimeOut.setGeometry(QtCore.QRect(550, 90, 241, 18))
        self.ITimeOut.setObjectName("ITimeOut")
        self.LSight = QtGui.QLabel(self.centralwidget)
        self.LSight.setGeometry(QtCore.QRect(410, 110, 91, 18))
        self.LSight.setObjectName("LSight")
        self.ISight = QtGui.QLabel(self.centralwidget)
        self.ISight.setGeometry(QtCore.QRect(550, 110, 241, 18))
        self.ISight.setObjectName("ISight")
        self.LLead = QtGui.QLabel(self.centralwidget)
        self.LLead.setGeometry(QtCore.QRect(410, 130, 91, 18))
        self.LLead.setObjectName("LLead")
        self.ILead = QtGui.QLabel(self.centralwidget)
        self.ILead.setGeometry(QtCore.QRect(550, 130, 241, 18))
        self.ILead.setObjectName("ILead")
        self.LDate = QtGui.QLabel(self.centralwidget)
        self.LDate.setGeometry(QtCore.QRect(410, 30, 91, 18))
        self.LDate.setObjectName("LDate")
        self.IDate = QtGui.QLabel(self.centralwidget)
        self.IDate.setGeometry(QtCore.QRect(550, 30, 251, 18))
        self.IDate.setObjectName("IDate")
        self.LTemperature = QtGui.QLabel(self.centralwidget)
        self.LTemperature.setGeometry(QtCore.QRect(410, 150, 91, 18))
        self.LTemperature.setObjectName("LTemperature")
        self.ITemperature = QtGui.QLabel(self.centralwidget)
        self.ITemperature.setGeometry(QtCore.QRect(550, 150, 251, 18))
        self.ITemperature.setObjectName("ITemperature")
        self.LNotes = QtGui.QLabel(self.centralwidget)
        self.LNotes.setGeometry(QtCore.QRect(200, 220, 62, 18))
        self.LNotes.setObjectName("LNotes")
        self.INotes = QtGui.QTextBrowser(self.centralwidget)
        self.INotes.setGeometry(QtCore.QRect(200, 240, 591, 331))
        self.INotes.setObjectName("INotes")
        self.IDepth = QtGui.QLabel(self.centralwidget)
        self.IDepth.setGeometry(QtCore.QRect(210, 90, 41, 20))
        self.IDepth.setObjectName("IDepth")
        self.ITime = QtGui.QLabel(self.centralwidget)
        self.ITime.setGeometry(QtCore.QRect(280, 130, 51, 18))
        self.ITime.setObjectName("ITime")
        self.ListDives = QtGui.QListWidget(self.centralwidget)
        self.ListDives.setGeometry(QtCore.QRect(0, 0, 191, 581))
        self.ListDives.setObjectName("ListDives")
        self.Delete = QtGui.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(410, 180, 171, 27))
        self.Delete.setObjectName("Delete")
        self.Edit = QtGui.QPushButton(self.centralwidget)
        self.Edit.setGeometry(QtCore.QRect(590, 180, 201, 27))
        self.Edit.setObjectName("Edit")
        Logbook.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Logbook)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Logbook.setMenuBar(self.menubar)
        self.AddDive = QtGui.QAction(Logbook)
        self.AddDive.setObjectName("AddDive")
        self.Quit = QtGui.QAction(Logbook)
        self.Quit.setObjectName("Quit")
        self.Stats = QtGui.QAction(Logbook)
        self.Stats.setObjectName("Stats")
        self.About = QtGui.QAction(Logbook)
        self.About.setObjectName("About")
        self.License = QtGui.QAction(Logbook)
        self.License.setObjectName("License")
        self.menuFile.addAction(self.AddDive)
        self.menuFile.addAction(self.Stats)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Quit)
        self.menuHelp.addAction(self.About)
        self.menuHelp.addAction(self.License)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Logbook)
        QtCore.QMetaObject.connectSlotsByName(Logbook)
        Logbook.setTabOrder(self.ListDives, self.Delete)
        Logbook.setTabOrder(self.Delete, self.Edit)
        Logbook.setTabOrder(self.Edit, self.logbookImage)
        Logbook.setTabOrder(self.logbookImage, self.INotes)

    def retranslateUi(self, Logbook):
        Logbook.setWindowTitle(QtGui.QApplication.translate("Logbook", "Logbook", None, QtGui.QApplication.UnicodeUTF8))
        self.LNumber.setText(QtGui.QApplication.translate("Logbook", "Dive Number", None, QtGui.QApplication.UnicodeUTF8))
        self.INumber.setText(QtGui.QApplication.translate("Logbook", "*RealNumber*", None, QtGui.QApplication.UnicodeUTF8))
        self.LLocation.setText(QtGui.QApplication.translate("Logbook", "Location", None, QtGui.QApplication.UnicodeUTF8))
        self.ILocation.setText(QtGui.QApplication.translate("Logbook", "*RealLocation*", None, QtGui.QApplication.UnicodeUTF8))
        self.LTimeIn.setText(QtGui.QApplication.translate("Logbook", "Time In", None, QtGui.QApplication.UnicodeUTF8))
        self.LTimeOut.setText(QtGui.QApplication.translate("Logbook", "Time Out", None, QtGui.QApplication.UnicodeUTF8))
        self.ITimeIn.setText(QtGui.QApplication.translate("Logbook", "*RealTimeIn*", None, QtGui.QApplication.UnicodeUTF8))
        self.ITimeOut.setText(QtGui.QApplication.translate("Logbook", "*RealTimeOut*", None, QtGui.QApplication.UnicodeUTF8))
        self.LSight.setText(QtGui.QApplication.translate("Logbook", "Sight", None, QtGui.QApplication.UnicodeUTF8))
        self.ISight.setText(QtGui.QApplication.translate("Logbook", "*RealSight*", None, QtGui.QApplication.UnicodeUTF8))
        self.LLead.setText(QtGui.QApplication.translate("Logbook", "Lead", None, QtGui.QApplication.UnicodeUTF8))
        self.ILead.setText(QtGui.QApplication.translate("Logbook", "*RealLead*", None, QtGui.QApplication.UnicodeUTF8))
        self.LDate.setText(QtGui.QApplication.translate("Logbook", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.IDate.setText(QtGui.QApplication.translate("Logbook", "*RealDate*", None, QtGui.QApplication.UnicodeUTF8))
        self.LTemperature.setText(QtGui.QApplication.translate("Logbook", "Temperature", None, QtGui.QApplication.UnicodeUTF8))
        self.ITemperature.setText(QtGui.QApplication.translate("Logbook", "*RealTemperature*", None, QtGui.QApplication.UnicodeUTF8))
        self.LNotes.setText(QtGui.QApplication.translate("Logbook", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.IDepth.setText(QtGui.QApplication.translate("Logbook", "*depth", None, QtGui.QApplication.UnicodeUTF8))
        self.ITime.setText(QtGui.QApplication.translate("Logbook", "*time*", None, QtGui.QApplication.UnicodeUTF8))
        self.Delete.setText(QtGui.QApplication.translate("Logbook", "Remove this Dive", None, QtGui.QApplication.UnicodeUTF8))
        self.Edit.setText(QtGui.QApplication.translate("Logbook", "Edit this Dive", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("Logbook", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("Logbook", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.AddDive.setText(QtGui.QApplication.translate("Logbook", "Add Dive", None, QtGui.QApplication.UnicodeUTF8))
        self.Quit.setText(QtGui.QApplication.translate("Logbook", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.Stats.setText(QtGui.QApplication.translate("Logbook", "View Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.About.setText(QtGui.QApplication.translate("Logbook", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.License.setText(QtGui.QApplication.translate("Logbook", "License", None, QtGui.QApplication.UnicodeUTF8))

import res_rc