"""
图像溶合
addWeighted(A, alpha, B, bate, gamma)
A,B 两个图片
alpha, bate 权重
gamma 静态权重
"""

import cv2
import numpy as np

back = cv2.imread('back.jpeg')
dog = cv2.imread('dog.jpeg')

# 只有两个图像的属性一样的时候才可以溶合
print(back.shape)
print(dog.shape)

result = cv2.addWeighted(dog, 0.7, back, 0.3, 0)
cv2.imshow('add2', result)
cv2.waitKey(0)
