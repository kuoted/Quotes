# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWidget_plot.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
#import PyQt5
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

import tushare as ts
import pyqtgraph as pg
import numpy as np

import CandlestickItem
import candle_stick

def clicked(plot, points):
    global lastClicked
    for p in lastClicked:
        p.resetPen()
    print("clicked points", points)
    for p in points:
        p.setPen('b', width=2)
    lastClicked = points
    return

class QuotesMainWindow( QMainWindow ):
    def __init__(self, ui_file, parent = None):
        super(QuotesMainWindow, self).__init__( parent )
        #self.main_window = QtWidgets.QMainWindow( )
        #self.mainwidget = PyQt5.uic.loadUi( ui_file,  self )
        #self.setCentralWidget(CandlestickItem.DrawChart.chart())
        #self.setCentralWidget(candle_stick.DrawChart().pyqtgraphDrawChart())
        self.lastClicked = []
        self.setupGUI()
        
    def setupGUI( self ):
        cw = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        cw.setLayout(l)
        
        self.iner_kline_plot = CandlestickItem.DrawChart.Chart( )
        self.iner_macd_plot = candle_stick.DrawChart( ).Chart( )
        #self.iner_kline_plot.setXLink( self.iner_macd_plot )
        #self.iner_macd_plot.setXLink( self.iner_kline_plot )
        
        l.addWidget(self.iner_kline_plot)
        l.addWidget(self.iner_macd_plot)
        
        self.setCentralWidget( cw )
        return

    def setupUi( self ):
        self.setObjectName( "MainWindow" )
        self.resize(800, 600)
        return

if __name__ == "__main__":
    import sys
    import os
    ui_file = os.path.dirname(__file__) + "/qt_designer/mainwindow.ui"
                
    if ui_file:
        app = QApplication(sys.argv)
        ui = QuotesMainWindow( ui_file )
        ui.setupUi( )
        ui.show()
        sys.exit(app.exec_())