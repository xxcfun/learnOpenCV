"""
图像卷积
filter2D(src, ddepth, kernel, anchor, delta, borderType)
低通滤波：
1.方盒滤波
boxFilter(src, ddepth, ksize, anchor, normalize, borderType)
2.均值滤波
blur(src, kszie, anchor, borderType)
3.高斯滤波 解决高斯噪点
GaussianBlur(img, kernel, sigmaX, sigmaY)
4.中值滤波 解决胡椒噪点
medianBlur(img, kszie)
5.双边滤波 保留边缘，进行美颜
bilateralFilter(img, d, sigmaColor, sigmaSpace, ...)
"""
import cv2
import numpy as np

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)

img = cv2.imread('shudu.jpeg')

# 创建一个5*5的矩阵，里面都是1，然后除以25
# kernal = np.ones((5, 5), np.float32) / 25
# dst = cv2.filter2D(img, -1, kernal)

# 均值滤波
# dst = cv2.blur(img, (5, 5))

# 高斯滤波
# dst = cv2.GaussianBlur(img, (5, 5), sigmaX=1)

# 中值滤波
dst = cv2.medianBlur(img, 5)

# 双边滤波
# dst = cv2.bilateralFilter(img, 7, 20, 50)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)
