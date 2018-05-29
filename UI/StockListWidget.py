#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import pandas as pd
import tushare as ts

class FetchStockList(QRunnable):
    '''
    @param done: a signal to emit when job done.
    '''
    def __init__(self, done=None):
        super(QRunnable, self).__init__()
        #super(QRunnable, self).setAutoDelete(False)
        self.work_obj_ = done
        self.df_ = None
    def run(self):
        print('%s:%d: %s'%(sys._getframe().f_code.co_filename, sys._getframe().f_lineno, sys._getframe().f_code.co_name))
        print( 'FetchStockList:idealThreadCount:%d'%(QThread.currentThread().idealThreadCount()))
        # do something
        try:
            #self.df_ = ts.get_stock_basics()
            self.df_ = ts.get_today_all()
            #self.df_ = ts.get_tick_data('600848',date='2014-01-09')
        except Exception as e:
            print(e)
            self.df_ = None
        else:            
            #self.df_.to_csv('./stock_list.csv')
            self.df_.to_csv('./stock_today_all.csv')
            
        self.work_obj_.job_done_.emit(self)
class StockListWidget(QObject):
    job_done_   = pyqtSignal(FetchStockList)
    def __init__(self, parent=None):
        super(QObject, self).__init__()
        self.table_widget_ = QTableWidget(2, 12, parent)
        self.table_widget_.setObjectName("stock_list_")
        self.table_widget_.setGridStyle(QtCore.Qt.SolidLine)
        self.table_widget_.setSortingEnabled(True)
        self.table_widget_.setEnabled(True)
        self.job_done_.connect(self.handle_data)
        self.fsl = FetchStockList( self )
        QThreadPool.globalInstance().start(self.fsl, 0)

    def retrieveStockList():
        pass
    
    #@pyqtSlot()
    def handle_data(self, run_obj):
        #run_obj = None
        print('%s:%d: %s'%(sys._getframe().f_code.co_filename, sys._getframe().f_lineno, sys._getframe().f_code.co_name))
        print('StockListWidget-handle_data:%s,obj=%s'%(QThread.currentThread().objectName(), type(run_obj)))
        print(run_obj.df_)
        
    def widget(self):
        return self.table_widget_
        
class StockListSubWindow(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self.tab_widget_ = QTabWidget()
        self.tab_widget_.setObjectName("all_stocks_list_")
        self.setupUi()
    
    def setupUi(self):
        stocks_of_shanghai_ = StockListWidget()
        
        self.tab_widget_.addTab(stocks_of_shanghai_.widget(), "sh_sse")
        self.tab_widget_.addTab(StockListWidget().widget(), "sz_sse")
        self.tab_widget_.addTab(StockListWidget().widget(), "hk_sse")
        
        
    def widget(self):
        return self.tab_widget_

if __name__ == "__main__":
    import sys
    import os
    from PyQt5.QtWidgets import QApplication, QMainWindow
    _translate = QtCore.QCoreApplication.translate
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow( )
    MainWindow.setObjectName("MainWindow")
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    MainWindow.setEnabled(True)
    MainWindow.resize(800, 600)
    central_widget = StockListSubWindow(MainWindow)
    
    MainWindow.setCentralWidget( central_widget.widget() )
    MainWindow.show()
       
    ret = app.exec_( )
    QThreadPool.globalInstance().waitForDone(-1)
    sys.exit(ret)