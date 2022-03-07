# 图的加法运算就是矩阵的加法运算
# 因此加法运算的两张图是要相等的
import cv2
import numpy as np


cv2.namedWindow('result', cv2.WINDOW_NORMAL)

img1 = cv2.imread('1.jpg')

img2 = np.ones((4032, 3024, 3), np.uint8) * 50

result = cv2.add(img1, img2)
cv2.imshow('result', result)
cv2.waitKey(0)
