#!/usr/bin/python3
import numpy as np
import cv2
import os

j = 0

while True: #search for last resized file
    if (os.path.isfile('new_' + '{n:04d}'.format(n = j) + '.avi')) != True: 
        break
    j += 1

while True:
    if (os.path.isfile('new_' + '{n:04d}'.format(n = j + 1) + '.avi')): #check for files to play
        if (os.path.isfile('new_' + '{n:04d}'.format(n = j) + '.avi')):
            
            cap = cv2.VideoCapture('new_' + '{n:04d}'.format(n = j) + '.avi')

            while(cap.isOpened()): #playing

                ret, frame = cap.read()
                if ret==True:
                    cv2.imshow('stream',frame)

                    if cv2.waitKey(33) & 0xFF == ord('q'): # 33ms delay between showing frames and wait time to push stop-button "Q" (fps ~ 30)
                        break
                else:
                    break

            cap.release()
            cv2.destroyAllWindows()
            j += 1
