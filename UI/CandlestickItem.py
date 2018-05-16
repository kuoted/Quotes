#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate creation of a custom graphic (a candlestick plot)

"""
import datetime
from matplotlib.dates import date2num
import pyqtgraph as pg
import tushare as ts

from pyqtgraph import QtCore, QtGui
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
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            if open > close:
                p.setBrush(pg.mkBrush('r'))
                p.drawRect(QtCore.QRectF(t-w, open, w*2, open-close))
            elif close > open:
                p.setBrush(pg.mkBrush('g'))
                p.drawRect(QtCore.QRectF(t-w, open, w*2, close-open))
            else:
                p.setBrush(pg.mkBrush('w'))
                p.drawRect(QtCore.QRectF(t-w, open, w*2, 1))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        ## boundingRect _must_ indicate the entire area that will be drawn on
        ## or else we will get artifacts and possibly crashing.
        ## (in this case, QPicture does all the work of computing the bouning rect for us)
        return QtCore.QRectF(self.picture.boundingRect())

class DrawChart():
    def chart():
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
    data = [  ## fields are (time, open, close, min, max).
        (1., 10, 13, 5, 15),
        (2., 13, 17, 9, 20),
        (3., 17, 14, 11, 23),
        (4., 14, 15, 5, 19),
        (5., 15, 9, 8, 22),
        (6., 9, 15, 8, 16),]
    item = CandlestickItem(data)
    plt = pg.plot()
    plt.addItem(item)
    plt.setWindowTitle('pyqtgraph example: customGraphicsItem')

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
