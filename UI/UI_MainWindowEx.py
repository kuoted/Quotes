from mainwindow import Ui_MainWindow

'''
    create our MainWindow from a sketch created by Qt Designer.
'''
class UI_MainWindowEx(Ui_MainWindow):
    def __init__(self, MainWindow):
        super(UI_MainWindowEx, self).__init__( )
        self.setupUi(MainWindow)
        
    def setupUi(self, MainWindow):
        super(UI_MainWindowEx, self).setupUi(MainWindow)
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    pass
    import sys
    import os
    import qdarkstyle
    from PyQt5 import QtWidgets, QtGui, uic
    from PyQt5.QtWidgets import QApplication, QMainWindow
    app = QApplication(sys.argv)
    win = QMainWindow( )
    ui = UI_MainWindowEx(win)
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())