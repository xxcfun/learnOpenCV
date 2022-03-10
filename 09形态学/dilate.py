"""
膨胀
dilate(img, kernel, iterations=1)
"""
import cv2
import numpy as np

img = cv2.imread('default.png')

# kernel = np.ones((5, 5), np.uint8)
# 或许形态学卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
dst = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
