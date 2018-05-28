#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt5 import QtCore
from PyQt5.QtCore import QThreadPool, QRunnable, QThread

class FetchStockList(QRunnable):
    def __init__(self, parent):
        super(QRunnable, self).__init__( )
        pass
    def run(self):
        print('%s:%d: %s\n'%(sys._getframe().f_code.co_filename, sys._getframe().f_lineno, sys._getframe().f_code.co_name))
        print( 'FetchStockList:%s'%(QThread.currentThread().objectName()))
        return
        
    @staticmethod
    def fetchStockList():
        pass
        

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QDialog
    app = QApplication(sys.argv)
    ui = QDialog( )
    ui.show( )
    
    fs = FetchStockList( app )
    qgs = QThreadPool.globalInstance().start(fs, 0)
    print('%s:%d: %s\n'%(sys._getframe().f_code.co_filename, sys._getframe().f_lineno, sys._getframe().f_code.co_name))
    print( 'fetch_stocklist.py:%s'%(QThread.currentThread().objectName()))
    ret = app.exec_( )
    QThreadPool.globalInstance().waitForDone(-1)
    sys.exit(ret)