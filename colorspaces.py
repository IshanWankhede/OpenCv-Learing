import os 
import cv2

image_path = os.path.join('.','data','parrot.jpg')

img = cv2.imread(image_path)
resized_img = cv2.resize(img, (640,480))

img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(resized_img, cv2.COLOR_BGR2HSV)

print(resized_img.shape)

cv2.imshow('image',resized_img)
cv2.imshow('image_rgb',img_rgb)
cv2.imshow('image_gray',img_gray) 
cv2.imshow('image_hsv',img_hsv) 
cv2.waitKey(0)