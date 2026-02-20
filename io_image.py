import os 
import cv2

#image read
image_path = os.path.join('.', 'data', '1 (1).jpeg')

img = cv2.imread(image_path)

# image write
cv2.imwrite(os.path.join('.', 'data', '1 (1)_out.jpeg'),img)

#visualize image

cv2.imshow('image', img)
cv2.waitKey(0)   # waits or holds the image till it disapper like if we press any key then it will disapper if we dont inclued it then the image will open and close so fast we cant see it
