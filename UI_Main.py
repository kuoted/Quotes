# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1149, 748)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imag/Imag/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/* === Shared === */\n"
"QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, \n"
"QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog {\n"
"    color: #BBBBBB;\n"
"    font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"/* === QWidget === */\n"
"QWidget:window {\n"
"    color: #BBBBBB;\n"
"    font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"/* === QToolTip === */\n"
"QToolTip {\n"
"    color: yellow;\n"
"}\n"
"\n"
"/* === QPushButton === */\n"
"QPushButton {\n"
"    padding: 4px;\n"
"    min-width: 65px;\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: yellow;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* === Checkable items === */\n"
"QCheckBox::indicator, QRadioButton::indicator, QTreeView::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"}\n"
"\n"
"QCheckBox::indicator::checked, QRadioButton::indicator::checked, QTreeView::indicator::checked {\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled, QTreeView::indicator:disabled {\n"
"}\n"
"\n"
"QCheckBox::indicator::checked:disabled, QRadioButton::indicator::checked:disabled, QTreeView::indicator::checked:disabled {\n"
"}\n"
"\n"
"/* === QComboBox === */\n"
"QComboBox {\n"
"    color: white;\n"
"    padding:1px 2em 1px 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 6px;\n"
"    height: 6px;\n"
"}\n"
"\n"
"/* === QGroupBox === */\n"
"QGroupBox {\n"
"    margin-top: 2ex;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: yellow;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"/* === QTabWidget === */\n"
"QTabWidget::pane {\n"
"}\n"
"\n"
"/* === QTabBar === */\n"
"QTabBar::tab {\n"
"    color: #BBBBBB;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: yellow\n"
"}\n"
"\n"
"/* === QToolBar === */\n"
"QToolBar {\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QToolBar:handle {\n"
"    color: #BBBBBB;\n"
"}\n"
"\n"
"QToolBar::separator {\n"
"    width: 6px;\n"
"}\n"
"\n"
"/* === QToolButton === */\n"
"QToolButton {\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"    color: yellow;\n"
"}\n"
"\n"
"/* === QMenu === */\n"
"QMenu {\n"
"    color: white;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:disabled {\n"
"    color: #666666;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"}\n"
"\n"
"QMenu::icon:checked {\n"
"\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"/* === QMenuBar === */\n"
"QMenuBar {\n"
"    color: white;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"}\n"
"\n"
"QMenuBar::item:disabled {\n"
"    color: gray;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"}\n"
"\n"
"/* === QScrollBar:vertical === */\n"
"QScrollBar:vertical {\n"
"    width: 16px;\n"
"    margin: 16px 0 16px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 16px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    height: 16px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 16px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"}\n"
"\n"
"QScrollBar:up-arrow:vertical, QScrollBar:down-arrow:vertical {\n"
"    width: 6px;\n"
"    height: 6px;\n"
"}\n"
"\n"
"/* === QScrollBar:horizontal === */\n"
"QScrollBar:horizontal {\n"
"    height: 16px;\n"
"    margin: 0 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 16px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    width: 16px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    width: 16px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar:right-arrow:horizontal {\n"
"    width: 6px;\n"
"    height: 6px;\n"
"}\n"
"\n"
"/* =================== */\n"
"QLineEdit, QListView, QTreeView, QTableView, QAbstractSpinBox {\n"
"    color: #BBBBBB;\n"
"}\n"
"\n"
"QAbstractScrollArea, QLineEdit, QTextEdit, QAbstractSpinBox, QComboBox {\n"
"    border: 1px solid #333333;\n"
"\n"
"}\n"
"\n"
"/* === QHeaderView === */\n"
"QHeaderView::section {\n"
"    color: #BBBBBB;\n"
"    padding: 3px 0 3px 4px;\n"
"}\n"
"\n"
"/* === QListView === */\n"
"QListView::item:hover {\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    color: yellow;\n"
"}\n"
"\n"
"/* === QTableView === */\n"
"QTableView::item:hover {\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    color: yellow;\n"
"}\n"
"\n"
"/* === QTreeView === */\n"
"QTreeView::item {\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    color: yellow;\n"
"}\n"
"\n"
"QTreeView::branch {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings {\n"
"\n"
"}\n"
"\n"
"/* === Customizations === */\n"
"QFrame#infoLabel {\n"
"}\n"
"2.\n"
"\n"
".QWidget {\n"
"}\n"
"\n"
"QToolBar {\n"
"}\n"
"\n"
"QDialog, QFileDialog {\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     color: white;\n"
"     padding-left: 4px;\n"
" }\n"
"\n"
" QHeaderView::section:checked\n"
" {\n"
" }\n"
"\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-top: 5px;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
"}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QStackedWidget, QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView, QWebView, QTreeView, QHeaderView {\n"
"    selection-color: #0a214c;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QLineEdit:focus, QFrame:focus {\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame  */\n"
"QLabel {\n"
"    padding: 0;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel  */\n"
"QToolTip {\n"
"    padding: 5px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"}\n"
"\n"
"/* Force the dialog\'s buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.QFrame_Top = QtWidgets.QFrame(self.centralwidget)
        self.QFrame_Top.setMaximumSize(QtCore.QSize(16777215, 40))
        self.QFrame_Top.setStyleSheet("")
        self.QFrame_Top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.QFrame_Top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QFrame_Top.setLineWidth(0)
        self.QFrame_Top.setObjectName("QFrame_Top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.QFrame_Top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.QFrame_MainMenu = QtWidgets.QFrame(self.QFrame_Top)
        self.QFrame_MainMenu.setMaximumSize(QtCore.QSize(16777215, 40))
        self.QFrame_MainMenu.setStyleSheet("\n"
"QToolButton\n"
"{\n"
"    border:none;\n"
"    font-weight:bold;\n"
"    padding: 3px;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 15px;\n"
"    text-align: center;\n"
"    border-radius: 3;\n"
"}\n"
"QToolButton::hover, QToolButton::pressed , QToolButton::checked\n"
"{\n"
"    background-color: rgb(117,27,19);\n"
"    font-size: 15px;\n"
"    text-decoration: underline;\n"
"    text-align: right;\n"
"    padding-Top: 8px;\n"
"    font-weight:100;\n"
"    font-weight:bold;\n"
"    background-repeat:no-repeat;\n"
"    background-position: center left;\n"
"}\n"
"")
        self.QFrame_MainMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.QFrame_MainMenu.setFrameShadow(QtWidgets.QFrame.Plain)
        self.QFrame_MainMenu.setLineWidth(0)
        self.QFrame_MainMenu.setObjectName("QFrame_MainMenu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.QFrame_MainMenu)
        self.horizontalLayout_3.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.QLabeLogo = QtWidgets.QLabel(self.QFrame_MainMenu)
        self.QLabeLogo.setObjectName("QLabeLogo")
        self.horizontalLayout_3.addWidget(self.QLabeLogo)
        self.QToolButton_mRankList = QtWidgets.QToolButton(self.QFrame_MainMenu)
        self.QToolButton_mRankList.setAutoFillBackground(False)
        self.QToolButton_mRankList.setCheckable(False)
        self.QToolButton_mRankList.setAutoRaise(True)
        self.QToolButton_mRankList.setObjectName("QToolButton_mRankList")
        self.horizontalLayout_3.addWidget(self.QToolButton_mRankList)
        self.QToolButton_mLimit = QtWidgets.QToolButton(self.QFrame_MainMenu)
        self.QToolButton_mLimit.setAutoRaise(True)
        self.QToolButton_mLimit.setObjectName("QToolButton_mLimit")
        self.horizontalLayout_3.addWidget(self.QToolButton_mLimit)
        self.QToolButton_mFuctuation = QtWidgets.QToolButton(self.QFrame_MainMenu)
        self.QToolButton_mFuctuation.setAutoRaise(True)
        self.QToolButton_mFuctuation.setObjectName("QToolButton_mFuctuation")
        self.horizontalLayout_3.addWidget(self.QToolButton_mFuctuation)
        self.QToolButton_mSecType = QtWidgets.QToolButton(self.QFrame_MainMenu)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.QToolButton_mSecType.setFont(font)
        self.QToolButton_mSecType.setStyleSheet("")
        self.QToolButton_mSecType.setAutoRaise(True)
        self.QToolButton_mSecType.setObjectName("QToolButton_mSecType")
        self.horizontalLayout_3.addWidget(self.QToolButton_mSecType)
        self.QToolButton_mNews = QtWidgets.QToolButton(self.QFrame_MainMenu)
        self.QToolButton_mNews.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.QToolButton_mNews.setAutoRaise(True)
        self.QToolButton_mNews.setObjectName("QToolButton_mNews")
        self.horizontalLayout_3.addWidget(self.QToolButton_mNews)
        self.QToolButton_mBigDatas = QtWidgets.QToolButton(self.QFrame_MainMenu)
        self.QToolButton_mBigDatas.setObjectName("QToolButton_mBigDatas")
        self.horizontalLayout_3.addWidget(self.QToolButton_mBigDatas)
        self.QToolButton_Setting = QtWidgets.QToolButton(self.QFrame_MainMenu)
        self.QToolButton_Setting.setObjectName("QToolButton_Setting")
        self.horizontalLayout_3.addWidget(self.QToolButton_Setting)
        self.horizontalLayout_2.addWidget(self.QFrame_MainMenu)
        spacerItem = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.frame_2 = QtWidgets.QFrame(self.QFrame_Top)
        self.frame_2.setStyleSheet("QToolButton\n"
"{\n"
"    border:none;\n"
"    font-weight:bold;\n"
"    padding: 3px;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 15px;\n"
"    text-align: center;\n"
"}\n"
"QToolButton::hover, QToolButton::pressed , QToolButton::checked\n"
"{\n"
"    font-size: 15px;\n"
"    text-decoration: underline;\n"
"    text-align: right;\n"
"    padding-Bottom: 8px;\n"
"    font-weight:100;\n"
"\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.QToolButton_Login = QtWidgets.QToolButton(self.frame_2)
        self.QToolButton_Login.setAutoRaise(True)
        self.QToolButton_Login.setObjectName("QToolButton_Login")
        self.horizontalLayout_4.addWidget(self.QToolButton_Login)
        self.QToolButton_Min = QtWidgets.QToolButton(self.frame_2)
        self.QToolButton_Min.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Imag/Imag/minimizePressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QToolButton_Min.setIcon(icon1)
        self.QToolButton_Min.setAutoRaise(True)
        self.QToolButton_Min.setObjectName("QToolButton_Min")
        self.horizontalLayout_4.addWidget(self.QToolButton_Min)
        self.QToolButton_Normal = QtWidgets.QToolButton(self.frame_2)
        self.QToolButton_Normal.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Imag/Imag/restorePressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QToolButton_Normal.setIcon(icon2)
        self.QToolButton_Normal.setAutoRaise(True)
        self.QToolButton_Normal.setObjectName("QToolButton_Normal")
        self.horizontalLayout_4.addWidget(self.QToolButton_Normal)
        self.QToolButton_Max = QtWidgets.QToolButton(self.frame_2)
        self.QToolButton_Max.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Imag/Imag/maximizePressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QToolButton_Max.setIcon(icon3)
        self.QToolButton_Max.setAutoRaise(True)
        self.QToolButton_Max.setObjectName("QToolButton_Max")
        self.horizontalLayout_4.addWidget(self.QToolButton_Max)
        self.QToolButton_Close = QtWidgets.QToolButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.QToolButton_Close.setFont(font)
        self.QToolButton_Close.setMouseTracking(False)
        self.QToolButton_Close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.QToolButton_Close.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.QToolButton_Close.setAcceptDrops(False)
        self.QToolButton_Close.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QToolButton_Close.setAutoFillBackground(False)
        self.QToolButton_Close.setStyleSheet("")
        self.QToolButton_Close.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.QToolButton_Close.setInputMethodHints(QtCore.Qt.ImhNone)
        self.QToolButton_Close.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Imag/Imag/closePressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QToolButton_Close.setIcon(icon4)
        self.QToolButton_Close.setAutoRepeat(False)
        self.QToolButton_Close.setAutoExclusive(False)
        self.QToolButton_Close.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.QToolButton_Close.setAutoRaise(True)
        self.QToolButton_Close.setObjectName("QToolButton_Close")
        self.horizontalLayout_4.addWidget(self.QToolButton_Close)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.QFrame_Top)
        self.QFrame_Menu = QtWidgets.QFrame(self.centralwidget)
        self.QFrame_Menu.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(117,27,19);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    background-color: rgb(160,80,21);\n"
"    font-weight:bold;\n"
"    padding: 1px;\n"
"    font-family: \"Verdana\";\n"
"    font-size: 15px;\n"
"    text-align: center;\n"
"    border-style: solid;\n"
"    border-radius: 3;\n"
"}\n"
"QPushButton::hover,  QToolButton::checked\n"
"{\n"
"    font-size: 15px;\n"
"    text-decoration: underline;\n"
"    font-weight:100;\n"
"    font-weight:bold;\n"
"    background-repeat:no-repeat;\n"
"}\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: rgb(255, 253, 238);\n"
"}\n"
"")
        self.QFrame_Menu.setObjectName("QFrame_Menu")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.QFrame_Menu)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.QFrame_CMenu = QtWidgets.QFrame(self.QFrame_Menu)
        self.QFrame_CMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.QFrame_CMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QFrame_CMenu.setObjectName("QFrame_CMenu")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.QFrame_CMenu)
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5.addWidget(self.QFrame_CMenu)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.QFrame_Menu)
        self.QFrame_Right = QtWidgets.QFrame(self.centralwidget)
        self.QFrame_Right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.QFrame_Right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.QFrame_Right.setLineWidth(0)
        self.QFrame_Right.setObjectName("QFrame_Right")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.QFrame_Right)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.QFrame_Right)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tab1.setObjectName("tab1")
        self.tabWidget.addTab(self.tab1, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.QFrame_Right)
        self.sizeGrip_layout = QtWidgets.QHBoxLayout()
        self.sizeGrip_layout.setSpacing(0)
        self.sizeGrip_layout.setObjectName("sizeGrip_layout")
        self.QFrame_Bottom = QtWidgets.QFrame(self.centralwidget)
        self.QFrame_Bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.QFrame_Bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.QFrame_Bottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.QFrame_Bottom.setMidLineWidth(0)
        self.QFrame_Bottom.setObjectName("QFrame_Bottom")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.QFrame_Bottom)
        self.horizontalLayout.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.QFrame_Bottom)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.QFrame_Bottom)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(586, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.QFrame_Bottom)
        self.label_4.setMaximumSize(QtCore.QSize(20, 20))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setPixmap(QtGui.QPixmap(":/Imag/Imag/Signal.ico"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.QFrame_Bottom)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.sizeGrip_layout.addWidget(self.QFrame_Bottom)
        self.verticalLayout.addLayout(self.sizeGrip_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.QToolButton_Close.clicked.connect(MainWindow.close)
        self.QToolButton_Max.clicked.connect(MainWindow.showMaximized)
        self.QToolButton_Normal.clicked.connect(MainWindow.showNormal)
        self.QToolButton_Min.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.QLabeLogo.setText(_translate("MainWindow", "Logo"))
        self.QToolButton_mRankList.setText(_translate("MainWindow", "龙虎榜"))
        self.QToolButton_mLimit.setText(_translate("MainWindow", "涨停预测"))
        self.QToolButton_mFuctuation.setText(_translate("MainWindow", "涨跌幅追踪"))
        self.QToolButton_mSecType.setText(_translate("MainWindow", "板块追踪"))
        self.QToolButton_mNews.setText(_translate("MainWindow", "资讯"))
        self.QToolButton_mBigDatas.setText(_translate("MainWindow", "数据中心"))
        self.QToolButton_Setting.setText(_translate("MainWindow", "微信推送"))
        self.QToolButton_Login.setText(_translate("MainWindow", "[登录]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "龙虎榜"))
        self.label_2.setText(_translate("MainWindow", "需求提交，"))
        self.label_3.setText(_translate("MainWindow", "请联系QQ：542601619"))
        self.label_5.setText(_translate("MainWindow", "连接正常"))

import UI_Resource_rc
