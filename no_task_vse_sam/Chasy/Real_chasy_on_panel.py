from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys, time


class DigitalClock(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Digital Clock - powered by MX productions')  # надпись сверху
        self.setGeometry(400, 300, height, wide)  # размеры
        self.setWindowIcon(QtGui.QIcon('clock_img.jpg'))
        # описываем процесс
        self.initUI()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.current_time)
        self.timer.start(1000)

    def initUI(self):
        self.clock_screen = QLCDNumber(self)
        self.clock_screen.setStyleSheet("color : lightyellow; background-color : lightblue")
        self.clock_screen.setDigitCount(8)
        self.clock_screen.setGeometry(0, 0, height, wide)
        self.current_time()

    def current_time(self):
        current = time.strftime('%H:%M:%S')
        self.clock_screen.display(current)


if __name__ == '__main__':
    height, wide = map(int, input('Введите высоту и ширину окна через пробел: ').split())
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())
