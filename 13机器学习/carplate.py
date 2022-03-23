import cv2
import numpy as np
import pytesseract

# 1 创建Haar级联器
plate = cv2.CascadeClassifier('./haarcascade/haarcascade_russian_plate_number.xml')

# 2 导入带车牌的图片并将其灰度化
img = cv2.imread('plate1.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3 进行车牌识别
plates = plate.detectMultiScale(gray, 1.1, 5)
x, y, w, h = 0, 0, 0, 0
for (x, y, w, h) in plates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# 对获取的车牌进行预处理
# 1 提取ROI
roi = gray[y:y+h, x:x+w]
# 2 进行二值化
ret, roi_bin = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 3 文字处理
# psm 分页模式 oem 引擎
plate_text = pytesseract.image_to_string(roi, lang='chi_sim+eng', config='--psm 8 --oem 3')
print(plate_text)

cv2.imshow('roi_bin', roi_bin)
cv2.imshow('img', img)
cv2.waitKey(0)
