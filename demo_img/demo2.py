from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import pyqtSignal, QObject
import re
import sys
import os
import time
from urllib.parse import urlparse, parse_qs
import requests
options_dict = {
    "": "最新壁纸",
    "36": "4K专区",
    "6": "美女模特",
    "30": "爱情美图",
    "9": "风景大片",
    "15": "小清新",
    "26": "动漫卡通",
    "11": "明星风尚",
    "14": "萌宠动物",
    "5": "游戏壁纸",
    "12": "汽车天下",
    "10": "炫酷时尚",
    "22": "军事天地",
    "16": "劲爆体育",
    "32": "纹理",
    "35": "文字控",
    "29": "月历壁纸",
    "7": "影视剧照",
    "13": "节日美图",
    "18": "BABY秀"
}


class GetIMGNeter:
    def __init__(self):
        # 加载UI文件
        self.ui = uic.loadUi(r"N:\Demo_QT\ui\get_img_neter.ui")
        self.ui.buttonStart.clicked.connect(self.get_img_parameter)
        self.ui.buttonPreview.clicked.connect(self.select_folder)

    def display_img(self):
        file_name = "http:\/\/p1.qhimg.com\/bdr\/__85\/t014a7301b00dad2a17.jpgg"
        html = f'''
        <div style="text-align: center;">
            <img src="{file_name}" width="300" height="200" />
        </div>
        '''
        self.ui.browserIMG.setHtml(html)

    def select_folder(self):
        # 打开文件夹选择对话框
        folder = QFileDialog.getExistingDirectory(self.ui, "选择文件夹")
        if folder:
            self.ui.editPath.setText(folder)  # 设置路径到文本框
            return folder

    def download_image(self, url, img_url, path, filename):
        """下载图片到本地"""
        parsed_url = urlparse(url)    # 解析获得cid参数
        query_params = parse_qs(parsed_url.query)
        cid = str(query_params.get('cid', [None])[0])
        if cid in options_dict:
            directory = path + f'\{options_dict[cid]}'
            file_path = os.path.join(directory, filename + '.jpg')
            if not os.path.exists(directory):   # 判断文件夹是否存在
                os.makedirs(directory)
            if os.path.exists(file_path):   # 判断图片是否存在
                print(f"该照片存在，跳过:   {file_path}")
            else:
                response = requests.get(img_url, stream=True, timeout=10)
                if response.status_code == 200:
                    with open(file_path, 'wb') as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    self.ui.browserLog.append(f"下载成功:   {file_path}")
                else:
                    print(f"下载失败:   {cid}")


    def get_img_parameter(self):
        """获取图片的参数，url中count表示照片数量"""
        try:
            img_url = "http://wallpaper.apc.360.cn/index.php?c=WallPaper&start=0&count=100&from=360chrome&a=getAppsByCategory&cid=36"
            img_number = self.ui.editNumber.text()
            img_type = self.ui.editType.currentText()
            img_path = self.ui.editPath.text()
            print(img_number,img_type,img_path)
            response = requests.get(img_url, timeout=10)
            if response.status_code == 200:
                    for data in response.json()['data']:
                        # print(f"图片名称：{data['utag']}")
                        # print(f"分辨率：{data['resolution']}")
                        # print(f"图片链接：{data['url']}")
                        if 'utag' not in data:
                            exclude_words = {'全部'}
                            pattern = re.compile(r'[\u4e00-\u9fff]+')
                            matches = pattern.findall(data['tag'])
                            filtered_matches = [match for match in matches if match not in exclude_words]
                            chinese_fields = ' '.join(filtered_matches)
                            self.download_image(img_url, data['url'], img_path,data['resolution'] + '_' + re.sub(r'[ <>:"/\\|?*]', '_', chinese_fields))
                            time.sleep(0.1)
                        else:
                            self.download_image(img_url, data['url'], img_path,data['resolution'] + '_' + re.sub(r'[ <>:"/\\|?*]', '_', data['utag']))
                            time.sleep(0.1)
            else:
                print(f"请求失败，状态码: {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"请求超时")
        except Exception as e:
            print(f"异常错误{e}")

if __name__ == "__main__":
    app = QApplication([])
    # app.setWindowIcon(QIcon("小鸭子图标.ico"))
    stats = GetIMGNeter()
    stats.ui.show()
    app.exec_()
