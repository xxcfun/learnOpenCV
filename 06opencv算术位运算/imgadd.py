# 图的加法运算就是矩阵的加法运算
# 因此加法运算的两张图是要相等的
import cv2
import numpy as np


cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.namedWindow('result1', cv2.WINDOW_NORMAL)
cv2.namedWindow('result2', cv2.WINDOW_NORMAL)
cv2.namedWindow('result3', cv2.WINDOW_NORMAL)
cv2.namedWindow('result4', cv2.WINDOW_NORMAL)

img1 = cv2.imread('1.jpg')

img2 = np.ones((4032, 3024, 3), np.uint8) * 50

# 原画
cv2.imshow('result', img1)

# 加法
result1 = cv2.add(img1, img2)
cv2.imshow('result1', result1)

# 减法
result2 = cv2.subtract(img1, img2)
cv2.imshow('result2', result2)

# 乘法
result3 = cv2.multiply(img1, img2)
cv2.imshow('result3', result3)

# 除法
result4 = cv2.divide(img1, img2)
cv2.imshow('result4', result4)

cv2.waitKey(0)
