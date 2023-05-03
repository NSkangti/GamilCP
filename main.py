import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('자리 바꾸기 프로그램')
        self.setWindowIcon(QIcon('20220822_221353.png'))
        self.setGeometry(300,300,300,300)
        self.resize(1080,540)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())