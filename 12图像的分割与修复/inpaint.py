"""
图像修复
inpaint(img, mask, inpaintRadius, flags)
inpaintRadius 每个点的圆形邻域半径
flags INPAINT_NS, INPAINT_TELEA
"""
import cv2
import numpy as np

img = cv2.imread('1.jpg')
img = cv2.resize(img, (480, 640))
mask = cv2.imread('mask.png', 0)
mask = cv2.resize(mask, (480, 640))

dst = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)

cv2.imshow('dst', dst)
cv2.waitKey(0)
