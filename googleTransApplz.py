import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import googletrans

form_class = uic.loadUiType("ui/googleUi.ui")[0]

class MyGoogleTrans(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)  # ui불러오기

        self.setWindowTitle("구글번역기 v1.0")  # 프로그램 윈도우 제목
        self.setWindowIcon(QIcon("icon/google.png"))
        self.statusBar().showMessage("Google Trans Applz v1.0 Copyrightⓒ 2023")

app = QApplication(sys.argv)
myProgram = MyGoogleTrans()
myProgram.show()
app.exec_() # 무한루프