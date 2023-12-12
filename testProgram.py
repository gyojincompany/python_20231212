import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/testui.ui")[0] # QT Designer에서 제작한 ui 불러오기

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self) # ui불러오기

        self.setWindowTitle("연습프로그램 v1.0") # 프로그램 윈도우 제목
        self.setWindowIcon(QIcon(""))

        self.pushButton.clicked.connect(self.btnClick) # 시그널
        self.clearButton.clicked.connect(self.clearClick) # 시그널

    def btnClick(self): # 슬롯
        self.lineEdit.setText("안녕하세요!") # lineEdit에 텍스트 출력하기

    def clearClick(self): #슬롯
        self.lineEdit.clear() # lineEdit에 입력된 텍스트 삭제


app = QApplication(sys.argv)
myProgram = MyWindow()
myProgram.show()
app.exec_() # 무한루프