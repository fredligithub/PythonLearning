import cv2
import numpy as np
from matplotlib import pyplot as plt
img= cv2.imread('E:/Code/Python/1stPythonEntry/venv/MyTestCode/Output/rnd.jpeg')
# 灰度图
GrayImage= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 大于阈值的像素点的灰度值设定为最大值(如8位灰度值最大为255)，灰度值小于阈值的像素点的灰度值设定为0
ret,thresh1= cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)

# 大于阈值的像素点的灰度值设定为0，而小于该阈值的设定为255
ret,thresh2= cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY_INV)

# 像素点的灰度值小于阈值不改变，大于阈值的灰度值的像素点就设定为该阈值
ret,thresh3= cv2.threshold(GrayImage,127,255,cv2.THRESH_TRUNC)

# 像素点的灰度值小于该阈值的不进行任何改变，而大于该阈值的部分，其灰度值全部变为0
ret,thresh4= cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO)

# 像素点的灰度值大于该阈值的不进行任何改变，像素点的灰度值小于该阈值的，其灰度值全部变为0
ret,thresh5= cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()
