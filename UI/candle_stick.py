#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate creation of a custom graphic (a candlestick plot)

"""
import datetime
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect() 
## (see QGraphicsItem documentation)

class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data
        self.generatePicture()

    def generatePicture(self):
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            if open > close:
                p.setPen(pg.mkPen('g'))
                p.setBrush(pg.mkBrush('g'))
                p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            else:
                p.setPen(pg.mkPen('r'))
                p.setBrush(pg.mkBrush('r'))
                p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

class DrawChart():
    def pyqtgraphDrawChart(self, code='sh', start=str(datetime.date.today() - datetime.timedelta(days=150)), end=str(datetime.date.today() + datetime.timedelta(days=1)), ktype='D'):
        try:
            self.hist_data = ts.get_hist_data(code, start, end, ktype).sort_index()
            self.data_list = []
            t = 0
            for dates, row in self.hist_data.iterrows():
                open, high, close, low = row[:4]
                datas = (t, open, close, low, high)
                self.data_list.append(datas)
                t += 1
            self.item = CandlestickItem(self.data_list)
            self.xdict = {0: str(self.hist_data.index[0]).replace('-', '/'),
                          int((t + 1) / 2) - 1: str(self.hist_data.index[int((t + 1) / 2)]).replace('-', '/'),
                          t - 1: str(self.hist_data.index[-1]).replace('-', '/')}
            self.stringaxis = pg.AxisItem(orientation='bottom')
            self.stringaxis.setTicks([self.xdict.items()])
            self.plt = pg.PlotWidget(axisItems={'bottom': self.stringaxis}, enableMenu=False)

            self.plt.addItem(self.item)
            self.plt.showGrid(x=True, y=True)
            return self.plt
        except:
            return pg.PlotWidget()

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
