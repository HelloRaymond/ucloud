# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\开发\uc\UI\uhost.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(70, 0, 291, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_listname = QtWidgets.QLabel(self.centralwidget)
        self.label_listname.setGeometry(QtCore.QRect(70, 140, 72, 21))
        self.label_listname.setObjectName("label_listname")
        self.cbx_hostlist = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_hostlist.setGeometry(QtCore.QRect(150, 140, 181, 22))
        self.cbx_hostlist.setObjectName("cbx_hostlist")
        self.cbx_hostlist.addItem("")
        self.btn_updatelist = QtWidgets.QPushButton(self.centralwidget)
        self.btn_updatelist.setGeometry(QtCore.QRect(340, 140, 22, 22))
        self.btn_updatelist.setStyleSheet("background-image: url(:/images/update_64px.png);\n"
"background-attachment: fixed;\n"
"background-origin:content-box;\n"
"")
        self.btn_updatelist.setText("")
        self.btn_updatelist.setObjectName("btn_updatelist")
        self.btn_shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.btn_shutdown.setGeometry(QtCore.QRect(71, 181, 93, 28))
        self.btn_shutdown.setObjectName("btn_shutdown")
        self.btn_reboot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reboot.setGeometry(QtCore.QRect(171, 181, 93, 28))
        self.btn_reboot.setObjectName("btn_reboot")
        self.btn_poweroff = QtWidgets.QPushButton(self.centralwidget)
        self.btn_poweroff.setGeometry(QtCore.QRect(171, 221, 93, 28))
        self.btn_poweroff.setObjectName("btn_poweroff")
        self.btn_poweron = QtWidgets.QPushButton(self.centralwidget)
        self.btn_poweron.setGeometry(QtCore.QRect(71, 221, 93, 28))
        self.btn_poweron.setObjectName("btn_poweron")
        self.btn_reinstall = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reinstall.setGeometry(QtCore.QRect(271, 181, 93, 28))
        self.btn_reinstall.setObjectName("btn_reinstall")
        self.lineEdit_pubkey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pubkey.setGeometry(QtCore.QRect(120, 80, 241, 21))
        self.lineEdit_pubkey.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_pubkey.setObjectName("lineEdit_pubkey")
        self.lineEdit_pvtkey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pvtkey.setGeometry(QtCore.QRect(120, 110, 241, 21))
        self.lineEdit_pvtkey.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pvtkey.setObjectName("lineEdit_pvtkey")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 72, 15))
        self.label_2.setObjectName("label_2")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(271, 221, 93, 28))
        self.btn_exit.setObjectName("btn_exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "云主机设置"))
        self.label_listname.setText(_translate("MainWindow", "主机列表："))
        self.cbx_hostlist.setItemText(0, _translate("MainWindow", "UHost"))
        self.btn_shutdown.setText(_translate("MainWindow", "关机"))
        self.btn_reboot.setText(_translate("MainWindow", "重启"))
        self.btn_poweroff.setText(_translate("MainWindow", "强制掉电"))
        self.btn_poweron.setText(_translate("MainWindow", "开机"))
        self.btn_reinstall.setText(_translate("MainWindow", "重装系统"))
        self.label.setText(_translate("MainWindow", "公钥："))
        self.label_2.setText(_translate("MainWindow", "私钥："))
        self.btn_exit.setText(_translate("MainWindow", "退出"))

import UI.icons_rc
