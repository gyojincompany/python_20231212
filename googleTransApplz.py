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

        self.transButton.clicked.connect(self.transFunction)
        self.resetButton.clicked.connect(self.resetFunction)

    def transFunction(self):
        trans = googletrans.Translator()  # 구글 번역객체 생성
        trans_kor = self.inputEdit.text()  # 사용자가 입력한 텍스트(한글)를 가져옴

        result_eng = trans.translate(trans_kor, dest='en')  # 영어로 번역
        result_jap = trans.translate(trans_kor, dest='ja')  # 일어로 번역
        result_chn = trans.translate(trans_kor, dest='zh-cn')  # 중국어로 번역

        self.engOutput.append(result_eng.text)
        self.japOutput.append(result_jap.text)
        self.chnOutput.append(result_chn.text)

    def resetFunction(self):
        self.inputEdit.clear()



app = QApplication(sys.argv)
myProgram = MyGoogleTrans()
myProgram.show()
app.exec_() # 무한루프