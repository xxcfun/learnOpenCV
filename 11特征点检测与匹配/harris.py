"""
Harris角点检测
cornerHarris(img, dst, blockSize, ksize, k)
blockSize: 检测窗口大小
ksize: Sobel的卷积核
k: 权重系数，经验值，一般0.02~0.04之间

Shi-Tomasi角点检测
goodFeaturesToTrack(img, maxCorners, ...)
maxCorners: 角点的最大数，值为0表示无限制
qualityLevel: 角点质量，小于1.0的正数，一般在0.01~0.1之间
minDistance: 角之间最小欧式距离，忽略小于此距离的点
mask: 感兴趣的区域
blockSize: 检测窗口大小
useHarrisDetector: 是否使用Harris算法
k: 默认0.04
"""
import cv2
import numpy as np

# Harris
# blockSize = 2
# ksize = 3
# k = 0.04

# Shi-Tomasi
maxCorners = 1000
qualityLevel = 0.01
minDistance = 10

img = cv2.imread('shudu.jpeg')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Harris角点检测
# dst = cv2.cornerHarris(gray, blockSize, ksize, k)
# Harris角点展示
# img[dst > 0.01 * dst.max()] = [0, 0, 255]

# Shi-Tomasi角点检测
corners = cv2.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)
print(corners)
# 浮点型转为整形
corners = np.int0(corners)
# Shi-Tomasi绘制角点
for i in corners:
    print(i)
    # 二维转为一维
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

cv2.imshow('harris', img)

cv2.waitKey(0)
