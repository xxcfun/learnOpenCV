"""
位运算：与，或，异或，非操作
"""
import cv2
import numpy as np

# 创建一个图片
img1 = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)
# img1 = cv2.imread('back.jpeg')
# img2 = cv2.imread('dog.jpeg')

img1[20:120, 20:120] = 255
img2[80:180, 80:180] = 255

# 非操作
not_img = cv2.bitwise_not(img1)

# 与操作
and_img = cv2.bitwise_and(img1, img2)

# 或操作
or_img = cv2.bitwise_or(img1, img2)

# 异或操作
xor_img = cv2.bitwise_xor(img1, img2)

cv2.imshow('not_img', not_img)
cv2.imshow('and_img', and_img)
cv2.imshow('or_img', or_img)
cv2.imshow('xor_img', xor_img)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey(0)
