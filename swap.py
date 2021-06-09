
import cv2
import numpy as np
p1=cv2.imread('nobita.jpg')
cv2.imshow('nobita.jpg',p1)
cv2.waitKey()
cv2.destroyAllWindows()
p2=cv2.imread('sunio.jpg')
cv2.imshow('sunio.jpg',p2)
cv2.waitKey()
cv2.destroyAllWindows()
p2=cv2.imread('sunio.jpg')
crop_p2=p2[30:130,60:200]
cv2.imshow('crop_p2',crop_p2)
cv2.waitKey()
cv2.destroyAllWindows()
p1=cv2.imread('nobita.jpg')
crop_p1=p1[30:130,60:200]
cv2.imshow('crop_p1',crop_p1)
cv2.waitKey()
cv2.destroyAllWindows()
p2=cv2.imread('sunio.jpg')
p2[30:130,60:200]=crop_p1
cv2.imshow('sunio.jpg',p2)
cv2.waitKey()
cv2.destroyAllWindows()
p1=cv2.imread('nobita.jpg')
p1[30:130,60:200]=crop_p2
cv2.imshow('nobita.jpg',p1)
cv2.waitKey()
cv2.destroyAllWindows()
