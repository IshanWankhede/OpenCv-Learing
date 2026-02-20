import os

import cv2

img = cv2.imread(os.path.join('.','data','Whiteboard.jpg'))

print(img.shape)

#line
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

#cv2.line(img, (x1,y1), (x2,y2), (color bgr), thinkness)

#rectangle
cv2.rectangle(img, (100, 250), (350, 400), (0, 0, 255), 3)
#cv2.rectangle(img, (x1,y1), (x2,y2), (color bgr), thinkness)   to fill the complerectangle put thickness value as -1

#circle
cv2.circle(img, (120, 200), 150, (255, 0, 0), 10)
# cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None)

#text 
cv2.putText(img, 'Ishan Wankhede', (100,100), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255,0), 3)
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)

cv2.imshow('img', img)
cv2.waitKey(0)