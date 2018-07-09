# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from predict import batch_hack_captcha
from predict_2 import batch_hack_captcha_2
from predict_3 import batch_hack_captcha_3
from predict_4 import batch_hack_captcha_4
from predict_5 import batch_hack_captcha_5
from PyQt5.QtCore import *
import sys, time

global thread
thread = 0
class MainWindow(QtWidgets.QMainWindow):

    def closeEvent(self, a0: QtGui.QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self,
                                               '提示',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit(0)
        else:
            a0.ignore()


class MyThread(QThread):

    update = QtCore.pyqtSignal(str)

    def run(self):
        time.sleep(1)
        self.update.emit("")

class MyThread_2(QThread):

    update = QtCore.pyqtSignal(str)

    def run(self):
        time.sleep(1)
        self.update.emit("")

class MyThread_3(QThread):

    update = QtCore.pyqtSignal(str)

    def run(self):
        time.sleep(1)
        self.update.emit("")

class MyThread_4(QThread):

    update = QtCore.pyqtSignal(str)

    def run(self):
        time.sleep(1)
        self.update.emit("")

class MyThread_5(QThread):

    update = QtCore.pyqtSignal(str)

    def run(self):
        time.sleep(1)
        self.update.emit("")

class Ui_Form(QtWidgets.QWidget):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(640, 614)
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 290, 115, 19))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 340, 93, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(330, 230, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 190, 72, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 260, 115, 19))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(520, 230, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../CAPTCHA_program/program/src/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QtCore.QSize(30, 16))
        self.toolButton_3.setObjectName("toolButton_3")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(110, 230, 115, 19))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setGeometry(QtCore.QRect(110, 350, 115, 19))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(230, 290, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 290, 221, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 340, 93, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 400, 601, 161))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(110, 320, 115, 19))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(420, 580, 202, 15))
        self.label_4.setObjectName("label_4")
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(520, 290, 31, 31))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(30, 16))
        self.toolButton_4.setObjectName("toolButton_4")
        self.label_5 = QtWidgets.QLabel(Form)
        png = QtGui.QPixmap('../CAPTCHA_program/program/src/header.jpg')
        self.label_5.setPixmap(png)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 640, 172))


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.textEdit.clear)

        # self.pushButton_2.clicked.connect(self.test)  #
        self.pushButton_2.clicked.connect(self.model)  #
        self.toolButton_3.clicked.connect(self.openfile1)  #
        self.toolButton_4.clicked.connect(self.openfile2)  #

    def model(self): #模型接口

        if (self.lineEdit.text() == "" or self.lineEdit_2.text() == ""):  # 输入输出路径是否为空
            self.textEdit.append("未选择数据路径或输出路径！")
        else:
            inroad = self.lineEdit.text()                             # 测试数据
            outroad = self.lineEdit_2.text() + "/mappings.txt"        # 输出文件 mappings.txt

            if (self.radioButton.isChecked()):

                self.textEdit.append("正在验证第一类，请稍候。。。^_^")
                self.thread = MyThread()
                self.thread.update.connect(self.test)
                self.thread.start()

            elif (self.radioButton_2.isChecked()):

                self.textEdit.append("正在验证第二类，请稍候。。。^_^")
                self.thread = MyThread_2()
                self.thread.update.connect(self.test_2)
                self.thread.start()

            elif (self.radioButton_3.isChecked()):

                self.textEdit.append("正在验证第三类，请稍候。。。^_^")
                self.thread = MyThread_3()
                self.thread.update.connect(self.test_3)
                self.thread.start()


            elif (self.radioButton_4.isChecked()):

                self.textEdit.append("正在验证第四类，请稍候。。。^_^")
                self.thread = MyThread_4()
                self.thread.update.connect(self.test_4)
                self.thread.start()

            elif (self.radioButton_5.isChecked()):

                self.textEdit.append("正在验证第五类，请稍候。。。^_^")
                self.thread = MyThread_5()
                self.thread.update.connect(self.test_5)
                self.thread.start()

            else:
                self.textEdit.append("未选中测试类型！")

    def msg(self, ty):
        self.box = QMessageBox()
        self.box.move(640, 290)
        self.box.information(self.box, "完成", "第{}类预测完成！".format(ty), QMessageBox.Ok)
        sys.exit(app.exec_())

    def msg_error(self):
        self.box = QMessageBox()
        self.box.move(640, 290)
        self.box.information(self.box, "提示", " 有错误发生，请检查输入文件是否有误！", QMessageBox.Ok)
        sys.exit(app.exec_())

    def test(self, text):

        inroad = self.lineEdit.text()  # 测试数据
        outroad = self.lineEdit_2.text() + "/mappings.txt"
        count = 0
        for fn in os.listdir(inroad):  # fn 表示的是文件名
             count += 1
        self.textEdit.append(text)
        ac = batch_hack_captcha(inroad, outroad)
        if ac != -1:
            self.textEdit.append("测试完成，共测试{}个数据。\n".format(count))
            self.msg("一")
        else:
            self.textEdit.append("发生错误！")
            self.msg_error()


    def test_2(self, text):
        inroad = self.lineEdit.text()  # 测试数据
        outroad = self.lineEdit_2.text() + "/mappings.txt"
        count = 0
        for fn in os.listdir(inroad):  # fn 表示的是文件名
             count += 1
        self.textEdit.append(text)
        result = batch_hack_captcha_2(inroad, outroad)
        if result != -1:
            self.textEdit.append("测试完成，共测试{}个数据。\n".format(count))
            self.msg("二")
        else:
            self.textEdit.append("发生错误！")
            self.msg_error()

    def test_3(self, text):
        inroad = self.lineEdit.text()  # 测试数据
        outroad = self.lineEdit_2.text() + "/mappings.txt"
        count = 0
        for fn in os.listdir(inroad):  # fn 表示的是文件名
             count += 1
        self.textEdit.append(text)
        result = batch_hack_captcha_3(inroad, outroad)
        if result != -1:
            self.textEdit.append("测试完成，共测试{}个数据。\n".format(count))
            self.msg("三")
        else:
            self.textEdit.append("发生错误！")
            self.msg_error()

    def test_4(self, text):
        inroad = self.lineEdit.text()  # 测试数据
        outroad = self.lineEdit_2.text() + "/mappings.txt"
        count = 0
        for fn in os.listdir(inroad):  # fn 表示的是文件名
             count += 1
        self.textEdit.append(text)
        result = batch_hack_captcha_4(inroad, outroad)
        if result != -1:
            self.textEdit.append("测试完成，共测试{}个数据。\n".format(count))
            self.msg("四")
        else:
            self.textEdit.append("发生错误！")
            self.msg_error()


    def test_5(self, text):
        inroad = self.lineEdit.text()  # 测试数据
        outroad = self.lineEdit_2.text() + "/mappings.txt"
        count = 0
        for fn in os.listdir(inroad):  # fn 表示的是文件名
             count += 1
        self.textEdit.append(text)
        result = batch_hack_captcha_5(inroad, outroad)
        if result != -1:
            self.textEdit.append("测试完成，共测试{}个数据。\n".format(count))
            self.msg("五")
        else:
            self.textEdit.append("发生错误！")
            self.msg_error()


    def openfile1(self):    # 选择测试数据
        filename = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(filename)


    def openfile2(self):   # 选择输出路径
        filename = QFileDialog.getExistingDirectory()
        self.lineEdit_2.setText(filename)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "中国大学生服务外包创新创业大赛-A16验证码识别"))
        Form.setWindowIcon(QtGui.QIcon('../CAPTCHA_program/program/src/qcom.jpg'))
        self.radioButton_3.setText(_translate("Form", "第三类"))
        self.pushButton.setText(_translate("Form", "重置"))
        self.label.setText(_translate("Form", "测试类型"))
        self.label_2.setText(_translate("Form", "测试数据"))
        self.radioButton_2.setText(_translate("Form", "第二类"))
        self.toolButton_3.setText(_translate("Form", "..."))
        self.radioButton.setText(_translate("Form", "第一类"))
        self.radioButton_5.setText(_translate("Form", "第五类"))
        self.label_3.setText(_translate("Form", "输出地址"))
        self.pushButton_2.setText(_translate("Form", "确定"))
        self.radioButton_4.setText(_translate("Form", "第四类"))
        self.label_4.setText(_translate("Form", "Developed By - 李说啥都对"))
        self.toolButton_4.setText(_translate("Form", "..."))
        self.toolButton_4.setStyleSheet("background: transparent")
        self.toolButton_3.setStyleSheet("background: transparent")


if __name__ == '__main__':

    fileroad = ""
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    ui = Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
