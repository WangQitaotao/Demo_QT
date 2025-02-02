import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
import concurrent.futures



class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi(r"N:\Demo_QT\ui\reptile.ui")
        # 绑定按钮点击事件
        self.ui.buttonStart.clicked.connect(self.request_parameter)
        self.ui.buttonBrowse.clicked.connect(self.select_folder)

    def request_parameter(self):
        url = self.ui.editURL.text()
        screen_condition = self.ui.boxScreen.currentText()  # 筛选条件
        screen_field = self.ui.editField.text()  # 筛选字段
        get_number = self.ui.editNumber.text()     # 抓取数量
        thread_number = self.ui.boxThread.value()  # 设置线程组
        file_path = self.select_folder()    # 存储路径
        # 执行程序

    def select_folder(self):
        # 打开文件夹选择对话框
        folder = QFileDialog.getExistingDirectory(self.ui, "选择文件夹")
        if folder:
            self.ui.editPath.setText(folder)  # 设置路径到文本框
            return folder


if __name__ == "__main__":
    app = QApplication([])
    # app.setWindowIcon(QIcon("N:\Dmoe_QT\小鸭子图标.ico"))
    stats = Stats()
    stats.ui.show()
    app.exec_()
