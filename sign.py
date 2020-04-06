# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Form_2(object):

	def messageBox(self, title, message):
		mess = QtWidgets.QMessageBox()
		mess.setWindowTitle(title)
		mess.setText(message)
		mess.StandardButtons(QtWidgets.QMessageBox.Ok)
		mess.exec_()

	def signup(self):
		user1 = self.lineEdit.text()
		name = self.lineEdit_2.text()
		email = self.lineEdit_3.text()
		contact = self.lineEdit_4.text()
		pasword = self.lineEdit_5.text()
		conn = sqlite3.connect("Staff.db")
		cur = conn.cursor()
		tbl = "CREATE TABLE IF NOT EXISTS user_sign(Username varchar(20) primary key, FName varchar(20), Email varchar(35) not null, Contact numeric(10) not null, Passwordd varchar(15) not null)"
		cur.execute(tbl)
		query = "insert into user_sign (Username, FName, Email, Contact, Passwordd) values('%s','%s','%s','%s','%s')" %(user1, name, email, contact, pasword)
		try:
			cur.execute(query)
			conn.commit()
			self.messageBox("Congrats", "You're successfully signed up.")
		except:
			conn.rollback()
			self.messageBox("Warning","You've enter wrong details.")
	
	
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(543, 527)
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(190, 30, 161, 31))
		font = QtGui.QFont()
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(70, 190, 111, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(Form)
		self.label_3.setGeometry(QtCore.QRect(70, 250, 101, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(Form)
		self.label_4.setGeometry(QtCore.QRect(70, 130, 91, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(Form)
		self.label_5.setGeometry(QtCore.QRect(80, 370, 101, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.lineEdit = QtWidgets.QLineEdit(Form)
		self.lineEdit.setGeometry(QtCore.QRect(220, 130, 251, 31))
		self.lineEdit.setText("")
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit_2 = QtWidgets.QLineEdit(Form)
		self.lineEdit_2.setGeometry(QtCore.QRect(220, 190, 251, 31))
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_3 = QtWidgets.QLineEdit(Form)
		self.lineEdit_3.setGeometry(QtCore.QRect(220, 250, 251, 31))
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_4 = QtWidgets.QLineEdit(Form)
		self.lineEdit_4.setGeometry(QtCore.QRect(220, 310, 251, 31))
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.label_6 = QtWidgets.QLabel(Form)
		self.label_6.setGeometry(QtCore.QRect(70, 310, 101, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.line = QtWidgets.QFrame(Form)
		self.line.setGeometry(QtCore.QRect(20, 60, 501, 20))
		self.line.setFrameShape(QtWidgets.QFrame.HLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.lineEdit_5 = QtWidgets.QLineEdit(Form)
		self.lineEdit_5.setGeometry(QtCore.QRect(220, 370, 251, 31))
		self.lineEdit_5.setObjectName("lineEdit_5")
		self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(200, 450, 151, 41))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.pushButton.setFont(font)
		self.pushButton.setObjectName("pushButton")
		
		self.pushButton.clicked.connect(self.signup)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.label.setText(_translate("Form", "Sign Up Form"))
		self.label_2.setText(_translate("Form", "Full Name"))
		self.label_3.setText(_translate("Form", "Email Id"))
		self.label_4.setText(_translate("Form", "Username"))
		self.label_5.setText(_translate("Form", "Password"))
		self.label_6.setText(_translate("Form", "Contact No."))
		self.pushButton.setText(_translate("Form", "SIGN UP"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	Form = QtWidgets.QWidget()
	ui = Ui_Form_2()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

