# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\开发\uc\UI\network.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 244)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 207, 51))
        self.label.setStyleSheet("font: 75 16pt \"微软雅黑\";")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(91, 191, 100, 28))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_pubkey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pubkey.setGeometry(QtCore.QRect(120, 70, 261, 21))
        self.lineEdit_pubkey.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_pubkey.setObjectName("lineEdit_pubkey")
        self.lineEdit_pvtkey = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pvtkey.setGeometry(QtCore.QRect(120, 110, 261, 21))
        self.lineEdit_pvtkey.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pvtkey.setObjectName("lineEdit_pvtkey")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 72, 15))
        self.label_3.setObjectName("label_3")
        self.cbx_list = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_list.setGeometry(QtCore.QRect(50, 150, 301, 21))
        self.cbx_list.setObjectName("cbx_list")
        self.cbx_list.addItem("")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(360, 150, 21, 21))
        self.btn_update.setStyleSheet("background-image: url(:/images/update_64px.png);\n"
"background-attachment: fixed;\n"
"background-origin:content-box;\n"
"")
        self.btn_update.setText("")
        self.btn_update.setObjectName("btn_update")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(238, 191, 100, 28))
        self.btn_exit.setObjectName("btn_exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Firewalls"))
        self.label.setText(_translate("MainWindow", "防火墙设置"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label_2.setText(_translate("MainWindow", "API公钥："))
        self.label_3.setText(_translate("MainWindow", "API私钥："))
        self.cbx_list.setItemText(0, _translate("MainWindow", "防火墙列表"))
        self.btn_exit.setText(_translate("MainWindow", "退出"))

import UI.icons_rc
