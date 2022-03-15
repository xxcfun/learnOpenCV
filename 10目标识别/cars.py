# opencv实战，车流检测
import cv2
import numpy as np

# 最小高度和宽度
min_w = 60
min_h = 40
# 车辆数组
cars = []
# 检测线高
line_width = 300
# 线的偏移量
offset = 7
# 初始化车辆总数
carnum = 0

# 求中心点
def center(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1

    return cx, cy


# 读视频 960*1280
cap = cv2.VideoCapture('rtsp://admin:Aa123456@192.168.1.84/H264?ch=1&subtype=0')

bgsubmog = cv2.createBackgroundSubtractorMOG2()

# 形态学kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

while True:
    ret, frame = cap.read()

    if ret:
        # 灰度
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 去噪
        blur = cv2.GaussianBlur(frame, (3, 3), 5)
        # 去背景
        mask = bgsubmog.apply(blur)

        # 腐蚀 去掉图像中的小斑块
        erode = cv2.erode(mask, kernel)

        # 膨胀 还原放大
        dilate = cv2.dilate(erode, kernel, iterations=3)

        # 闭操作 去掉物体内部的小块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)
        close = cv2.morphologyEx(close, cv2.MORPH_CLOSE, kernel)

        # 查找轮廓
        contours, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 画线 从左侧画一条检测线
        cv2.line(frame, (line_width, 600), (line_width, 880), (255, 255, 0), 3)

        # for循环画轮廓
        for (i, c) in enumerate(contours):
            (x, y, w, h) = cv2.boundingRect(c)

            # 对车辆进行过滤，以验证是否是有效的车辆
            isValid = (w >= min_w) and (h >= min_h)
            if not isValid:
                continue

            # 到这里都是有效的车辆
            # 将车被标记出来
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # 拿到车的中心点cpoint
            cpoint = center(x, y, w, h)
            # 将点存入车辆数组
            cars.append(cpoint)
            # 画出车的中心点
            cv2.circle(frame, (cpoint), 5, (0, 0, 255), -1)

            for (x, y) in cars:
                # 要有一条线，有范围，车辆经过后减去
                if (x > line_width - offset) and (x < line_width + offset):
                    carnum += 1
                    cars.remove((x, y))

        cv2.putText(frame, "Cars Count:" + str(carnum), (800, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
        # cv2.imshow('video', close)
        cv2.imshow('origin', frame)

    key = cv2.waitKey(1)
    # 27就是键盘左上角的ESC键
    if key == 27:
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
