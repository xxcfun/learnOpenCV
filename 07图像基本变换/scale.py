"""
图像的放大和缩小
缩放算法：
* INTER_NEAREST 邻近插值，速度快，效果差
* INTER_LINEAR 双线性插值，原图中的4个点
* INTER_CUBIC 三次插值，原图中的16个点
* INTER_AREA 效果最好
"""
import cv2
import numpy as np

dog = cv2.imread('dog.jpeg')
new = cv2.resize(dog, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)

cv2.imshow('dog', dog)
cv2.imshow('new', new)
cv2.waitKey(0)