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
import CandlestickItem

class QuotesMainWindow( QMainWindow ):
    def __init__(self, ui_file, parent = None):
        super(QuotesMainWindow, self).__init__( parent )
        self.mainWindow = QtWidgets.QMainWindow( )
        self.mainwidget = PyQt5.uic.loadUi( ui_file,  self.mainWindow )
        self.mainWindow.setCentralWidget(CandlestickItem.DrawChart.chart())

    def setupUi( self ):
        self.mainWindow.setObjectName( "MainWindow" )
        self.mainWindow.resize(800, 600)
        return

if __name__ == "__main__":
    import sys
    import os
    ui_file = os.path.dirname(__file__) + "/qt_designer/mainwindow.ui"
                
#    ui_file = "C:\\Users\\ted\\Documents\\GitHub\\Quotes\\UI\\qt_designer\\mainwindow.ui"
#    ui_file = "C:\\Users\\Administrator\\Documents\\GitHub\\Quotes\\UI\\qt_designer\mainwindow.ui"

    if ui_file:
        app = QtGui.QApplication(sys.argv)
        ui = QuotesMainWindow( ui_file )
        ui.setupUi( )
        ui.mainWindow.show()
        sys.exit(app.exec_())