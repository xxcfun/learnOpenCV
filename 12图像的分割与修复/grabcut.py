"""
grabCut 图像分割
grabCut(img, mask, rect, bgdModel, fgdModel, 5, mode)
mask 生成的掩码 BGD: 背景，0
              FGD: 前景，1
              PR_BGD: 可能是背景，2
              PR_FGD: 可能是前景，3
rect 区域
mode 模式 FC_INIT_WITH_RECT  FC_INIT_WITH_MASK
"""

import cv2
import numpy as np


class App:
    flag_rect = False
    rect = (0, 0, 0, 0)
    startX = 0
    startY = 0

    # 鼠标移动事件
    def onmouse(self, event, x, y, flags, param):
        # 按下
        if event == cv2.EVENT_LBUTTONDOWN:
            self.flag_rect = True
            self.startX = x
            self.startY = y
        # 抬起
        elif event == cv2.EVENT_LBUTTONUP:
            self.flag_rect = False
            cv2.rectangle(self.img, (self.startX, self.startY), (x, y), (0, 0, 255), 3)
            self.rect = (min(self.startX, x), min(self.startY, y), abs(self.startX - x), abs(self.startY - y))
        # 移动
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.flag_rect:
                self.img = self.img2.copy()
                cv2.rectangle(self.img, (self.startX, self.startY), (x, y), (255, 0, 0), 3)

    # 主程序
    def run(self):
        cv2.namedWindow('input')
        cv2.setMouseCallback('input', self.onmouse)

        self.img = cv2.imread('1.jpg')
        self.img = cv2.resize(self.img, (480, 640))
        self.img2 = self.img.copy()
        self.mask = np.zeros(self.img.shape[:2], np.uint8)
        self.output = np.zeros(self.img.shape, np.uint8)

        while 1:
            cv2.imshow('input', self.img)
            cv2.imshow('output', self.output)
            k = cv2.waitKey(10)
            if k == 27:
                break

            if k == ord('g'):
                bgdModel = np.zeros((1, 65), np.float64)
                fgdModel = np.zeros((1, 65), np.float64)
                cv2.grabCut(self.img2, self.mask, self.rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((self.mask == 1) | (self.mask == 3), 255, 0).astype('uint8')
            self.output = cv2.bitwise_and(self.img2, self.img2, mask=mask2)
            cv2.imwrite('mask.png', self.output)


# 程序运行
App().run()
