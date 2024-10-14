import requests
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Stats():
    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi(r"N:\Dmoe_QT\ui\request.ui")

        # 绑定按钮点击事件
        self.ui.buttonRequest.clicked.connect(self.sendRequest)
        self.ui.buttonAdd.clicked.connect(self.add_row)
        self.ui.buttonRemove.clicked.connect(self.remove_row)
        self.ui.buttonClean.clicked.connect(self.clear_browser_input)
        # 设置header字段的行和列
        # self.ui.widgetHeader.setRowHeight(0, 60)
        self.ui.widgetHeader.setColumnWidth(0, 120)
        self.ui.widgetHeader.setColumnWidth(1, 193)

    def get_table_header(self):
        """ 从 QTableWidget 中提取数据，并将其转换为表单编码格式
        实例数据：
        'field_0_0': 'Value 1',
        'field_0_1': 'Value 2',
        'field_1_0': 'Value 3',
        'field_1_1': 'Value 4'
        """
        body_data = {}
        row_count = self.ui.widgetHeader.rowCount()   # 行
        col_count = self.ui.widgetHeader.columnCount()    # 列
        # 遍历列中的每对字段名和字段值
        for row in range(row_count):
            key_item = self.ui.widgetHeader.item(row, 0)
            value_item = self.ui.widgetHeader.item(row, 1)
            if key_item:
                key = key_item.text()
                value = value_item.text() if value_item else ''  # 默认值为空字符串
                body_data[key] = value

        return body_data

    def sendRequest(self):
        """ 定义接口请求函数 """
        method = self.ui.boxMethod.currentText().lower()
        url = self.ui.editURL.text()
        headers = self.get_table_header()
        data = self.ui.editBody.toPlainText()
        proxies = {
            "http": None,
            "https": None,
        }
        print(method,url,headers,data)
        try:
            if method == "post":
                response = requests.post(url, data=data, headers=headers, proxies=proxies)
            elif method == "get":
                response = requests.get(url, headers=headers, proxies=proxies)
            else:
                print("Unsupported method")
                return
            # 打印响应内容或其他处理
            print("Response Status Code:", response.status_code)
            print("Response Text:", response.text)
            template = f"""
            -------- 发送请求 --------
            {method}  {url}
            {headers}

            {data}

            -------- 得到响应 --------
            {response.text}

            """
            self.ui.browserInput.setPlainText(template)

        except Exception as e:
            self.ui.browserInput.setPlainText(f"请求异常: {e}")
            print(f"Error occurred: {e}")

    def add_row(self):
        """增加一行从 QTableWidget"""
        row_count = self.ui.widgetHeader.rowCount()
        self.ui.widgetHeader.insertRow(row_count)

    def remove_row(self):
        """删除一行从 QTableWidget"""
        row_count = self.ui.widgetHeader.rowCount()
        if row_count > 0:
            self.ui.widgetHeader.removeRow(row_count - 1)

    def clear_browser_input(self):
        """ 清空 browserInput 的内容 """
        self.ui.browserInput.clear()


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("N:\Dmoe_QT\小鸭子图标.ico"))
    stats = Stats()
    stats.ui.show()
    app.exec_()
