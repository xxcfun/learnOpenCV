"""
暴力特征匹配
1.创建匹配器 BFMatcher(normType, crossCheck) 参数：匹配类型 交叉检查
2.进行特征匹配 bf.match(des1, des2)
3.绘制匹配点 cv2.drawMatches(img1, kp1, img2, kp2, match, ...)
"""
import cv2
import numpy as np

img1 = cv2.imread('dog.jpeg')
img2 = cv2.imread('tou.jpeg')

# 灰度化
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.xfeatures2d.SIFT_create()

# 同时计算两张图关键点和描述
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# 创建匹配器
bf = cv2.BFMatcher(cv2.NORM_L1)

# 进行特征匹配
match = bf.match(des1, des2)

# 绘制匹配点
img3 = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

cv2.imshow('img3', img3)

cv2.waitKey(0)
