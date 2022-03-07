# 基本功能：
# 通过鼠标进行基本图形的绘制
# l键画线 r键画矩形 c键画圆
import cv2
import numpy as np

curshape = 0
startpos = (0, 0)

# 显示窗口和背景
img = np.zeros((800, 800, 3), np.uint8)


# 鼠标回调函数
def mouse_callback(event, x, y, flags, userdata):
    global curshape, startpos

    if event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
        startpos = (x, y)
    elif event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP:
        if curshape == 0:  # line
            cv2.line(img, startpos, (x, y), (0, 0, 255), 4)
        elif curshape == 1:  # rectangle
            cv2.rectangle(img, startpos, (x, y), (0, 0, 255), 4)
        elif curshape == 2:  # circle
            a = (x - startpos[0])
            b = (y - startpos[1])
            r = int((a**2+b**2)**0.5)
            cv2.circle(img, startpos, r, (0, 0, 255), 4)
        else:
            print('null')


# 创建窗口
cv2.namedWindow('drawshape', cv2.WINDOW_NORMAL)

# 设置鼠标回调
cv2.setMouseCallback('drawshape', mouse_callback)

while True:
    cv2.imshow('drawshape', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('l'):  # line
        curshape = 0
    elif key == ord('r'):  # rectangle
        curshape = 1
    elif key == ord('c'):  # circle
        curshape = 2

cv2.destroyAllWindows()