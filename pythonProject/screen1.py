# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_screen1(object):
    def setupUi(self, screen1):
        screen1.setObjectName("screen1")
        screen1.resize(800, 450)
        screen1.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.centralwidget = QtWidgets.QWidget(screen1)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1_1.setGeometry(QtCore.QRect(90, 320, 231, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1_1.setFont(font)
        self.pushButton1_1.setStyleSheet("background-color: rgb(149, 255, 120);")
        self.pushButton1_1.setObjectName("pushButton1_1")
        self.pushButton1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1_2.setGeometry(QtCore.QRect(500, 320, 231, 61))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1_2.setFont(font)
        self.pushButton1_2.setStyleSheet("background-color: rgb(149, 255, 120);")
        self.pushButton1_2.setObjectName("pushButton1_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 90, 791, 151))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        screen1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(screen1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        screen1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(screen1)
        self.statusbar.setObjectName("statusbar")
        screen1.setStatusBar(self.statusbar)

        self.retranslateUi(screen1)
        QtCore.QMetaObject.connectSlotsByName(screen1)

    def retranslateUi(self, screen1):
        _translate = QtCore.QCoreApplication.translate
        screen1.setWindowTitle(_translate("screen1", "MainWindow"))
        self.pushButton1_1.setText(_translate("screen1", "CÁC BỘ TRÚNG THƯỞNG"))
        self.pushButton1_2.setText(_translate("screen1", "XÁC XUẤT SỐ LÀ BÀI"))
        self.label.setText(_translate("screen1", "XÁC SUẤT RÚT BÀI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    screen1 = QtWidgets.QMainWindow()
    ui = Ui_screen1()
    ui.setupUi(screen1)
    screen1.show()
    sys.exit(app.exec_())
