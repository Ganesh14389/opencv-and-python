import numpy as np
import cv2
p1=cv2.imread('sunio1.jpg')
p2=cv2.imread('dora.png')
p1=p1[0:180,40:180]
p2=p2[0:180,40:180]
cv2.imshow('p1',p1)
cv2.imshow('p2',p2)
cv2.waitKey()
cv2.destroyAllWindows
cv2.imshow('p1',p1)
cv2.imshow('p2',p2)
cv2.waitKey()
cv2.destroyAllWindows

