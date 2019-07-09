#!/usr/bin/python
import numpy as np
import cv2
import os

j = 1

while True:
    if (os.path.isfile('new_' + '{n:04d}'.format(n = j) + '.avi')) != True:
        break
    j += 1

while True:
    if (os.path.isfile('new_' + '{n:04d}'.format(n = j - 1) + '.avi')):
        if (os.path.isfile('new_' + '{n:04d}'.format(n = j) + '.avi')):
            
            cap = cv2.VideoCapture('new_' + '{n:04d}'.format(n = j - 1) + '.avi')

            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret==True:
                    cv2.imshow('framte',frame)

                    if cv2.waitKey(30) & 0xFF == ord('q'):
                        break
                else:
                    break

            cap.release()
            cv2.destroyAllWindows()
            j += 1
            print(j)
