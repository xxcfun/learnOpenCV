import cv2

# 初始化窗口
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

# 获取视频设备/从视频文件读取视频帧
cap = cv2.VideoCapture('rtsp://admin:Aa123456@192.168.1.84/H264?ch=1&subtype=0')

# 创建videowriter为写自媒体文件
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
vw = cv2.VideoWriter('out.mp4', fourcc, 25, size)

# 判断摄像头是否打开
while cap.isOpened():
    # 从摄像头获取视频帧
    ret, frame = cap.read()

    if ret:
        # 将视频帧在窗口中显示
        cv2.imshow('video', frame)
        # 重新将窗口设置为指定大小
        cv2.resizeWindow('video', 640, 480)

        # 写数据到多媒体文件
        vw.write(frame)

        # 等待键盘事件，如为q，退出
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    else:
        break

# 释放videoCapture
cap.release()
# 释放videowrite
vw.release()
# 释放窗口
cv2.destroyAllWindows()
