import numpy as np
import cv2

image=np.zeros((512,512,3),np.uint8)
cv2.line(image,(0,0),(512,512),(255,0,0),7)
cv2.rectangle(image,(50,50),(200,200),(50,120,13),5)
cv2.circle(image,(256,256),80,(0,0,255),5)
cv2.imshow("black image",image)

cv2.waitKey(0)

cv2.destroyWindow()