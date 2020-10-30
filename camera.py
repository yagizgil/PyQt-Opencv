from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import cv2, qimage2ndarray, sys

class Camera(QWidget):
    c = cv2.VideoCapture(0)

    def __init__(self, m):
        super().__init__()
        self.m = m
        self.setUI()

    def setUI(self):
        h = QHBoxLayout()
        self.timer = QTimer()
        self.timer.timeout.connect(self.cam)

        self.l = QLabel()
        h.addWidget(self.l)

        self.setLayout(h)

    def start(self):
        self.timer.start(int(self.m.data["timer"]))

    def cam(self):
        _, frame = self.c.read()
        frame = cv2.cvtColor(frame, self.m.colors[self.m.data["color_filter"]])
        image = qimage2ndarray.array2qimage(frame)
        self.l.setPixmap(QPixmap.fromImage(image))
