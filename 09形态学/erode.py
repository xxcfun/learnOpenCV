"""
腐蚀
erode(img, kernel, iterations=1)

获取形态学卷积核
getStructuringElement(type, size)
size(3*3 5*5)
卷积核类型 1.MORPH_RECT 矩形
         2.MORPH_ELLIPSE 圆形
         3.MORPH_CROSS 十字架形

膨胀
dilate(img, kernel, iterations=1)

开运算 = 先腐蚀后膨胀  消除图像外面噪点
morphologyEx(img, MORPH_OPEN, kernel)

闭运算 = 先膨胀后腐蚀  消除图像内部噪点
morphologyEx(img, MORPH_CLOSE, kernel)

梯度运算 求图形的边缘
morphologyEx(img, MORPH_GRADIENT, kernel)

顶帽运算 = 原图 - 开运算  得到图像外面的噪点
morphologyEx(img, MORPH_TOPHAT, kernel)

黑帽运算 = 原图 - 闭运算  得到图像内部的噪点
morphologyEx(img, MORPH_BLACKHAT, kernel)
"""
import cv2
import numpy as np

img = cv2.imread('open.png')
img1 = cv2.imread('close.png')
img2 = cv2.imread('default.png')
img3 = cv2.imread('tophat.png')

# 自定义的卷积核
# kernel = np.ones((5, 5), np.uint8)

# 或许形态学卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

# 腐蚀
erode = cv2.erode(img, kernel, iterations=1)

# 膨胀
dilate = cv2.dilate(erode, kernel, iterations=1)

# 开运算
open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 闭运算
close = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernel)

# 梯度运算
gradient = cv2.morphologyEx(img2, cv2.MORPH_GRADIENT, kernel)

# 顶帽运算
tophat = cv2.morphologyEx(img3, cv2.MORPH_TOPHAT, kernel)

# 黑帽运算
blackhat = cv2.morphologyEx(img1, cv2.MORPH_BLACKHAT, kernel)

# cv2.imshow('img', img)
# cv2.imshow('erode', erode)
# cv2.imshow('dilate', dilate)
# cv2.imshow('open', open)
# cv2.imshow('close', close)
# cv2.imshow('gradient', gradient)
# cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)
cv2.waitKey(0)
