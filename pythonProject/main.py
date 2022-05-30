import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore
from screen1 import Ui_screen1
from screen2 import Ui_screen2
from screen3 import Ui_screen3
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_screen1()
        self.uic.setupUi(self.main_win)
        self.uic.label.setAlignment(QtCore.Qt.AlignCenter)
        self.uic.pushButton1_1.clicked.connect(self.show2)
        self.uic.pushButton1_2.clicked.connect(self.show3)
        self.main_win.show()
    def show2(self):
        self.main_win = QMainWindow()
        self.uic = Ui_screen2()
        self.uic.setupUi(self.main_win)
        self.uic.pushButton2_1.clicked.connect(self.__init__)
        self.uic.tableWidget.setColumnWidth(0,500)
        self.uic.tableWidget.setColumnWidth(1, 150)
        self.main_win.show()
    def show3(self):
        self.main_win = QMainWindow()
        self.uic = Ui_screen3()
        self.uic.setupUi(self.main_win)
        self.uic.table1.setColumnWidth(0,350)
        self.uic.table1.setColumnWidth(1, 300)
        self.uic.table1_2.setColumnWidth(0,350)
        self.uic.table1_2.setColumnWidth(1, 300)
        self.uic.table1_3.setColumnWidth(0, 350)
        self.uic.table1_3.setColumnWidth(1, 300)
        self.uic.pushButton3_1.clicked.connect(self.__init__)
        self.main_win.show()
    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())