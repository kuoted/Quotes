#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import * #QThreadPool, QRunnable, QThread

class FetchStockList(QRunnable):
    '''
    @param done: a signal to emit when job done.
    '''
    def __init__(self, done=None):
        super(QRunnable, self).__init__()
        self.work_obj_ = done
    def run(self):
        print('%s:%d: %s'%(sys._getframe().f_code.co_filename, sys._getframe().f_lineno, sys._getframe().f_code.co_name))
        print( 'FetchStockList:%s'%(QThread.currentThread().objectName()))
        # do something
        self.work_obj_.emitSignal()
        return

class StockListWidget(QObject):
    job_done_   = pyqtSignal()
    def __init__(self, parent=None):
        super(QObject, self).__init__()
        self.table_widget_ = QTableWidget(2, 12, parent)
        self.table_widget_.setObjectName("stock_list_")
        self.table_widget_.setGridStyle(QtCore.Qt.SolidLine)
        self.table_widget_.setSortingEnabled(True)
        self.table_widget_.setEnabled(True)
        self.job_done_.connect(self.handle_data)
        #time.sleep(2)        
        #self.job_done_.emit()
        
    @pyqtSlot()
    def handle_data(self):
        print('%s:%d: %s'%(sys._getframe().f_code.co_filename, sys._getframe().f_lineno, sys._getframe().f_code.co_name))
        print( 'StockListWidget-handle_data:%s'%(QThread.currentThread().objectName()))
        
    def widget(self):
        return self.table_widget_
    def emitSignal(self):
        self.job_done_.emit()
        
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
        
        fsl = FetchStockList( stocks_of_shanghai_ )
        QThreadPool.globalInstance().start(fsl, 0)
        
        #stocks_of_shanghai_.emitSignal()
        #fsl.run()
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