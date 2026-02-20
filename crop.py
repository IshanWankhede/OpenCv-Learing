import os
import cv2

image_path = os.path.join('.','data','1 (1).jpeg')

img = cv2.imread(image_path)

print(img.shape)

croped_image = img[320:640, 420:700]   #- img[y1:y2, x1:x2]
# cropped = img[y_start:y_end, x_start:x_end]

cv2.imshow('image', img)
cv2.imshow('image1', croped_image)
cv2.waitKey(0)