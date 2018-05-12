# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(529, 242)
        Form.setStyleSheet(_fromUtf8(""))
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setStyleSheet(_fromUtf8("QLabel{\n"
"border-radius: 4px;\n"
"selection-background-color: darkgray;\n"
"lineedit-password-character: 9679;\n"
"selection-color: #0a214c;\n"
"background-color:(0,0,0,0);\n"
"color: #666666;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"color:rgb(166,137,124);\n"
"}\n"
"QToolButton{\n"
"border-radius: 4px;\n"
"selection-background-color: darkgray;\n"
"lineedit-password-character: 9679;\n"
"selection-color: #0a214c;\n"
"background-color:(0,0,0,0);\n"
"color: #666666;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"color:rgb(166,137,124);\n"
"}\n"
"QCheckBox{\n"
"border-radius: 4px;\n"
"selection-background-color: darkgray;\n"
"lineedit-password-character: 9679;\n"
"selection-color: #0a214c;\n"
"background-color:(0,0,0,0);\n"
"color: #666666;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"color:rgb(166,137,124);\n"
"}"))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.QToolButton_Close = QtGui.QToolButton(self.frame)
        self.QToolButton_Close.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setBold(True)
        font.setWeight(75)
        self.QToolButton_Close.setFont(font)
        self.QToolButton_Close.setMouseTracking(False)
        self.QToolButton_Close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.QToolButton_Close.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.QToolButton_Close.setAcceptDrops(False)
        self.QToolButton_Close.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.QToolButton_Close.setAutoFillBackground(False)
        self.QToolButton_Close.setStyleSheet(_fromUtf8(""))
        self.QToolButton_Close.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.QToolButton_Close.setInputMethodHints(QtCore.Qt.ImhNone)
        self.QToolButton_Close.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Imag/Imag/closePressed.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QToolButton_Close.setIcon(icon)
        self.QToolButton_Close.setAutoRepeat(False)
        self.QToolButton_Close.setAutoExclusive(False)
        self.QToolButton_Close.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.QToolButton_Close.setAutoRaise(True)
        self.QToolButton_Close.setObjectName(_fromUtf8("QToolButton_Close"))
        self.horizontalLayout_2.addWidget(self.QToolButton_Close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setStyleSheet(_fromUtf8("font: 60 18pt \"Arial\";\n"
"color: rgb(255, 255, 0);\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.QLineEdit_user = QtGui.QLineEdit(self.frame)
        self.QLineEdit_user.setMinimumSize(QtCore.QSize(0, 30))
        self.QLineEdit_user.setStyleSheet(_fromUtf8("QLineEdit { \n"
"border-bottom: 1px solid #CCCCCC; \n"
"border-radius: 4px; \n"
"color: #666666; \n"
"font: 16px; \n"
"selection-background-color: darkgray; \n"
"selection-color: #0a214c; \n"
"background-image: url(:/icons/bgxx.jpg);\n"
"} \n"
"QLineEdit:hover{ \n"
"} \n"
"                "))
        self.QLineEdit_user.setText(_fromUtf8(""))
        self.QLineEdit_user.setObjectName(_fromUtf8("QLineEdit_user"))
        self.horizontalLayout_3.addWidget(self.QLineEdit_user)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.QLineEdit_Password = QtGui.QLineEdit(self.frame)
        self.QLineEdit_Password.setMinimumSize(QtCore.QSize(0, 30))
        self.QLineEdit_Password.setStyleSheet(_fromUtf8("QLineEdit{ \n"
"border-radius: 4px;\n"
"selection-background-color: darkgray;\n"
"lineedit-password-character: 9679;\n"
"color: #666666;\n"
"font: 12px;\n"
"selection-color: #0a214c;\n"
"background-image: url(:/icons/bgxx.jpg);\n"
"} \n"
"QLineEdit:hover{ \n"
"}"))
        self.QLineEdit_Password.setText(_fromUtf8(""))
        self.QLineEdit_Password.setObjectName(_fromUtf8("QLineEdit_Password"))
        self.horizontalLayout_4.addWidget(self.QLineEdit_Password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.QCheckBox_RemberPwd = QtGui.QCheckBox(self.frame)
        self.QCheckBox_RemberPwd.setStyleSheet(_fromUtf8(""))
        self.QCheckBox_RemberPwd.setChecked(False)
        self.QCheckBox_RemberPwd.setObjectName(_fromUtf8("QCheckBox_RemberPwd"))
        self.horizontalLayout.addWidget(self.QCheckBox_RemberPwd)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.QToolButton_Login = QtGui.QToolButton(self.frame)
        self.QToolButton_Login.setStyleSheet(_fromUtf8(""))
        self.QToolButton_Login.setAutoRepeatInterval(96)
        self.QToolButton_Login.setAutoRaise(True)
        self.QToolButton_Login.setObjectName(_fromUtf8("QToolButton_Login"))
        self.horizontalLayout.addWidget(self.QToolButton_Login)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.QToolButton_Register = QtGui.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(False)
        self.QToolButton_Register.setFont(font)
        self.QToolButton_Register.setStyleSheet(_fromUtf8(""))
        self.QToolButton_Register.setAutoRaise(True)
        self.QToolButton_Register.setObjectName(_fromUtf8("QToolButton_Register"))
        self.horizontalLayout_5.addWidget(self.QToolButton_Register)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.QToolButton_Close, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "数据驱动投资  科技改变金融", None))
        self.label_2.setText(_translate("Form", "用户名:", None))
        self.label_3.setText(_translate("Form", "密 码：", None))
        self.QCheckBox_RemberPwd.setText(_translate("Form", "记住密码", None))
        self.QToolButton_Login.setText(_translate("Form", "登    录", None))
        self.QToolButton_Register.setText(_translate("Form", "注册账号", None))

import UI_Resource_rc
