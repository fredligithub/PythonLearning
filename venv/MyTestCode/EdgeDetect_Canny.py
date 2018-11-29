import cv2
import numpy as np

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
    dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('Canny demo', dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread('C:/Users/GG/Pictures/Saved Pictures/Road.jpg')

# 读取了图片的长， 宽
# h,w = img.shape[:2]
# print(h,w)

# 图片转换为灰度图， 包括几种常用的转换方法： cv2.COLOR_BGR2GRAY  cv2.COLOR_BGR2RGB  cv2.COLOR_GRAY2BGR
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('Canny demo')

cv2.createTrackbar('Min threshold', 'Canny demo', lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
