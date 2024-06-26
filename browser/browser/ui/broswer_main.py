import sys

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow


class broswer_main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui= ui_Form()
        self.ui.setupUi(self)

        # 반복문으로 한 번에 버튼 연결 설정하기
        # if로 i== 1일 때는 pushButton 연결
        # for i in range(1, 6):

        self.ui.pushButton.pressed.connect(self.web_google)
        self.ui.pushButton_2.pressed.connect(self.web_Naver)
        self.ui.pushButton_3.pressed.connect(self.web_Daum)
        self.ui.pushButton_4.pressed.connect(self.web_Bing)
        self.ui.pushButton_5.pressed.connect(self.web_Zum)

    # def load_web(self):
        # 함수 하나로 여러 개의 버튼을 한 번에 연결하기
        # 긴 코드에서 버튼의 이름- 포털사이트 단어만 추출해서 변수에 할당하고 url 양식에 포함('http://'+name+'.com')
            # http://www.daum.net 주소 문제 해결하기
    #     for i in range(1, 6):
    #         if(i== 1):
    #             self.ui.webEngineView.setUrl(self.ui.pushButton.Qurl('http://google.com'))
    #         else:
    #             self.ui.webEngineView.setUrl((self.ui.pushButton_i.Qurl('http://')))

    def web_google(self):
        self.ui.webEngineView.setUrl(QUrl('http://www.google.com'))
    def web_Naver(self):
        self.ui.webEngineView.setUrl(QUrl('http://www.naver.com'))
    def web_Daum(self):
        self.ui.webEngineView.setUrl(QUrl('http://www.daum.net'))
    def web_Bing(self):
        self.ui.webEngineView.setUrl(QUrl('http://www.bing.com'))
    def web_Zum(self):
        self.ui.webEngineView.setUrl(QUrl('http://www.zum.com'))

if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    window = broswer_main()
    window.show()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
