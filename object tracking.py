import cv2
import numpy as np
image = cv2.imread('blue.png')
new_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('popup',new_image)
lower_bound = np.array([110,50,50])
upper_bound = np.array([130,252,252])
mask = cv2.inRange(new_image,lower_bound,upper_bound)
cv2.imshow('mask',mask)
result = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow('result',result)
cv2.waitKey(10000)
cv2.destroyAllWindows()