"""
摄像头中的人脸识别
"""
import cv2
import numpy as np

# 1 创建Haar级联器
face = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('./haarcascade/haarcascade_eye.xml')

# 2 导入人脸识别的图片并将其灰度化
cap = cv2.VideoCapture('rtsp://admin:Aa123456@192.168.1.84/H264?ch=1&subtype=0')
# 本机摄像头
# cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 3 进行人脸识别
        faces = face.detectMultiScale(gray, 1.1, 5)
        i = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

            # 取脸部
            roi_img = frame[y:y+h, x:x+w]

            # 在脸部进行眼睛识别
            eyes = eye.detectMultiScale(roi_img, 1.1, 4)
            for (x, y, w, h) in eyes:
                cv2.rectangle(roi_img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            cv2.imshow('img', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
