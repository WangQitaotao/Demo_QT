import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QPushButton, QMessageBox


class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi(r"N:\Dmoe_QT\ui\request.ui")
        self.ui.buttonRequest.clicked.connect(self.sendRequest)

    def sendRequest(self):
        method = self.ui.boxMethod.currentText()
        url = self.ui.editURL.text()
        body = self.ui.widgetBody.item(1, 1)
        header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,en-GB;q=0.5',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'webreg=nfnuhaf6k405ekv1t6593qa6kduul6ac',  # 注意这里需要替换为您实际的Cookie值
        'Host': 'cekbpom.pom.go.id',
        'Origin': 'https://cekbpom.pom.go.id',
        'Referer': 'https://cekbpom.pom.go.id/kosmetika',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
        }
        proxies = {
            "http": None,
            "https": None,
        }
        try:
            print(body)
            if method == "post":
                response = requests.post(url=url, data=body, headers=header, proxies=proxies)
            elif method == "get":
                response = requests.get(url=url, data=body, headers=header, proxies=proxies)
            print("Button clicked!")
        except Exception as e:
            print(e)

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()

