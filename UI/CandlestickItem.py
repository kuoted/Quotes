#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate creation of a custom graphic (a candlestick plot)

"""
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

import datetime
from matplotlib.dates import date2num
import pyqtgraph as pg
import tushare as ts

#from pyqtgraph import QtCore, QtGui
## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect() 
## (see QGraphicsItem documentation)

class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, open, close, min, max
        self.generatePicture()

    def generatePicture(self):
        ## pre-computing a QPicture object allows paint() to run much more quickly, 
        ## rather than re-drawing the shapes every time.
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:            
            if open > close:
                p.setBrush(pg.mkBrush('g'))
                p.drawRect(QtCore.QRectF(t-w, open, w*2, open-close))
            elif close > open:
                p.setBrush(pg.mkBrush('r'))
                p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
            else:
                p.setBrush(pg.mkBrush('w'))
                p.drawRect(QtCore.QRectF(t-w, open, w*2, 1))
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())

class DrawChart():
    def Chart(  ):
        hist_data = ts.get_hist_data('600519',start='2017-05-01',end='2017-11-24')
        data_list = []
        for dates,row in hist_data.iterrows():
            # 将时间转换为数字
            date_time = datetime.datetime.strptime(dates,'%Y-%m-%d')
            t = date2num(date_time)
            # t = dict(enumerate(datetime))
            open,high,close,low = row[:4]
            datas = (t,open,close,low,high)
            data_list.append(datas)
        #axis_dict = dict(enumerate(axis))
        item = CandlestickItem(data_list)
        plt = pg.PlotWidget()
        plt.addItem(item,)
        plt.showGrid(x=True,y=True)
        return plt


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    
    main_window = QtGui.QMainWindow()
    main_window.setWindowTitle(__file__)
    main_window.setCentralWidget( DrawChart.Chart() )
    main_window.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app.exec_()
