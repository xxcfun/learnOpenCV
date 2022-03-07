import cv2
import numpy as np


# cv2.namedWindow('img', cv2.WINDOW_NORMAL)

img = cv2.imread('1.jpg')

# shape属性包含了三个信息
# 高度 长度 通道数
print(img.shape)

# 图像占用多大空间 
# 高度 * 长度 * 通道数
print(img.size)

# 图像中每个元素的位深
print(img.dtype)