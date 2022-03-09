"""
边缘检测 canny
Canny(src, minVal, maxVal, ...)
"""
import cv2
import numpy as np

cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)

img = cv2.imread('1.jpg')

dst = cv2.Canny(img, 80, 120)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
