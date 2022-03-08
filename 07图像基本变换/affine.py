"""
仿射变换 图像平移
warpAffine(src, M, dsize, flags, mode, value)
M: 变换矩阵
dsize: 输出尺寸大小
flags: 与resize中的插值算法一致
mode: 边界外推法标志
value: 填充边界的值

仿射变换 变换矩阵（一）
getRotationMatrix2D(center, angle, scale)
center: 中心点
angle: 角度
scale: 缩放比例

仿射变换 变换矩阵（二）
getAffineTransform(src[], dst[])
通过三个点可以确定变换的位置
"""
import cv2
import numpy as np

dog = cv2.imread('dog.jpeg')
h, w, ch = dog.shape
# M = np.float32([[1, 0, 100], [0, 1, 0]])
# 旋转角度是逆时针 中心点格式(x, y)
# M = cv2.getRotationMatrix2D((w/2, h/2), 15, 1.0)
src = np.float32([[400, 300], [800, 300], [400, 1000]])
dst = np.float32([[200, 400], [600, 500], [150, 1100]])
M = cv2.getAffineTransform(src, dst)

# 如果想改变图像的尺寸，需要更改下面的dsize
new = cv2.warpAffine(dog, M, (w, h))

cv2.imshow('new', new)
cv2.imshow('dog', dog)
cv2.waitKey(0)
