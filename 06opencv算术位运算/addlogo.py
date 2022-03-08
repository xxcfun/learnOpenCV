"""
给图像添加水印
1.引入一张图片
2.要有一个logo
3.计算图片在什么地方添加，在添加的地方变成黑色 先取反再相与
4.利用add，将logo与图片叠加在一起
"""
import cv2
import numpy as np

# 导入图片
back = cv2.imread('back.jpeg')

# 创建logo
logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

# 绘制logo
logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]

mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255

# 对mask取反
m = cv2.bitwise_not(mask)

# 选择图像添加logo的位置
roi = back[0:200, 0:200]

# 与m经行与操作
tmp = cv2.bitwise_and(roi, roi, mask=m)

dst = cv2.add(tmp, logo)
back[0:200, 0:200] = dst

cv2.imshow('back', back)
# cv2.imshow('tmp', tmp)
# cv2.imshow('dst', dst)
# cv2.imshow('m', m)
# cv2.imshow('mask', mask)
# cv2.imshow('logo', logo)
cv2.waitKey(0)
