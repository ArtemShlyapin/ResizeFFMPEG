#!/usr/bin/python3
import numpy as np
import cv2
import os

i = 0
j = 0

while True: #search for already recorded files to save order of recording
    if (os.path.isfile('output_' + '{n:04d}'.format(n = j) + '.avi')) != True:
        break
    j += 1

codec_DVIX = cv2.VideoWriter_fourcc(*'DIVX') 
out = cv2.VideoWriter('output_' + '{n:04d}'.format(n=j) + '.avi',codec_DVIX, 25.0, (640,480)) # output_0000.avi, DVIX codec, 25fps 640x480 size, 

cap = cv2.VideoCapture(0) #initializing webcam of laptop

while (cap.isOpened()): #recording

    ret, frame = cap.read()
    if ret==True:
    
        i += 1
        if i > 100:  #start new .avi file every 100 frames
            j += 1
            i = 0
            out = cv2.VideoWriter('output_' + '{n:04d}'.format(n=j) + '.avi',codec_DVIX, 25.0, (640,480)) #updating filename, seems like output_0000.avi
        
        out.write(frame)

        cv2.imshow('fram',frame) 

        if cv2.waitKey(1) & 0xFF == ord('q'): # 1ms delay to push stop-button "Q"
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
