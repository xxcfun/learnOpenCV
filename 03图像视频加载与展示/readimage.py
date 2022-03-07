import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread("C:/Users/honor/Desktop/bike.png")

cv2.imshow('img', img)

key = cv2.waitKey(0)
if (key == ord('q')):
    exit()

cv2.destroyAllWindows()
