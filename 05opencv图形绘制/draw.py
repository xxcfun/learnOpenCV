import cv2
import numpy as np

cv2.namedWindow('img', cv2.WINDOW_NORMAL)

img = cv2.imread('1.jpg')

# 画线
cv2.line(img, (10, 20), (500, 1000), (0, 0, 255), 10, 4)
cv2.line(img, (100, 20), (600, 1000), (255, 255, 255), 10, 16)

# 画矩形
cv2.rectangle(img, (1320, 1240), (1620, 1640), (0, 0, 255), 4)

# 画圆
cv2.circle(img, (2000, 500), 100, (0, 0, 255), 4)
cv2.circle(img, (2000, 500), 10, (0, 0, 255), -1)

# 画椭圆
# 度是按顺时针计算的
# 0度是从右侧开始的
cv2.ellipse(img, (2000, 500), (100, 50), 0, 0, 360, (0, 0, 255), 4)

# 画多边形
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 255), 4)
# 填充多边形颜色
cv2.fillPoly(img, [pts], (255, 255, 0))

# 绘制文本
cv2.putText(img, "hello, I`m XueBin Yan", (600, 2000), cv2.FONT_HERSHEY_DUPLEX, 5, (0, 0, 255), 4)

cv2.imshow('img', img)
cv2.waitKey(0)
