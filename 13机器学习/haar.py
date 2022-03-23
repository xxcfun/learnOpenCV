import cv2
import numpy as np

# 1 创建Haar级联器
face = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('./haarcascade/haarcascade_eye.xml')

# 2 导入人脸识别的图片并将其灰度化
img = cv2.imread('kda.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3 进行人脸识别
faces = face.detectMultiScale(gray, 1.1, 5)
i = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # 取多少行多少列
    roi_img = img[y:y+h, x:x+w]

    eyes = eye.detectMultiScale(roi_img, 1.1, 4)
    for (x, y, w, h) in eyes:
        cv2.rectangle(roi_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 提取每一个脸部
    i = i + 1
    winname = 'face' + str(i)
    cv2.imshow(winname, roi_img)

cv2.imshow('img', img)
cv2.waitKey(0)
