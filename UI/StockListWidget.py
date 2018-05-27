#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #QThreadPool, QRunnable, QThread

class __FetchStockList(QRunnable):
    def __init__(self, parent):
        super(QRunnable, self).__init__()
        pass
    def run(self):
        print('%s:%d: %s'%(sys._getframe().f_code.co_filename, sys._getframe().f_lineno, sys._getframe().f_code.co_name))
        print( 'FetchStockList:%s'%(QThread.currentThread().objectName()))
        return
        
    @staticmethod
    def fetchStockList():
        pass

class StockListWidget(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__()
        self.table_widget_ = QTableWidget(2, 12, parent)
        self.table_widget_.setObjectName("stock_list_")
        self.table_widget_.setGridStyle(QtCore.Qt.SolidLine)
        self.table_widget_.setSortingEnabled(True)
        #self.table_widget_.setRowCount(2)
        #self.table_widget_.setColumnCount(12)
        self.table_widget_.setEnabled(True)
        
    def widget(self):
        return self.table_widget_
        
class StockListSubWindow(QObject):
    def __init__(self, parent=None):
        super(QObject, self).__init__(parent)
        self.tab_widget_ = QTabWidget()
        self.tab_widget_.setObjectName("all_stocks_list_")
        self.setupUi()
    
    def setupUi(self):
        stocks_of_shanghai_ = StockListWidget().widget()
        self.tab_widget_.addTab(stocks_of_shanghai_, "sh_sse")
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
    
    fs = __FetchStockList( app )
    qgs = QThreadPool.globalInstance().start(fs, 0)
    
    ret = app.exec_( )
    QThreadPool.globalInstance().waitForDone(-1)
    sys.exit(ret)