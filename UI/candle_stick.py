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
        red_pen = pg.mkPen( 'r' )
        red_brush = pg.mkBrush( 'r' )
        
        green_pen = pg.mkPen( 'g' )
        green_brush = pg.mkBrush( 'g' )
        
        white_pen = pg.mkPen( 'w' )
        white_brush = pg.mkBrush( 'w' )

        p.setPen(white_pen)
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, open, close, min, max) in self.data:
            
            if open > close:
                #p.setPen(green_pen)
                p.setBrush(green_brush)
            elif open == close:
                #p.setPen( white_pen )
                p.setBrush( white_brush )
            else: # open < close
                #p.setPen( red_pen )
                p.setBrush( red_brush )

            p.drawRect(QtCore.QRectF(t - w, open, w * 2, close - open))
            p.drawLine(QtCore.QPointF(t, min), QtCore.QPointF(t, max))
            
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())

class DrawChart():
    def Chart( self ):            
        hist_data1 = ts.get_hist_data('600519',start='2017-05-01',end='2017-11-24')
        hist_data = hist_data1.sort_index()
        data_list = []
        t = 0
        for dates, row in hist_data.iterrows():
            open, high, close, low = row[:4]
            datas = (t, open, close, low, high)
            data_list.append(datas)
            t += 1
        item = CandlestickItem(data_list)
        xdict = {0: str(hist_data.index[0]).replace('-', '/'),
                      int((t + 1) / 2) - 1: str(hist_data.index[int((t + 1) / 2)]).replace('-', '/'),
                      t - 1: str(hist_data.index[-1]).replace('-', '/')}
        stringaxis = pg.AxisItem(orientation='bottom')
        stringaxis.setTicks([xdict.items()])
        plt = pg.PlotWidget(axisItems={'bottom': stringaxis}, enableMenu=False)
        
        plt.addItem( item )
        plt.showGrid(x=True, y=True)
        return plt
       

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    main_window = QMainWindow()
    main_window.setCentralWidget( DrawChart().Chart() )
    main_window.setWindowTitle(__file__)
    main_window.show()

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app.exec_()
