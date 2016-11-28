import numpy as np
import cv2

ip= 'http://192.168.0.62:8080/videofeed'

cap = cv2.VideoCapture(0)

if cap.isOpened()==False:
    cap.open(ip)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()