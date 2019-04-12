# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\selenium_driver_chrome\choosecourse_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_DPL_DeptName = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_DPL_DeptName.setGeometry(QtCore.QRect(70, 20, 201, 22))
        self.comboBox_DPL_DeptName.setObjectName("comboBox_DPL_DeptName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 41, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_DPL_Degree = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_DPL_Degree.setGeometry(QtCore.QRect(70, 50, 201, 22))
        self.comboBox_DPL_Degree.setObjectName("comboBox_DPL_Degree")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 460, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 460, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 470, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(40, 90, 256, 361))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(380, 50, 271, 401))
        self.listView_2.setObjectName("listView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
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
        self.label.setText(_translate("MainWindow", "系別 : "))
        self.label_2.setText(_translate("MainWindow", "年級 :"))
        self.pushButton.setText(_translate("MainWindow", "新增 >"))
        self.pushButton_2.setText(_translate("MainWindow", "< 刪除"))
        self.pushButton_3.setText(_translate("MainWindow", "開始"))

