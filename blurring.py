import os
import cv2

img = cv2.imread(os.path.join('.','data','1 (1).jpeg'))


k_size = 75
img_blur = cv2.blur(img, (k_size, k_size))

img_gaussianBlur = cv2.GaussianBlur(img, (k_size,k_size), 10)

img_medianBlur = cv2.medianBlur(img, k_size)

cv2.imshow('image0', img)
cv2.imshow('image1', img_blur)
cv2.imshow('image2', img_gaussianBlur)
cv2.imshow('image3', img_medianBlur)   # TO REMOVE THE NOISE FROM IMAGE
cv2.waitKey(0)


