"""
全局二值化
threshold(img, thresh, maxVal, type)
img: 图像，最好是灰度图
thresh: 阈值
maxVal: 超过阈值，替换成maxVal
type: 1.THRESH_BINARY 和 THRESH_BINARY_INV
      2.THRESH_TRUNC
      3.THRESH_TOZERO 和 THRESH_TOZERO_INV
"""
import cv2
import numpy as np

img = cv2.imread('dog.jpeg')
# 转化为灰度图
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)

cv2.imshow('img1', img1)
cv2.imshow('dst', dst)
cv2.waitKey(0)
