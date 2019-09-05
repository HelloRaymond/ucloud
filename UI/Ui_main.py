# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\开发\uc\UI\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 185)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titlename = QtWidgets.QLabel(self.centralwidget)
        self.label_titlename.setGeometry(QtCore.QRect(90, 30, 181, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_titlename.setFont(font)
        self.label_titlename.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titlename.setObjectName("label_titlename")
        self.btn_host = QtWidgets.QPushButton(self.centralwidget)
        self.btn_host.setGeometry(QtCore.QRect(60, 110, 93, 28))
        self.btn_host.setObjectName("btn_host")
        self.btn_network = QtWidgets.QPushButton(self.centralwidget)
        self.btn_network.setGeometry(QtCore.QRect(200, 110, 93, 28))
        self.btn_network.setObjectName("btn_network")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titlename.setText(_translate("MainWindow", "UCloud\n"
"主机设置小工具"))
        self.btn_host.setText(_translate("MainWindow", "主机"))
        self.btn_network.setText(_translate("MainWindow", "网络"))

