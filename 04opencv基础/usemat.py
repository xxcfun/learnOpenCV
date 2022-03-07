import cv2
import numpy as np


cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.namedWindow('img2', cv2.WINDOW_NORMAL)
cv2.namedWindow('img3', cv2.WINDOW_NORMAL)

img = cv2.imread('1.jpg')

# 浅拷贝 一个对象改变了赋值，就会影响到另一个对象 新旧对象共享同一块内存
img2 = img

# 深拷贝 修改新对象，不会影响原对象，新旧对象不共享内存
img3 = img.copy()

img[10:100, 10:100] = [0, 0, 255]

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)