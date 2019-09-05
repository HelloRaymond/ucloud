# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\开发\uc\UI\reinstall.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 214)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_reinstall = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reinstall.setGeometry(QtCore.QRect(50, 140, 93, 28))
        self.btn_reinstall.setObjectName("btn_reinstall")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(180, 140, 93, 28))
        self.btn_cancel.setObjectName("btn_cancel")
        self.label_titlename = QtWidgets.QLabel(self.centralwidget)
        self.label_titlename.setGeometry(QtCore.QRect(100, 30, 121, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_titlename.setFont(font)
        self.label_titlename.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titlename.setObjectName("label_titlename")
        self.label_listname = QtWidgets.QLabel(self.centralwidget)
        self.label_listname.setGeometry(QtCore.QRect(50, 90, 72, 20))
        self.label_listname.setObjectName("label_listname")
        self.cbx_imglist = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_imglist.setGeometry(QtCore.QRect(120, 90, 131, 22))
        self.cbx_imglist.setObjectName("cbx_imglist")
        self.cbx_imglist.addItem("")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(260, 90, 21, 21))
        self.btn_update.setStyleSheet("background-image: url(:/images/update_64px.png);\n"
"background-attachment: fixed;\n"
"background-origin:content-box;\n"
"")
        self.btn_update.setText("")
        self.btn_update.setObjectName("btn_update")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_cancel.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_reinstall.setText(_translate("MainWindow", "重装"))
        self.btn_cancel.setText(_translate("MainWindow", "取消"))
        self.label_titlename.setText(_translate("MainWindow", "重装系统"))
        self.label_listname.setText(_translate("MainWindow", "镜像列表："))
        self.cbx_imglist.setItemText(0, _translate("MainWindow", "Imagine"))

import UI.icons_rc
