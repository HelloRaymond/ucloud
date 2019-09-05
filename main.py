from ucloud import UHost_api, FireWalls_api
from PyQt5 import QtWidgets, QtGui, QtCore
import json, sys
from UI import Ui_network,Ui_messagebox,Ui_main,Ui_reinstall,Ui_uhost

def firewall_set_event():
    PublicKey = ui_network.lineEdit_pubkey.text()
    PrivateKey = ui_network.lineEdit_pvtkey.text()
    uc_hk = FireWalls_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            fdid = ui_network.cbx_list.currentText().split(":")[-1]
            if uc_hk.GrantFirewall(fdid) == 0:
                ui_messagebox.label.setText("设置成功！")
                NetworkWindow.close()
                MessageBox.show()
            else:
                ui_messagebox.label.setText("设置失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("设置失败！\n请尝试更新列表")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()
def firewall_update_event():
    PublicKey = ui_network.lineEdit_pubkey.text()
    PrivateKey = ui_network.lineEdit_pvtkey.text()
    uc_hk = FireWalls_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            response = uc_hk.DescribeFirewall()
            ui_network.cbx_list.clear()
            if response["RetCode"] == 0:
                ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
                ui_messagebox.label.setText("更新成功！")
                MessageBox.show()
                for i in response["DataSet"]:
                    ui_network.cbx_list.addItem(":".join([i["Name"],i["FWId"]]))
            else:
                ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
                ui_messagebox.label.setText("更新失败！")
                ui_network.cbx_list.addItem("获取列表失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("更新失败！\n网络出现异常")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()
def enter_host_event():
    MainWindow.close()
    HostWindow.show()
def enter_network_event():
    MainWindow.close()
    NetworkWindow.show()
def enter_reinstall_event():
    ReinstallWindow.show()
def host_update_event():
    PublicKey = ui_host.lineEdit_pubkey.text()
    PrivateKey = ui_host.lineEdit_pvtkey.text()
    uc_hk = UHost_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            response = uc_hk.DescribeUHostInstance()
            ui_host.cbx_hostlist.clear()
            if response["RetCode"] == 0:
                # ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
                # ui_messagebox.label.setText("更新成功！")
                # MessageBox.show()
                for i in response["UHostSet"]:
                    ui_host.cbx_hostlist.addItem(":".join([i["Name"],i["UHostId"]]))
            else:
                ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
                ui_messagebox.label.setText("更新失败！")
                ui_host.cbx_hostlist.addItem("获取列表失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("获取列表失败！\n网络出现异常")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()
def image_update_event():
    PublicKey = ui_host.lineEdit_pubkey.text()
    PrivateKey = ui_host.lineEdit_pvtkey.text()
    uc_hk = UHost_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            response = uc_hk.DescribeImage()
            ui_reinstall.cbx_imglist.clear()
            if response["RetCode"] == 0:
                # ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
                # ui_messagebox.label.setText("更新成功！")
                # MessageBox.show()
                for i in response["ImageSet"]:
                    ui_reinstall.cbx_imglist.addItem(":".join([i["ImageName"],i["ImageId"]]))
            else:
                ui_messagebox.label.setStyleSheet("font: 14pt \"黑体\";")
                ui_messagebox.label.setText("更新失败！")
                ui_reinstall.cbx_imglist.addItem("获取列表失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("获取列表失败！\n网络出现异常")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()
def host_start_event():
    PublicKey = ui_host.lineEdit_pubkey.text()
    PrivateKey = ui_host.lineEdit_pvtkey.text()
    uc_hk = UHost_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            HostId = ui_host.cbx_hostlist.currentText().split(":")[-1]
            if uc_hk.StartUHostInstance(HostId) == 0:
                ui_messagebox.label.setText("开机成功！")
                MessageBox.show()
            else:
                ui_messagebox.label.setText("开机失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("开机失败！\n请尝试更新列表")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()
def host_stop_event():
    PublicKey = ui_host.lineEdit_pubkey.text()
    PrivateKey = ui_host.lineEdit_pvtkey.text()
    uc_hk = UHost_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            HostId = ui_host.cbx_hostlist.currentText().split(":")[-1]
            if uc_hk.StopUHostInstance(HostId) == 0:
                ui_messagebox.label.setText("关机成功！")
                MessageBox.show()
            else:
                ui_messagebox.label.setText("关机失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("关机失败！\n请尝试更新列表")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()
def host_reboot_event():
    PublicKey = ui_host.lineEdit_pubkey.text()
    PrivateKey = ui_host.lineEdit_pvtkey.text()
    uc_hk = UHost_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            HostId = ui_host.cbx_hostlist.currentText().split(":")[-1]
            if uc_hk.RebootUHostInstance(HostId) == 0:
                ui_messagebox.label.setText("重启成功！")
                MessageBox.show()
            else:
                ui_messagebox.label.setText("重启失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("重启失败！\n请尝试更新列表")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()
def host_poweroff_event():
    PublicKey = ui_host.lineEdit_pubkey.text()
    PrivateKey = ui_host.lineEdit_pvtkey.text()
    uc_hk = UHost_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            HostId = ui_host.cbx_hostlist.currentText().split(":")[-1]
            if uc_hk.PoweroffUHostInstance(HostId) == 0:
                ui_messagebox.label.setText("强制掉电成功！")
                MessageBox.show()
            else:
                ui_messagebox.label.setText("强制掉电失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("强制掉电失败！\n请尝试更新列表")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()
def host_reinstall_event():
    PublicKey = ui_host.lineEdit_pubkey.text()
    PrivateKey = ui_host.lineEdit_pvtkey.text()
    uc_hk = UHost_api(PublicKey,PrivateKey)
    if len(PublicKey + PrivateKey) != 128:
        ui_messagebox.label.setText("请输入正确的API Key！")
        MessageBox.show()
    else:
        try:
            HostId = ui_host.cbx_hostlist.currentText().split(":")[-1]
            ImageID = ui_reinstall.cbx_imglist.currentText().split(":")[-1]
            if uc_hk.ReinstallUHostInstance(HostId,ImageID) == 0:
                ui_messagebox.label.setText("重装成功！")
                ReinstallWindow.close()
                MessageBox.show()
            else:
                ui_messagebox.label.setText("重装失败！")
                MessageBox.show()
        except Exception as e:
                print(e)
                ui_messagebox.label.setText("重装失败！\n请尝试更新列表")
                ui_messagebox.label.setStyleSheet("font: 12pt \"黑体\";")
                MessageBox.show()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
# 提示窗口
    MessageBox = QtWidgets.QDialog()
    MessageBox.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui_messagebox = Ui_messagebox.Ui_Dialog()
    ui_messagebox.setupUi(MessageBox)
# 网络设置窗口
    NetworkWindow = QtWidgets.QMainWindow()
    NetworkWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui_network = Ui_network.Ui_MainWindow()
    ui_network.setupUi(NetworkWindow)
# 主机设置窗口
    HostWindow = QtWidgets.QMainWindow()
    HostWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui_host = Ui_uhost.Ui_MainWindow()
    ui_host.setupUi(HostWindow)
# 重装设置窗口
    ReinstallWindow = QtWidgets.QMainWindow()
    ReinstallWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui_reinstall = Ui_reinstall.Ui_MainWindow()
    ui_reinstall.setupUi(ReinstallWindow)
# 主窗口
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui_main = Ui_main.Ui_MainWindow()
    ui_main.setupUi(MainWindow)

# 槽函数定义
    ui_network.pushButton.clicked.connect(firewall_set_event)
    ui_network.btn_update.clicked.connect(firewall_update_event)
    ui_main.btn_host.clicked.connect(enter_host_event)
    ui_main.btn_network.clicked.connect(enter_network_event)
    ui_host.btn_reinstall.clicked.connect(enter_reinstall_event)
    ui_host.btn_updatelist.clicked.connect(host_update_event)
    ui_host.btn_poweron.clicked.connect(host_start_event)
    ui_host.btn_poweroff.clicked.connect(host_poweroff_event)
    ui_host.btn_reboot.clicked.connect(host_reboot_event)
    ui_host.btn_shutdown.clicked.connect(host_stop_event)
    # ui_host.cbx_hostlist.highlighted.connect(host_update_event)
    # ui_reinstall.cbx_imglist.highlighted.connect(image_update_event)
    ui_reinstall.btn_reinstall.clicked.connect(host_reinstall_event)
    ui_reinstall.btn_update.clicked.connect(image_update_event)

    MainWindow.show()
    sys.exit(app.exec_())

