# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QWidget_plot.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QMainWindow

import tushare as ts
import pyqtgraph as pg
import numpy as np

from UI_MainWindowEx import UI_MainWindowEx
import CandlestickItem
import candle_stick

class QuotesMainWindow( QMainWindow ):
    def __init__(self, ui_file=None, parent=None):
        super(QuotesMainWindow, self).__init__( parent )
        self.main_window = QtWidgets.QMainWindow( )
        try:
            if os.path.exists(ui_file):
                self.ui = uic.loadUi(ui_file,  self)
        except:
            self.setupGUI()
            
    def setupGUI( self ):
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
        print(sys._getframe().f_code.co_filename)  #当前位置所在的文件名
        print(sys._getframe().f_code.co_name)      #当前位置所在的函数名
        print(sys._getframe().f_lineno)            #当前位置所在的行号
        return
    def onActionRestorePreLayoutTriggered(self, changed):
        print(sys._getframe().f_code.co_name)      #当前位置所在的函数名
        print(sys._getframe().f_lineno)            #当前位置所在的行号
        return
    def onActionSaveCurLayoutTriggered(self, changed):
        print(sys._getframe().f_code.co_name)      #当前位置所在的函数名
        print(sys._getframe().f_lineno)            #当前位置所在的行号
        return

    def onKLinePeriodChanged(min, max):
        print(sys._getframe().f_code.co_name)      #当前位置所在的函数名
        print(sys._getframe().f_lineno)            #当前位置所在的行号
        return
    def onActionTriggered( me, action_ ):
        print('%d: %s'%(sys._getframe().f_lineno, sys._getframe().f_code.co_name), flush=True)
        print( "action_" + action_.objectName())
        return





if __name__ == "__main__":
    import sys
  
    import qdarkstyle
    print('%d: %s'%(sys._getframe().f_lineno, sys._getframe().f_code.co_name), flush=True)
    ui_file = []
    #ui_file = os.path.dirname(__file__) + "/mainwindow.ui"
    app = QApplication(sys.argv)
    ui = QuotesMainWindow( ui_file )
    ui.show()
    sys.exit(app.exec_())