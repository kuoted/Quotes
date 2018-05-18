# -*- coding: utf-8 -*-

import configparser
import re
import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import *

from UI_Login import Ui_Form
import UI_Register
import Fuct_Account
import Fuct_Json


class MainWindow(QDialog):
	"""启动登录流程"""
	on_login_success = pyqtSignal(int)
	def __init__(self,parent=None):
		"""初始化登录界面"""
		#QtWidgets.QMainWindow.__init__(self)
		super.__init__(self)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		# 背景透明
		# self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
		self.ui.QLineEdit_user.setPlaceholderText(u'用户名')
		self.ui.QLineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
		self.ui.QLineEdit_Password.setPlaceholderText(u'密码')
		# 设置界面样式
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		# 读取配置文件
		self.Rember_Info()
		# 绑定登陆按钮
		self.ui.QToolButton_Login.clicked.connect(self.Login)
		self.ui.QToolButton_Register.clicked.connect(self.Register)


	def Rember_Info(self):
		"""读取登录信息"""
		cf = configparser.ConfigParser()
		cf.read('./Config.ini')
		# print
		Rember = cf.get("INFO", "Rember")
		usr = cf.get("INFO", "usr")
		pwd = cf.get("INFO", "pwd")
		if Rember == '0':
			self.ui.QCheckBox_RemberPwd.setChecked(True)
			self.ui.QLineEdit_user.setText(usr)
			self.ui.QLineEdit_Password.setText(pwd)

	def Save_Rember_Info(self):
		"""保存登录信息"""
		Rember = '-1'
		usr = self.ui.QLineEdit_user.text()
		pwd = self.ui.QLineEdit_Password.text()
		if self.ui.QCheckBox_RemberPwd.isChecked():
			Rember = '0'
		cf = ConfigParser.ConfigParser()
		cf.read("./Config.ini")
		cf.set("INFO", "Rember", Rember)
		cf.set("INFO", "usr", usr)
		cf.set("INFO", "pwd", pwd)
		cf.write(open("./Config.ini", "w"))

	def Login(self):
		on_login_success.emit( 0 )
		return

		"""进入登陆流程"""
		if len(self.ui.QLineEdit_user.text()) > 5 and len(self.ui.QLineEdit_Password.text()) > 5:
			# print ,
			# 登录成功
			key = ["userName", "passWord"]
			value = [str(self.ui.QLineEdit_user.text()), str(self.ui.QLineEdit_Password.text())]
			Login_INFO = dict(zip(key, value))
			Result = Fuct_Account.Login(Login_INFO)
			if Result:
				Result = Fuct_Json.Decode(Result)
				if Result["status"] == "0":
					self.close()
					self.Save_Rember_Info()
					on_login_success.emit( 0 )
					#self.emit(QtCore.SIGNAL("transfer_login"), 0)
					self.show_message(u'登陆成功！')
				else:
					self.show_message(u"登陆失败，请重试或联系客服。\n客服QQ：306911135")
			# 登录失败
			else:
				self.show_message( u"登陆失败，请重试或联系客服。\n客服QQ：306911135")
		else:
			self.show_message(u'输入信息有误，请检查用户名和密码！')

	def Register(self):
		"""新用户注册UI"""
		self.st = QDialog()
		self.setting = UI_Register.Ui_Form()
		self.setting.setupUi(self.st)
		self.st.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setting.QPustButton_Register.clicked.connect(partial(self.Register_Send))
		self.st.exec_()

	def Register_Send(self):
		"""新用户注册,功能函数"""
		UserInfo = [u'用户名', u'密码', u'确认密码', u'电话号码', u'QQ号']
		try:
			usr = str(self.setting.QLineEdit_usr.text())
			pwd = str(self.setting.QLineEdit_pwd.text())
			rpwd = str(self.setting.QLineEdit_rpwd.text())
			phone = str(self.setting.QLineEdit_phone.text())
			qq = str(self.setting.QLineEdit_qq.text())
			UserInfo_Status = 0
			for info in [usr, pwd, rpwd]:
				if len(info) > 15 or len(info) < 6:
					info_index = [usr, pwd, rpwd, phone, qq].index(info)
					self.show_message(u'【%s】长度应为6-15个字符，请修改！' %UserInfo[info_index])
					UserInfo_Status = -1
					break
			if UserInfo_Status == 0:
				for info in [usr, pwd, rpwd]:
					if self.Mach_UserInfo(info, 1):
						self.show_message(u'用户名、密码仅包含【字母或数字】，请修改！')
						UserInfo_Status = -1
						break
			if UserInfo_Status == 0:
				for info in [phone, qq]:
					if len(info) > 0:
						if self.Mach_UserInfo(info, 0):
							self.show_message(u'手机号、QQ仅包含【数字】，请修改！')
							UserInfo_Status = -1
						break
			if UserInfo_Status == 0:
				if pwd != rpwd:
					self.show_message(u'两次密码输入不一致，请修改！')
					UserInfo_Status = -1
			if UserInfo_Status == 0:
				key = ["userName", "passWord", "phone", "qq"]
				value = [usr, pwd, phone, qq]
				Register_INFO = dict(zip(key, value))
				# 发送登录Post请求
				Result = Fuct_Account.Register(Register_INFO)
				if Result:
					Result = Fuct_Json.Decode(Result)
					if Result["status"] == "0":
						self.st.close()
						self.ui.QLineEdit_user.setText(usr)
						self.ui.QLineEdit_Password.setText(pwd)
						self.show_message(u'恭喜您，注册成功！')
					elif Result["status"] == "1":
						self.show_message(u'该用户名已存在，请修改后重试！')
					else:
						self.show_message(u'注册失败，请重试或联系客服。\n客服QQ：306911135')
				else:
					self.show_message(u'注册失败，请重试或联系客服。\n客服QQ：306911135')
		except Exception as e:
			print( Exception, e )
			self.show_message(u'请检查网络是否正常！')

	def Mach_UserInfo(self, Info, Type):
		"""正则校验用户注册信息"""
		if Type == 1:
			if re.match('^[0-9a-zA-Z]+$', Info):
				return False
			else:
				return True
		else:
			if re.match('^[0-9]+$', Info):
				return False
			else:
				return True

	def show_message(self, log):
		"""消息提示框"""
		QtGui.QMessageBox.information(self, u"提示", log)

	def mousePressEvent(self,event):
		"""鼠标点击事件"""
		if event.button() == QtCore.Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			event.accept()

	def mouseMoveEvent(self,event):
		"""鼠标移动事件"""
		if event.buttons() ==QtCore.Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()

if __name__ == '__main__':
	import qdarkstyle
	app = QtWidgets.QApplication(sys.argv)
	#app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())