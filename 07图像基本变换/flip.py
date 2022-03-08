"""
图像反转
flip(img, flipCode)
flipCode == 0, 上下
flipCode > 0, 左右
flipCode < 0, 上下左右
"""
import cv2
import numpy as np

dog = cv2.imread('dog.jpeg')
new1 = cv2.flip(dog, 0)
new2 = cv2.flip(dog, 1)
new3 = cv2.flip(dog, -1)

cv2.imshow('new1', new1)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)
cv2.waitKey(0)
