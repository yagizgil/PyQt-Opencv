from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys, cv2
import camera as c


class Window(QMainWindow):
    data = {"timer":1,
            "color_filter":"COLOR_BGR2BGR555"}
    colors = {
            "COLOR_BGR2BGR555":cv2.COLOR_BGR2BGR555,
            "COLOR_BGR2BGR565":cv2.COLOR_BGR2BGR565,
            "COLOR_BGR2BGRA":cv2.COLOR_BGR2BGRA,
            "COLOR_BGR2GRAY":cv2.COLOR_BGR2GRAY,
            "COLOR_BGR2HLS":cv2.COLOR_BGR2HLS,
            "COLOR_BGR2HLS_FULL":cv2.COLOR_BGR2HLS_FULL,
            "COLOR_BGR2HSV":cv2.COLOR_BGR2HSV,
            "COLOR_BGR2HSV_FULL":cv2.COLOR_BGR2HSV_FULL,
            "COLOR_BGR2LAB":cv2.COLOR_BGR2LAB,
            "COLOR_BGR2LUV":cv2.COLOR_BGR2LUV,
            "COLOR_BGR2Lab":cv2.COLOR_BGR2Lab,
            "COLOR_BGR2Luv":cv2.COLOR_BGR2Luv,
            "COLOR_BGR2RGB":cv2.COLOR_BGR2RGB,
            "COLOR_BGR2RGBA":cv2.COLOR_BGR2RGBA,
            "COLOR_BGR2XYZ":cv2.COLOR_BGR2XYZ,
            "COLOR_BGR2YCR_CB":cv2.COLOR_BGR2YCR_CB,
            "COLOR_BGR2YCrCb":cv2.COLOR_BGR2YCrCb,
            "COLOR_BGR2YUV":cv2.COLOR_BGR2YUV,
            "COLOR_BGR2YUV_I420":cv2.COLOR_BGR2YUV_I420,
            "COLOR_BGR2YUV_IYUV":cv2.COLOR_BGR2YUV_IYUV,
            "COLOR_BGR2YUV_YV12":cv2.COLOR_BGR2YUV_YV12,
            "COLOR_BGRA2BGR":cv2.COLOR_BGRA2BGR,
            "COLOR_BGRA2BGR555":cv2.COLOR_BGRA2BGR555,
            "COLOR_BGRA2BGR565":cv2.COLOR_BGRA2BGR565,
            "COLOR_BGRA2GRAY":cv2.COLOR_BGRA2GRAY,
            "COLOR_BGRA2RGB":cv2.COLOR_BGRA2RGB,
            "COLOR_BGRA2RGBA":cv2.COLOR_BGRA2RGBA,
            "COLOR_BGRA2YUV_I420":cv2.COLOR_BGRA2YUV_I420,
            "COLOR_BGRA2YUV_IYUV":cv2.COLOR_BGRA2YUV_IYUV,
            "COLOR_BGRA2YUV_YV12":cv2.COLOR_BGRA2YUV_YV12,
            "COLOR_HLS2BGR":cv2.COLOR_HLS2BGR,
            "COLOR_HLS2BGR_FULL":cv2.COLOR_HLS2BGR_FULL,
            "COLOR_HLS2RGB":cv2.COLOR_HLS2RGB,
            "COLOR_HLS2RGB_FULL":cv2.COLOR_HLS2RGB_FULL,
            "COLOR_HSV2BGR":cv2.COLOR_HSV2BGR,
            "COLOR_HSV2BGR_FULL":cv2.COLOR_HSV2BGR_FULL,
            "COLOR_HSV2RGB":cv2.COLOR_HSV2RGB,
            "COLOR_HSV2RGB_FULL":cv2.COLOR_HSV2RGB_FULL,
            "COLOR_LAB2BGR":cv2.COLOR_LAB2BGR,
            "COLOR_LAB2LBGR":cv2.COLOR_LAB2LBGR,
            "COLOR_LAB2LRGB":cv2.COLOR_LAB2LRGB,
            "COLOR_LAB2RGB":cv2.COLOR_LAB2RGB,
            "COLOR_LBGR2LAB":cv2.COLOR_LBGR2LAB,
            "COLOR_LBGR2LUV":cv2.COLOR_LBGR2LUV,
            "COLOR_LBGR2Lab":cv2.COLOR_LBGR2Lab,
            "COLOR_LBGR2Luv":cv2.COLOR_LBGR2Luv,
            "COLOR_LRGB2LAB":cv2.COLOR_LRGB2LAB,
            "COLOR_LRGB2LUV":cv2.COLOR_LRGB2LUV,
            "COLOR_LRGB2Lab":cv2.COLOR_LRGB2Lab,
            "COLOR_LRGB2Luv":cv2.COLOR_LRGB2Luv,
            "COLOR_LUV2BGR":cv2.COLOR_LUV2BGR,
            "COLOR_LUV2LBGR":cv2.COLOR_LUV2LBGR,
            "COLOR_LUV2LRGB":cv2.COLOR_LUV2LRGB,
            "COLOR_LUV2RGB":cv2.COLOR_LUV2RGB,
            "COLOR_Lab2BGR":cv2.COLOR_Lab2BGR,
            "COLOR_Lab2LBGR":cv2.COLOR_Lab2LBGR,
            "COLOR_Lab2LRGB":cv2.COLOR_Lab2LRGB,
            "COLOR_Lab2RGB":cv2.COLOR_Lab2RGB,
            "COLOR_Luv2BGR":cv2.COLOR_Luv2BGR,
            "COLOR_Luv2LBGR":cv2.COLOR_Luv2LBGR,
            "COLOR_Luv2LRGB":cv2.COLOR_Luv2LRGB,
            "COLOR_Luv2RGB":cv2.COLOR_Luv2RGB,
            "COLOR_RGB2BGR":cv2.COLOR_RGB2BGR,
            "COLOR_RGB2BGR555":cv2.COLOR_RGB2BGR555,
            "COLOR_RGB2BGR565":cv2.COLOR_RGB2BGR565,
            "COLOR_RGB2BGRA":cv2.COLOR_RGB2BGRA,
            "COLOR_RGB2GRAY":cv2.COLOR_RGB2GRAY,
            "COLOR_RGB2HLS":cv2.COLOR_RGB2HLS,
            "COLOR_RGB2HLS_FULL":cv2.COLOR_RGB2HLS_FULL,
            "COLOR_RGB2HSV":cv2.COLOR_RGB2HSV,
            "COLOR_RGB2HSV_FULL":cv2.COLOR_RGB2HSV_FULL,
            "COLOR_RGB2LAB":cv2.COLOR_RGB2LAB,
            "COLOR_RGB2LUV":cv2.COLOR_RGB2LUV,
            "COLOR_RGB2Lab":cv2.COLOR_RGB2Lab,
            "COLOR_RGB2Luv":cv2.COLOR_RGB2Luv,
            "COLOR_RGB2RGBA":cv2.COLOR_RGB2RGBA,
            "COLOR_RGB2XYZ":cv2.COLOR_RGB2XYZ,
            "COLOR_RGB2YCR_CB":cv2.COLOR_RGB2YCR_CB,
            "COLOR_RGB2YCrCb":cv2.COLOR_RGB2YCrCb,
            "COLOR_RGB2YUV":cv2.COLOR_RGB2YUV,
            "COLOR_RGB2YUV_I420":cv2.COLOR_RGB2YUV_I420,
            "COLOR_RGB2YUV_IYUV":cv2.COLOR_RGB2YUV_IYUV,
            "COLOR_RGB2YUV_YV12":cv2.COLOR_RGB2YUV_YV12,
            "COLOR_RGBA2BGR":cv2.COLOR_RGBA2BGR,
            "COLOR_RGBA2BGR555":cv2.COLOR_RGBA2BGR555,
            "COLOR_RGBA2BGR565":cv2.COLOR_RGBA2BGR565,
            "COLOR_RGBA2BGRA":cv2.COLOR_RGBA2BGRA,
            "COLOR_RGBA2GRAY":cv2.COLOR_RGBA2GRAY,
            "COLOR_RGBA2RGB":cv2.COLOR_RGBA2RGB,
            "COLOR_RGBA2YUV_I420":cv2.COLOR_RGBA2YUV_I420,
            "COLOR_RGBA2YUV_IYUV":cv2.COLOR_RGBA2YUV_IYUV,
            "COLOR_RGBA2YUV_YV12":cv2.COLOR_RGBA2YUV_YV12,
            "COLOR_XYZ2BGR":cv2.COLOR_XYZ2BGR,
            "COLOR_XYZ2RGB":cv2.COLOR_XYZ2RGB,
            "COLOR_YCR_CB2BGR":cv2.COLOR_YCR_CB2BGR,
            "COLOR_YCR_CB2RGB":cv2.COLOR_YCR_CB2RGB,
            "COLOR_YCrCb2BGR":cv2.COLOR_YCrCb2BGR,
            "COLOR_YCrCb2RGB":cv2.COLOR_YCrCb2RGB,
            "COLOR_YUV2BGR":cv2.COLOR_YUV2BGR,
            "COLOR_YUV2RGB":cv2.COLOR_YUV2RGB,
            "IMREAD_REDUCED_COLOR_2":cv2.IMREAD_REDUCED_COLOR_2,
            "IMREAD_REDUCED_COLOR_4":cv2.IMREAD_REDUCED_COLOR_4
              }

    def __init__(self):
        super().__init__()

        self.setUI()

    def setUI(self):
        w = QWidget()
        f = QFormLayout()

        btn = QPushButton("Başlat")
        btn.clicked.connect(self.st)
        f.addRow(btn)

        self.cb = QComboBox()
        self.cb.addItems(self.colors.keys())
        self.cb.currentIndexChanged.connect(self.set_color)
        f.addRow(self.cb)

        self.sp = QSpinBox()
        self.sp.setMaximum(5000)
        self.sp.valueChanged.connect(self.set_timer)
        f.addRow(self.sp)

        self.cam = c.Camera(self)
        f.addRow(self.cam)


        w.setLayout(f)
        self.setCentralWidget(w)

    def set_color(self):
        self.data["color_filter"] = self.cb.currentText()

    def set_timer(self):
        self.data["timer"] = self.sp.value()
        self.st()

    def st(self):
        self.cam.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())