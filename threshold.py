import os 
import cv2

# converting colored image to binary image like only white or black pixels

image_path = os.path.join('.','data','Bear.jpg')

img = cv2.imread(image_path)
resized_img = cv2.resize(img,(640, 480))

# step1 -> converting this image in bgr to grayscale

img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('image',resized_img)
cv2.imshow('image_gray',img_gray)
cv2.imshow('image_thresh',thresh)
cv2.waitKey(0)


# - 80 (threshold value)
# - Any pixel intensity greater than 80 will be set to the maximum value (here 255).
# - Any pixel intensity less than or equal to 80 will be set to 0.

# - 255 (max value)
# - The value assigned to pixels that pass the threshold condition.
# - In binary thresholding, this is usually 255 (white).

# - THRESH_BINARY means:
# - Pixel > threshold → set to max value (255)
# - Pixel ≤ threshold → set to 0

# Return Values
# • 	
# • 	The threshold value used (in this case, it will just be 80).
# • 	Useful if you use automatic methods like .
# • 	
# • 	The output binary image after thresholding.
# • 	Same size as , but only contains 0s and 255s.