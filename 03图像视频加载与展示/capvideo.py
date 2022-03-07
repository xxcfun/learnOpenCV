import cv2

# 初始化窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

# 获取视频设备/从视频文件读取视频帧
# cap = cv2.VideoCapture('C:/Users/honor/Desktop/1.mp4')
cap = cv2.VideoCapture('rtsp://admin:Aa123456@192.168.1.84/H264?ch=1&subtype=0')

while True:
    # 从摄像头获取视频帧
    ret, frame = cap.read()

    # 将视频帧在窗口中显示
    cv2.imshow('video', frame)

    # 等待键盘事件，如为q，退出
    key = cv2.waitKey(10)
    if (key & 0xFF == ord('q')):
        break

# 释放videoCapture
cap.release()
cv2.destroyAllWindows()
