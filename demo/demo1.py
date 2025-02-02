from PyQt5.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QPushButton, QMessageBox


# 定义一个函数
def handleCalc():
    info = textEdit.toPlainText()
    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name,salary,age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window,
                '统计结果',
                f'''薪资20000 以上的有：\n{salary_above_20k}
                \n薪资20000 以下的有：\n{salary_below_20k}'''
                )

# 实例化对象
app = QApplication([])

# 创建一个窗口对象
window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('薪资统计')

# 创建一个子窗口对象
textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入薪资表")
textEdit.move(10, 25)
textEdit.resize(300, 350)

# 创建一个按钮
button = QPushButton('统计', window)
button.move(380, 80)
button.clicked.connect(handleCalc)

# 显示在界面并运行
window.show()
app.exec() # PySide6 是 exec 而不是 exec_
