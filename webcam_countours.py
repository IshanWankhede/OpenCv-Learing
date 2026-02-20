import cv2

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(frame_gray, 127, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 100:
            # cv2.drawContours(frame, cnt, -1, (0, 0, 255), 3)

            x1, y1, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(frame, (x1,y1), (x1 + w,y1 + h), (0,255,0), 2)

    cv2.imshow('frame', frame) 

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break  

webcam.release()
cv2.destroyAllWindows()