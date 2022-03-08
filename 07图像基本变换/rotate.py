"""
图像旋转
rotate(img, rotateCode)
rotateCode == ROTATE_90_CLOCKWISE, 90°
rotateCode == ROTATE_180, 180°
rotateCode ROTATE_90_COUNTERCLOCKWISE, 270°
"""
import cv2
import numpy as np

dog = cv2.imread('dog.jpeg')
new1 = cv2.rotate(dog, cv2.ROTATE_90_CLOCKWISE)
new2 = cv2.rotate(dog, cv2.ROTATE_180)
new3 = cv2.rotate(dog, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('new1', new1)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)
cv2.waitKey(0)
