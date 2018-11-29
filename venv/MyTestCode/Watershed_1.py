import cv2
import numpy as np

img = cv2.imread('C:/Users/GG/Pictures/Saved Pictures/bubble.jpg')
cv2.imshow('img',img)

# 将图像转化为灰度图像
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 阈值化处理
ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# cv2.imshow('thresh',thresh)

#noise removal
#opening operator是先腐蚀后膨胀，可以消除一些细小的边界，消除噪声
kernel=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
# cv2.imshow('opening',opening)

#sure background area
sure_bg=cv2.dilate(opening,kernel,iterations=3)
# cv2.imshow('bg',sure_bg)

#finding sure foreground area
dist_transfrom=cv2.distanceTransform(opening,cv2.DIST_L2 ,5)
#cv2.imshow('dist_transfrom',dist_transfrom)
ret,sure_fg=cv2.threshold(dist_transfrom,0.7*dist_transfrom.max(),255,0)

# cv2.imshow('sure_fg',sure_fg)

#finding unknow region
sure_fg=np.uint8(sure_fg)
unknow=cv2.subtract(sure_bg,sure_fg) #背景-前景
# cv2.imshow('unknow',unknow)

ret,maker=cv2.connectedComponents(sure_fg)
maker=maker+1
maker[unknow==255]=0

maker = cv2.watershed(img,maker)
# cv2.imshow('maker',maker)
img[maker == -1] = [0,0,255]
cv2.imshow('result',img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()