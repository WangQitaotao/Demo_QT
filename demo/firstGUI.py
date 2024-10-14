import sys
from PyQt5.QtWidgets import QApplication, QWidget


# 创建QApplication类的实例
app = QApplication(sys.argv)
# 创建一个窗口
window = QWidget()
# 设置窗口的尺寸
window.resize(800, 500)
# 设置窗口的标题
window.setWindowTitle("Hello World")
# 显示窗口
window.show()
# 进入程序的主循环
sys.exit(app.exec_())
