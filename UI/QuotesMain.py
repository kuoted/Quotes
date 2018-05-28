# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWidget_plot.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os
import sys

from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow

import tushare as ts
import pyqtgraph as pg
import numpy as np

from UI_MainWindowEx import UI_MainWindowEx
import CandlestickItem
import candle_stick

class QuotesMainWindow( QMainWindow ):
    def __init__(self, ui_file='', parent=None):
        super(QuotesMainWindow, self).__init__( parent )
        self.main_window = QtWidgets.QMainWindow( )
        
        if os.path.exists(ui_file):
            self.ui = uic.loadUi(ui_file,  self)
        else:
            self.__setupGUI()
            
    def __setupGUI( self ):
        self.ui = UI_MainWindowEx(self)
        
        cw = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        cw.setLayout(l)
        self.iner_kline_plot = CandlestickItem.DrawChart.Chart( )
        self.iner_macd_plot = candle_stick.DrawChart( ).Chart( )
        #self.iner_kline_plot.setXLink( self.iner_macd_plot )
        #self.iner_macd_plot.setXLink( self.iner_kline_plot )
        l.addWidget(self.iner_kline_plot)
        l.addWidget(self.iner_macd_plot)
        #self.setCentralWidget( cw )
        return

    def onKLineChanged(self, changed):
        print('%s:%d: %s'%(sys._getframe().f_code.co_name, sys._getframe().f_lineno, sys._getframe().f_code.co_name), end='\n', flush=True)
        return
    def onActionRestorePreLayoutTriggered(self, changed):
        print('%s:%d: %s'%(sys._getframe().f_code.co_name, sys._getframe().f_lineno, sys._getframe().f_code.co_name), end='\n', flush=True)
        return
    def onActionSaveCurLayoutTriggered(self, changed):
        print('%s:%d: %s'%(sys._getframe().f_code.co_name, sys._getframe().f_lineno, sys._getframe().f_code.co_name), end='\n', flush=True)
        return

    def onKLinePeriodChanged(min, max):
        print('%s:%d: %s'%(sys._getframe().f_code.co_name, sys._getframe().f_lineno, sys._getframe().f_code.co_name), end='\n', flush=True)
        return
    def onActionTriggered( me, action_ ):
        print('%s:%d: %s'%(sys._getframe().f_code.co_name, sys._getframe().f_lineno, sys._getframe().f_code.co_name), end='\n', flush=True)
        print( "action_" + action_.objectName())
        return



if __name__ == "__main__":
    import qdarkstyle
    print('%s:%d: %s\n'%(sys._getframe().f_code.co_filename, sys._getframe().f_lineno, sys._getframe().f_code.co_name))
    ui_file = ''
    #ui_file = os.path.dirname(__file__) + "/mainwindow.ui"
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ui = QuotesMainWindow( ui_file )
    ui.show()
    sys.exit(app.exec_())