import os 
import cv2

#image read
image_path = os.path.join('.', 'data', '1 (1).jpeg')

img = cv2.imread(image_path)   

resized_img = cv2.resize(img, (640, 480))    # width and height
# resized_img_1 = cv2.resize(img, (64, 48))
 
print(img.shape)    # height and width
print(resized_img.shape)
# print(resized_img_1.shape)

#visualize image

cv2.imshow('image', img)
cv2.imshow('resized_image', resized_img)
# cv2.imshow('resized_image_1', resized_img_1)
cv2.waitKey(0)   
