"""  注意 opencv4后 sift和surf都没了，这pip包里用opencv的3.4.2.16版本
SIFT关键点检测
1.创建SIFT对象，sift=cv2.xfeatures2d.SIFT_create()
2.进行检测，kp=sift.detect(img, ...)
3.绘制关键点，drawKeypoints(grap, kp, img)

同时计算关键点和描述 一般用这个
kp, des = sift.detectAndCompute(img, mask)
mask: 指明对img中哪个区域进行计算

SURF特征检测 相比SIFT速度加快了
1.创建对象 surf=cv2.xfeatures2d.SURF_create()
2.进行检测 kp,des=surf.detectAndCompute(img,mask)
3.绘制关键点

ORB特征检测 实时检测，准确性不如上面两个
1.创建对象 orb=cv2.ORB_create()
2.进行检测 kp,des=orb.detectAndCompute(img,mask)
3.绘制关键点
"""
import cv2
import numpy as np

# 读文件
img = cv2.imread('shudu.jpeg')

# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # 创建sift对象
sift = cv2.xfeatures2d.SIFT_create()
#
# # SIFT关键点检测
# # kp = sift.detect(gray, None)
#
# # 同时计算关键点和描述
# kp, des = sift.detectAndCompute(gray, None)

# # 创建SURF对象
# surf = cv2.xfeatures2d.SURF_create()
# # 使用SURF进行检测
# kp, des = surf.detectAndCompute(gray, None)

# 创建ORB对象
orb = cv2.ORB_create()
# 使用SURF进行检测
kp, des = orb.detectAndCompute(gray, None)

# print(des[0])

# 绘制关键点
cv2.drawKeypoints(gray, kp, img)

cv2.imshow('img', img)
cv2.waitKey(0)
