"""
自适应阈值二值化
adaptiveThreshold(img, maxVal, adaptiveMethod, type, blockSize, C)
adaptiveMethod: 计算阈值的方法
                1.ADAPTIVE_THRESH_MEAN_C: 计算邻近区域的平均值
                2.ADAPTIVE_THRESH_GAUSSIAN_C: 高斯窗口加权平均值
type: 和全局二值化一样，但只有两个值
      1.THRESH_BINARY
      2.THRESH_BINARY_INV
blockSize: 邻近区域的大小
C: 常量，应从计算出的平均值或加权平均值中减去
"""
import cv2
import numpy as np

img = cv2.imread('dog.jpeg')
# 转化为灰度图
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 0)

cv2.imshow('img1', img1)
cv2.imshow('dst', dst)
cv2.waitKey(0)
