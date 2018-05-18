# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(529, 242)
        Form.setStyleSheet("")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QLabel{\n"
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
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.QToolButton_Close = QtWidgets.QToolButton(self.frame)
        self.QToolButton_Close.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imag/Imag/closePressed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QToolButton_Close.setIcon(icon)
        self.QToolButton_Close.setAutoRepeat(False)
        self.QToolButton_Close.setAutoExclusive(False)
        self.QToolButton_Close.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.QToolButton_Close.setAutoRaise(True)
        self.QToolButton_Close.setObjectName("QToolButton_Close")
        self.horizontalLayout_2.addWidget(self.QToolButton_Close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 60 18pt \"Arial\";\n"
"color: rgb(255, 255, 0);\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.QLineEdit_user = QtWidgets.QLineEdit(self.frame)
        self.QLineEdit_user.setMinimumSize(QtCore.QSize(0, 30))
        self.QLineEdit_user.setStyleSheet("QLineEdit { \n"
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
"                ")
        self.QLineEdit_user.setText("")
        self.QLineEdit_user.setObjectName("QLineEdit_user")
        self.horizontalLayout_3.addWidget(self.QLineEdit_user)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.QLineEdit_Password = QtWidgets.QLineEdit(self.frame)
        self.QLineEdit_Password.setMinimumSize(QtCore.QSize(0, 30))
        self.QLineEdit_Password.setStyleSheet("QLineEdit{ \n"
"border-radius: 4px;\n"
"selection-background-color: darkgray;\n"
"lineedit-password-character: 9679;\n"
"color: #666666;\n"
"font: 12px;\n"
"selection-color: #0a214c;\n"
"background-image: url(:/icons/bgxx.jpg);\n"
"} \n"
"QLineEdit:hover{ \n"
"}")
        self.QLineEdit_Password.setText("")
        self.QLineEdit_Password.setObjectName("QLineEdit_Password")
        self.horizontalLayout_4.addWidget(self.QLineEdit_Password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.QCheckBox_RemberPwd = QtWidgets.QCheckBox(self.frame)
        self.QCheckBox_RemberPwd.setStyleSheet("")
        self.QCheckBox_RemberPwd.setChecked(False)
        self.QCheckBox_RemberPwd.setObjectName("QCheckBox_RemberPwd")
        self.horizontalLayout.addWidget(self.QCheckBox_RemberPwd)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.QToolButton_Login = QtWidgets.QToolButton(self.frame)
        self.QToolButton_Login.setStyleSheet("")
        self.QToolButton_Login.setAutoRepeatInterval(96)
        self.QToolButton_Login.setAutoRaise(True)
        self.QToolButton_Login.setObjectName("QToolButton_Login")
        self.horizontalLayout.addWidget(self.QToolButton_Login)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.QToolButton_Register = QtWidgets.QToolButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(False)
        self.QToolButton_Register.setFont(font)
        self.QToolButton_Register.setStyleSheet("")
        self.QToolButton_Register.setAutoRaise(True)
        self.QToolButton_Register.setObjectName("QToolButton_Register")
        self.horizontalLayout_5.addWidget(self.QToolButton_Register)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.frame)

        self.retranslateUi(Form)
        self.QToolButton_Close.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "数据驱动投资  科技改变金融"))
        self.label_2.setText(_translate("Form", "用户名:"))
        self.label_3.setText(_translate("Form", "密 码："))
        self.QCheckBox_RemberPwd.setText(_translate("Form", "记住密码"))
        self.QToolButton_Login.setText(_translate("Form", "登    录"))
        self.QToolButton_Register.setText(_translate("Form", "注册账号"))

import UI_Resource_rc
