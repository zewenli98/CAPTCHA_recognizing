#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys

class Ui_Form(QtWidgets.QWidget):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(490, 280)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 93, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 60, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 72, 21))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(360, 60, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../CAPTCHA_program/program/src/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QtCore.QSize(30, 16))
        self.toolButton_3.setObjectName("toolButton_3")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 120, 221, 33))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 180, 93, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(275, 250, 202, 15))
        self.label_4.setObjectName("label_4")
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(360, 120, 31, 31))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(30, 16))
        self.toolButton_4.setObjectName("toolButton_4")
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.lineEdit_2.clear)
        self.pushButton_2.clicked.connect(self.compare)  #
        self.toolButton_3.clicked.connect(self.openfile1)  #
        self.toolButton_4.clicked.connect(self.openfile2)  #

    def msg(self):
        self.box = QMessageBox()
        self.box.move(640, 290)
        self.box.information(self.box, "提示", "   请选择mappings文件路径！", QMessageBox.Ok)

    def msg_2(self):
        reply = QMessageBox.information(self, "提示", "有错误发生，请检查输入文件是否有误！", QMessageBox.Ok)

    def msg_result(self, ac):
        reply = QMessageBox.information(self, "完成", "比对完成，准确率为{}% 。".format(ac), QMessageBox.Ok)

    def predict(self):

        inroad = self.lineEdit.text()
        outroad = self.lineEdit_2.text()
        try:
            file = open(inroad)
            lines = file.readlines()
            file.close()

            file2 = open(outroad)
            lines2 = file2.readlines()
            file2.close()

            cnt = len(lines)
            cnt2 = len(lines2)

            right_count = 0
            for i in range(min(cnt, cnt2)):
                text = lines[i].split(",")[-1].strip()
                text2 = lines2[i].split(",")[-1].strip()

                if text == text2:
                    right_count += 1
                # print(text, " ", text2)
            # print("正确数：", right_count)
            self.msg_result('%.2f' % (right_count * 100.0 / cnt))

        except:
            self.msg_2()

    def compare(self):

        if (self.lineEdit.text() == "" or self.lineEdit_2.text() == ""):  # 输入输出路径是否为空
            self.msg()
        else:
            self.predict()

    def openfile1(self):
        filename, type = QFileDialog.getOpenFileName(self,
                  "选取文件",
                  "./",
                  "All Files (*.txt);;Text Files (*.txt)")
        self.lineEdit.setText(filename)


    def openfile2(self):
        filename, type = QFileDialog.getOpenFileName(self,
                  "选取文件",
                  "./",
                  "All Files (*.txt);;Text Files (*.txt)")
        self.lineEdit_2.setText(filename)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "中国大学生服务外包创新创业大赛"))
        Form.setWindowIcon(QtGui.QIcon('../CAPTCHA_program/program/src/qcom.jpg'))
        self.pushButton.setText(_translate("Form", "重置"))
        self.label_2.setText(_translate("Form", "预测文件"))
        self.toolButton_3.setText(_translate("Form", "..."))
        self.label_3.setText(_translate("Form", "标记文件"))
        self.pushButton_2.setText(_translate("Form", "确定"))
        self.label_4.setText(_translate("Form", "Developed By - 李说啥都对"))
        self.toolButton_4.setText(_translate("Form", "..."))
        self.toolButton_4.setStyleSheet("background: transparent")
        self.toolButton_3.setStyleSheet("background: transparent")


if __name__ == '__main__':

    fileroad = ""
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())