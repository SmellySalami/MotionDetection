import cv2
import numpy as np
import time
import imutils

cap = cv2.VideoCapture(0)
x = 7
a=0

while True:
    a = a + 1
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(25,25),0)

    if x > 5:
        x = 0
        frame1 = gray

    diff = cv2.absdiff(frame1, gray)
    ret, diff = cv2.threshold(diff, 12, 255, cv2.THRESH_BINARY)

    if cv2.countNonZero(diff)!=0:
        print(a)


    # thresh = cv2.dilate(thresh, None, iterations=2)
    # (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('leooo', gray)
    cv2.imshow('sdf', diff)

    x = x+1

    if cv2.waitKey(1) & 0xff == ord ('q'):
        break


cap.release()
cv2.destroyAllWindows()

#
# x = 0
# while True:
#     print(x)
#     x = x + 1
#     if x>90000:
#         break