# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWidget_plot.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import PyQt5
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


import pyqtgraph as pg
import tushare as ts
import candle_stick
from candle_stick import *

class Ui_MainWindow( QMainWindow ):
    def __init__(self, ui_file, parent = None):
        super(Ui_MainWindow, self).__init__( parent )
        self.mainWindow = QtWidgets.QMainWindow( )
        self.mainwidget = PyQt5.uic.loadUi( ui_file,  self.mainWindow )

    def setupUi( self ):
        self.mainWindow.setObjectName( "MainWindow" )
        self.mainWindow.resize(800, 600)
        return
        
        self.centralwidget = QtGui.QWidget(self.mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout")
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self.mainWindow)
        self.statusbar.setObjectName("statusbar")
        self.mainWindow.setStatusBar(self.statusbar)

        self.drawChart = DrawChart()
        self.verticalLayout_2.addWidget(self.drawChart.pyqtgraphDrawChart(ktype='D'))

        self.retranslateUi(self.mainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

    def retranslateUi(self, MainWindow):
        #MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.mainWindow.setWindowTitle("MainWindow")




if __name__ == "__main__":
    import sys
    import os
    ui_file = None
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.ui') and file == "mainwindow.ui":
                ui_file = file
                break
    ui_file = "C:\\Users\\ted\\Documents\\GitHub\\Quotes\\UI\\qt_designer\\mainwindow.ui"
    app = QtGui.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow() "./qt_designer/mainwindow.ui"
    if ui_file:
        ui = Ui_MainWindow( ui_file )
        ui.setupUi( )
        ui.mainWindow.show()
        sys.exit(app.exec_())