import os

import cv2

import numpy as np 

img = cv2.imread(os.path.join('.','data','parrot.jpg'))
resized_img = cv2.resize(img, (640,480))

img_edge = cv2.Canny(resized_img, 100, 200)

img_edge_d = cv2.dilate(img_edge, np.ones((5,5), dtype = np.int8))

img_edge_e = cv2.erode(img_edge_d, np.ones((5,5), dtype = np.int8))

cv2.imshow('img', resized_img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)

cv2.waitKey(0)