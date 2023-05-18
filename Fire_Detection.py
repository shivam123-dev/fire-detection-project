import cv2
import numpy as np
import winsound
cap = cv2.VideoCapture(0) 
lower_cutoff = np.array([0, 150, 150])
upper_cutoff = np.array([10, 255, 255])
while True:
    ret, fr = cap.read()
    fr = cv2.resize(fr, (640, 480))
    hv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)
    mk = cv2.inRange(hv, lower_cutoff, upper_cutoff)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mk = cv2.erode(mk, k, iterations=2)
    mk = cv2.dilate(mk, k, iterations=4)
    cntr, hCntr = cv2.findContours(mk, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(cntr) > 0:
        x, y, w, h = cv2.boundingRect(cntr[0])
        cv2.rectangle(fr, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print('Fire Detected')
        f = 1000
        s = 500
        winsound.Beep(f, s)
    cv2.imshow('Fire Detection', fr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()