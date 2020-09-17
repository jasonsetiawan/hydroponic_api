import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Test1.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
lower_green = np.array([0,0,30])
upper_green = np.array([100,255,255])
    
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(img,img, mask= mask)
gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 1)
# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=2)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)


# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

# markers = cv2.watershed(img,markers)
# img[markers == -1] = [255,0,0]


cv2.imshow('main',img)
cv2.imshow('hsv',hsv)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('thresh',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()