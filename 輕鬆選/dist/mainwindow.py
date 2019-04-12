# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\selenium_driver_chrome\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_User = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_User.setGeometry(QtCore.QRect(120, 110, 201, 20))
        self.lineEdit_User.setObjectName("lineEdit_User")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 110, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 31, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setGeometry(QtCore.QRect(120, 140, 201, 20))
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 290, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_DPL = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_DPL.setGeometry(QtCore.QRect(120, 60, 201, 22))
        self.comboBox_DPL.setObjectName("comboBox_DPL")
        self.label_alert = QtWidgets.QLabel(self.centralwidget)
        self.label_alert.setGeometry(QtCore.QRect(120, 180, 201, 21))
        self.label_alert.setText("")
        self.label_alert.setObjectName("label_alert")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 210, 211, 51))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "帳號(學號) :"))
        self.label_2.setText(_translate("MainWindow", "密碼 :"))
        self.pushButton.setText(_translate("MainWindow", "登入"))
        self.label_3.setText(_translate("MainWindow", "第一次登入會先抓課程資訊，按登入後如果有跳兩個視窗出來不要動他們，等他們跑完"))

