from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import cv2, qimage2ndarray, sys
import requests as rq
import numpy as np

class Camera(QWidget):
    url = ""
    w = 640
    h = 480
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

    def start(self, url, w, h):
        self.url = url
        self.w = w
        self.h = h
        self.timer.start(int(self.m.data["timer"]))
    
    def set_timer(self,v):
        self.timer.setInterval(int(v))
        
    def set_re(self,w,h):
        self.w = w
        self.h = h
    
    def cam(self):
        w = self.w
        h = self.h
        i_response = rq.get(self.url)
        i_array = np.array(bytearray(i_response.content), dtype=np.uint8)
        frame = cv2.imdecode(i_array, cv2.IMREAD_COLOR)
        frame = cv2.resize(frame, (w,h))
        frame = cv2.cvtColor(frame, self.m.colors[self.m.data["color_filter"]])
        image = qimage2ndarray.array2qimage(frame)
        self.l.setPixmap(QPixmap.fromImage(image))
