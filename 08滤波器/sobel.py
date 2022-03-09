"""
高通滤波  ！！！！scale后面的值几乎不用
1.Sobel（索贝尔算子）（高斯）
Sobel(src, ddepth, dx, dy, kszie=3, scale=1, delta=0, borderType=BORDER_DEFAULT)

2.Scharr（沙尔算子）
Scharr(src, ddepth, dx, dy, scale=1, delta=0, borderType=BORDER_DEFAULT)

3.Laplacian(拉普拉斯算子) 可以同时求两个方向的边缘 对噪音敏感，一般先去噪再用拉普拉斯算子
Laplacian(src, ddepth, ksize=1, scale=1, borderType=BORDER_DEFAULT)
"""
import cv2
import numpy as np

img = cv2.imread('shudu.jpeg')

# 索贝尔算子y方向边缘
# d1 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# 索贝尔算子x方向边缘
# d2 = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

# 沙尔算子y方向边缘
# d1 = cv2.Scharr(img, cv2.CV_64F, 1, 0)
# 沙尔算子x方向边缘
# d2 = cv2.Scharr(img, cv2.CV_64F, 0, 1)
#
# dst = cv2.add(d1, d2)

# 拉普拉斯算子
ldst = cv2.Laplacian(img, cv2.CV_64F, ksize=5)

# cv2.imshow('d1', d1)
# cv2.imshow('d2', d2)
# cv2.imshow('dst', dst)
cv2.imshow('ldst', ldst)
cv2.waitKey(0)
