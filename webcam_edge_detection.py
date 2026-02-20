import os

import cv2

import numpy as np 

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    frame_edge = cv2.Canny(frame, 100, 200)

    cv2.imshow('frame', frame)

    cv2.imshow('frame_edge', frame_edge)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()
