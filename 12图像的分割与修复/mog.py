"""
视频前背景分离
createBackgroundSubtractorMOG(history, nmixtures, backgroundRatio, noiseSigma)
history 默认200
nmixtures 高斯范围值 默认5
backgroundRatio 背景比率 默认0.7
noiseSigma 自动降噪 默认0
"""
import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://admin:Aa123456@192.168.1.84/H264?ch=1&subtype=0')
# mog
# mog = cv2.bgsegm.createBackgroundSubtractorMOG()

# mog2 优点：会检测出阴影部分  缺点：会产生很多噪点
# mog = cv2.createBackgroundSubtractorMOG2()

# gmg 优点：可以计算出阴影部分，同时减少噪点  缺点：如果采用默认值，在开始很长时间内没有信息显示  解决：调整开始的初始帧数
mog = cv2.bgsegm.createBackgroundSubtractorGMG(10)

while True:
    ret, frame = cap.read()
    fgmask = mog.apply(frame)

    cv2.imshow('video', fgmask)

    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
