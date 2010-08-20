# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/stats.ui'
#
# Created: Fri Aug 20 13:30:58 2010
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Stats(object):
    def setupUi(self, Stats):
        Stats.setObjectName("Stats")
        Stats.resize(339, 346)
        Stats.setMinimumSize(QtCore.QSize(339, 346))
        self.centralwidget = QtGui.QWidget(Stats)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top = QtGui.QHBoxLayout()
        self.Top.setObjectName("Top")
        self.Logo = QtGui.QFrame(self.centralwidget)
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
        self.Logo.setFrameShadow(QtGui.QFrame.Raised)
        self.Logo.setObjectName("Logo")
        self.Top.addWidget(self.Logo)
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
        self.Statistics = QtGui.QGridLayout()
        self.Statistics.setObjectName("Statistics")
        self.LTotalDives = QtGui.QLabel(self.centralwidget)
        self.LTotalDives.setObjectName("LTotalDives")
        self.Statistics.addWidget(self.LTotalDives, 0, 0, 1, 1)
        self.ITotalDives = QtGui.QLabel(self.centralwidget)
        self.ITotalDives.setObjectName("ITotalDives")
        self.Statistics.addWidget(self.ITotalDives, 0, 1, 1, 1)
        self.LTotalLocations = QtGui.QLabel(self.centralwidget)
        self.LTotalLocations.setObjectName("LTotalLocations")
        self.Statistics.addWidget(self.LTotalLocations, 1, 0, 1, 1)
        self.ITotalLocations = QtGui.QLabel(self.centralwidget)
        self.ITotalLocations.setObjectName("ITotalLocations")
        self.Statistics.addWidget(self.ITotalLocations, 1, 1, 1, 1)
        self.LAvgAir = QtGui.QLabel(self.centralwidget)
        self.LAvgAir.setObjectName("LAvgAir")
        self.Statistics.addWidget(self.LAvgAir, 2, 0, 1, 1)
        self.IAvgAir = QtGui.QLabel(self.centralwidget)
        self.IAvgAir.setObjectName("IAvgAir")
        self.Statistics.addWidget(self.IAvgAir, 2, 1, 1, 1)
        self.LTotalTime = QtGui.QLabel(self.centralwidget)
        self.LTotalTime.setObjectName("LTotalTime")
        self.Statistics.addWidget(self.LTotalTime, 3, 0, 1, 1)
        self.ITotalTime = QtGui.QLabel(self.centralwidget)
        self.ITotalTime.setObjectName("ITotalTime")
        self.Statistics.addWidget(self.ITotalTime, 3, 1, 1, 1)
        self.LAvgTime = QtGui.QLabel(self.centralwidget)
        self.LAvgTime.setObjectName("LAvgTime")
        self.Statistics.addWidget(self.LAvgTime, 4, 0, 1, 1)
        self.IAvgTime = QtGui.QLabel(self.centralwidget)
        self.IAvgTime.setObjectName("IAvgTime")
        self.Statistics.addWidget(self.IAvgTime, 4, 1, 1, 1)
        self.LMaxDepth = QtGui.QLabel(self.centralwidget)
        self.LMaxDepth.setObjectName("LMaxDepth")
        self.Statistics.addWidget(self.LMaxDepth, 5, 0, 1, 1)
        self.IMaxDepth = QtGui.QLabel(self.centralwidget)
        self.IMaxDepth.setObjectName("IMaxDepth")
        self.Statistics.addWidget(self.IMaxDepth, 5, 1, 1, 1)
        self.LAvgDepth = QtGui.QLabel(self.centralwidget)
        self.LAvgDepth.setObjectName("LAvgDepth")
        self.Statistics.addWidget(self.LAvgDepth, 6, 0, 1, 1)
        self.IAvgDepth = QtGui.QLabel(self.centralwidget)
        self.IAvgDepth.setObjectName("IAvgDepth")
        self.Statistics.addWidget(self.IAvgDepth, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.Statistics)
        self.Button = QtGui.QHBoxLayout()
        self.Button.setObjectName("Button")
        self.Ok = QtGui.QPushButton(self.centralwidget)
        self.Ok.setObjectName("Ok")
        self.Button.addWidget(self.Ok)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Button.addItem(spacerItem)
        self.verticalLayout.addLayout(self.Button)
        Stats.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stats)
        QtCore.QMetaObject.connectSlotsByName(Stats)

    def retranslateUi(self, Stats):
        Stats.setWindowTitle(QtGui.QApplication.translate("Stats", "Your Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.LTitle.setText(QtGui.QApplication.translate("Stats", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600;\">Your Statistics</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.LTotalDives.setText(QtGui.QApplication.translate("Stats", "Total Dives", None, QtGui.QApplication.UnicodeUTF8))
        self.ITotalDives.setText(QtGui.QApplication.translate("Stats", "*TotalDives*", None, QtGui.QApplication.UnicodeUTF8))
        self.LTotalLocations.setText(QtGui.QApplication.translate("Stats", "Total Locations", None, QtGui.QApplication.UnicodeUTF8))
        self.ITotalLocations.setText(QtGui.QApplication.translate("Stats", "*TotalLocations*", None, QtGui.QApplication.UnicodeUTF8))
        self.LAvgAir.setText(QtGui.QApplication.translate("Stats", "Average Air Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.IAvgAir.setText(QtGui.QApplication.translate("Stats", "*AVG Air*", None, QtGui.QApplication.UnicodeUTF8))
        self.LTotalTime.setText(QtGui.QApplication.translate("Stats", "Total Dive Time", None, QtGui.QApplication.UnicodeUTF8))
        self.ITotalTime.setText(QtGui.QApplication.translate("Stats", "*TotalTime*", None, QtGui.QApplication.UnicodeUTF8))
        self.LAvgTime.setText(QtGui.QApplication.translate("Stats", "Average Dive Time", None, QtGui.QApplication.UnicodeUTF8))
        self.IAvgTime.setText(QtGui.QApplication.translate("Stats", "*AVGTime*", None, QtGui.QApplication.UnicodeUTF8))
        self.LMaxDepth.setText(QtGui.QApplication.translate("Stats", "Maximum Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.IMaxDepth.setText(QtGui.QApplication.translate("Stats", "*MaxDepth*", None, QtGui.QApplication.UnicodeUTF8))
        self.LAvgDepth.setText(QtGui.QApplication.translate("Stats", "Average Depth", None, QtGui.QApplication.UnicodeUTF8))
        self.IAvgDepth.setText(QtGui.QApplication.translate("Stats", "*AvgDepth*", None, QtGui.QApplication.UnicodeUTF8))
        self.Ok.setText(QtGui.QApplication.translate("Stats", "Ok, Thanks!", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
