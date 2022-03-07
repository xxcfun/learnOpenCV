import cv2
import numpy as np

cv2.namedWindow('img1', cv2.WINDOW_NORMAL)
cv2.namedWindow('b', cv2.WINDOW_NORMAL)
cv2.namedWindow('g', cv2.WINDOW_NORMAL)
cv2.namedWindow('r', cv2.WINDOW_NORMAL)
cv2.namedWindow('img2', cv2.WINDOW_NORMAL)

# img1 = np.zeros((480, 640, 3), np.uint8)
img1 = cv2.imread('1.jpg')

b, g, r = cv2.split(img1)

b[10:100, 10:100] = 255
g[10:100, 10:100] = 255

img2 = cv2.merge((b, g, r))

cv2.imshow('img1', img1)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.imshow('img2', img2)

cv2.waitKey(0)