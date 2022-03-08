"""
透视变换
warpPerspective(img, M, dszie, ...)
M: 变换矩阵
dszie: 目标图像大小
透视变换矩阵
getPersectiveTransform(src, dst)
通过四个点确定位置
"""
import cv2
import numpy as np

img = cv2.imread('dog.jpeg')

src = np.float32([[280, 120], [900, 120], [280, 570], [900, 570]])
dst = np.float32([[0, 0], [630, 0], [0, 420], [630, 420]])
M = cv2.getPerspectiveTransform(src, dst)

new = cv2.warpPerspective(img, M, (630, 420))

cv2.imshow('new', new)
cv2.waitKey(0)