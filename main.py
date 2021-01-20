### maryshca (c)

import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.setText("press")
        self.pushButton.clicked.connect(self.run)
        self.drawing = False
        self.canvas.setText("")
        self.pixmap = QPixmap(self.canvas.width(), self.canvas.height())
        self.canvas.setPixmap(self.pixmap)

    def run(self):
        self.drawing = True
        self.repaint()
        self.drawing = False

    def paintEvent(self, event):
        if self.drawing:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self.pixmap)
            self.draw_circle(qp)
            # Завершаем рисование
            qp.end()
            self.canvas.setPixmap(self.pixmap)

    def draw_circle(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 250, 0))
        # Рисуем прямоугольник заданной кистью
        r = randint(0, 100)
        x, y = randint(0, self.canvas.width() - r), randint(0, self.canvas.height() - r)
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())




