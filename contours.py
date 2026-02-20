import os
 
import cv2
 
img = cv2.imread(os.path.join('.','data','birds.jpg'))

resized_img = cv2.resize(img, (640,480))

img_gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 600:
        # cv2.drawContours(resized_img, cnt, -1, (0, 0, 255), 3)

        x1, y1, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(resized_img, (x1,y1), (x1 + w,y1 + h), (0,255,0), 2)

cv2.imshow('img', resized_img)
# cv2.imshow('img_gray', img_gray)
cv2.imshow('img_thresh', thresh)
cv2.waitKey(0)


# Key points about contours:
# • 	Definition: A contour is a curve joining all continuous points along a boundary with the same color or intensity.
# • 	Purpose: They are widely used for shape analysis, object detection, and recognition.


# • 	How to find them:
# • 	Usually, you first convert the image to a binary image (object = white, background = black).
# • 	Apply thresholding or Canny edge detection.
# • 	Use  to extract contours.
# • 	Output of :
# • 	Contours → A list of points outlining each detected shape.
# • 	Hierarchy → Information about nested contours (e.g., one shape inside another).


# - for cnt in contours:
# - Loops through each contour found in the image.
# - contours is usually obtained from cv2.findContours().
# - if cv2.contourArea(cnt) > 600:
# - Calculates the area of the contour.
# - Only processes contours larger than 600 pixels (to ignore small noise).
# - cv2.boundingRect(cnt)
# - Finds the smallest upright rectangle that can fully contain the contour.
# - Returns (x1, y1, w, h):
# - x1, y1 → top-left corner of the rectangle
# - w, h → width and height of the rectangle
# - cv2.rectangle(resized_img, (x1,y1), (x1 + w,y1 + h), (0,255,0), 2)
# - Draws a green rectangle ((0,255,0)) around the contour.
# - (x1, y1) is the top-left corner.
# - (x1 + w, y1 + h) is the bottom-right corner.
# - 2 is the thickness of the rectangle border.
