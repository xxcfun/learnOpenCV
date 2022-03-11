"""
*查找轮廓
findContours(img, mode, ApproximationMode...)
mode: 模式，对查找的轮廓如何处置 1.RETR_EXTERNAL=0，表示只检测外轮廓
                            2.RETR_LIST=1，检测的轮廓不建立等级关系
                            3.RETR_CCOMP=2，每层最多两级
                            4.RETR_TREE=3，按树形存储轮廓
ApproximationMode: 近似模式  1.CHAIN_APPROX_SIMPLE，只保存角点
                            2.CHAIN_APPROX_NONE，保存所有轮廓上的点
api两个返回值 contours，hierarchy
contours 所有轮廓集
hierarchy 层级关系

*绘制轮廓
drawContours(img, contours, contourIdx, color, thickness...)
contourIdx: 对哪些轮廓进行绘制，如：-1表示绘制所有轮廓
thickness： 线宽，如：-1是全部填充

*轮廓面积
contourArea(contour)
contour: 轮廓
*轮廓周长
arcLength(curve, closed)
curve: 轮廓
closed: 是否是闭合的 true false

*多边形逼近
approxPolyDP(curve, epsilon, closed)
curve: 轮廓
epsilon: 精度
closed: 是否闭合

*凸包
convexHull(points, clockwise, ...)
points: 轮廓
clockwise： 顺时针绘制

*最小外接矩形
minAreaRect(points)
points: 轮廓
返回值：RotatedRect

*最大外接矩形
boundingRect(array)
array: 轮廓
返回值：Rect
"""
import cv2
import numpy as np


def drawShape(src, points):
    i = 0
    while i < len(points):
        if i == len(points) - 1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 3)
        else:
            x, y = points[i][0]
            x1, y1 = points[i + 1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 3)
        i = i + 1


# 读文件
# img = cv2.imread('contours.png')
# img = cv2.imread('hand.png')
img = cv2.imread('hello.png')

# 转变成单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制轮廓
cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

# # 计算面积
# area = cv2.contourArea(contours[0])
# print(area)
#
# # 计算周长
# len = cv2.arcLength(contours[0], True)
# print(len)

# # 多边形逼近
# e = 20  # 精度
# approx = cv2.approxPolyDP(contours[0], e, True)
#
# # drawShape(img, approx)
#
# # 凸包
# hull = cv2.convexHull(contours[0])

# drawShape(img, hull)

# 最小外接矩形
r = cv2.minAreaRect(contours[1])
box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

# 最大外接矩形
x, y, w, h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x, y), (w+x, h+y), (255, 0, 0), 3)

cv2.imshow('img', img)
cv2.imshow('binary', binary)
cv2.waitKey(0)
