import asyncio
import json
import base64
import threading
import urllib.parse
import re
from Crypto.Cipher import AES
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal, QObject
import websockets


class Communicator(QObject):
    update_qian = pyqtSignal(str)
    update_hou = pyqtSignal(str)
    clear_widgets = pyqtSignal()


class Stats:
    def __init__(self):
        # 加载UI文件
        self.ui = uic.loadUi("decode_v2.ui")
        self.ui.buttonOpenWeb.clicked.connect(self.start_websocket_server_thread)
        self.ui.buttonStartDecode.clicked.connect(self.manual_decode)
        self.ui.buttonClear.clicked.connect(self.clear_information)
        # 创建信号和槽
        self.comm = Communicator()
        self.comm.update_qian.connect(self.ui.editDecode_qian.append)
        self.comm.update_hou.connect(self.ui.editDecode_hou.append)
        self.comm.clear_widgets.connect(self.clear_widgets)

        # 设置控件属性
        self.ui.buttonStartDecode.setFixedSize(100, 35)
        self.ui.buttonClear.setFixedSize(100, 35)

    def clear_widgets(self):
        """清空文本框内容"""
        self.ui.editDecode_qian.clear()
        self.ui.editDecode_hou.clear()

    def decrypt_url(self, url):
        """解密营销链接"""
        try:
            # 在主线程中清空内容
            self.comm.clear_widgets.emit()
            self.comm.update_qian.emit(f"{url}\n")
            base_data = base64.b64decode(url).decode('utf-8')
            key = "uJhXC7qm6qoju1kF".encode()
            cipher = AES.new(key, AES.MODE_ECB)
            aes_data = cipher.decrypt(base64.b64decode(base_data)).decode('utf-8')
            return urllib.parse.unquote(urllib.parse.unquote(aes_data))
        except:
            self.comm.update_hou.emit("解密失败！")
            return None

    async def handler(self, websocket, path):
        async for message in websocket:
            try:
                data = json.loads(message)
                title = data.get("title")
                url = data.get("url")

                # 在主线程中清空内容
                self.comm.clear_widgets.emit()

                if "https://www.diskpart.com" in url:
                    clean_text = re.sub(r'[\x00-\x1F\x7F]', '', self.decrypt_url(url.split("eurl=")[-1]))
                    if clean_text:
                        self.comm.update_hou.emit(f"{clean_text}\n")
                else:
                    self.comm.update_hou.emit("检测到是其他链接,暂不处理！")
            except json.JSONDecodeError:
                self.comm.update_hou.emit("无效的JSON消息")
            except Exception:
                self.comm.update_hou.emit("Exception 异常错误！")

    async def start_websocket_server(self):
        self.ui.editLog.append("-------------> 开启 WebSocket 服务 <-------------")
        start_server = websockets.serve(self.handler, "localhost", 8080)
        self.ui.editLog.append("""
        成功开启服务...
        
        记得去浏览器管理扩展界面手动刷新 Page Watcher 插件！""")
        await start_server  # 保持服务器运行
        await asyncio.Future()  # 持续运行，直到被停止

    def start_websocket_server_thread(self):
        self.ui.buttonOpenWeb.setEnabled(False)     # 点击按钮后就禁用该按钮
        server_thread = threading.Thread(target=self.run_async_server)
        server_thread.daemon = True  # 确保主程序退出时线程也会退出
        server_thread.start()

    def run_async_server(self):
        # 创建新的事件循环并设置为当前线程的事件循环
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.start_websocket_server())

    def manual_decode(self):
        """手动解码"""
        try:
            url = self.ui.editManualDecode_qian.toPlainText()
            if "https://www.diskpart.com" in url:
                base_data = base64.b64decode((url.split("eurl="))[1]).decode('utf-8')
                key = "uJhXC7qm6qoju1kF".encode()
                cipher = AES.new(key, AES.MODE_ECB)
                aes_data = cipher.decrypt(base64.b64decode(base_data)).decode('utf-8')
                decrypt_url = urllib.parse.unquote(urllib.parse.unquote(aes_data))
                clean_text = re.sub(r'[\x00-\x1F\x7F]', '', decrypt_url)
                self.ui.editManualDecode_hou.append(clean_text)
        except Exception as e:
            self.ui.editManualDecode_hou.append(e)

    def clear_information(self):
        self.ui.editManualDecode_qian.clear()
        self.ui.editManualDecode_hou.clear()


if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("小鸭子图标.ico"))
    stats = Stats()
    stats.ui.show()
    app.exec_()
