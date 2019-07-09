#!/usr/bin/python
import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
i = 0
j = 0

while True:
    if (os.path.isfile('output_' + '{n:04d}'.format(n = j) + '.avi')) != True:
        break
    j += 1

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output_' + '{n:04d}'.format(n=j) + '.avi',fourcc, 25.0, (640,480))
#out = cv2.VideoWriter('output.jpeg', -1, 2.0, (640,480))

while (cap.isOpened()):
    i += 1
    print(i)
    ret, frame = cap.read()
    print(frame.__class__) #<type 'numpy.ndarray'>
    if ret==True:
        frame = cv2.flip(frame,1)

        # write the flipped frame
        #frame = fmpeg.input('output.avi4')
        if i > 100:
            j += 1
            i = 0
            out = cv2.VideoWriter('output_' + '{n:04d}'.format(n=j) + '.avi',fourcc, 25.0, (640,480))
        out.write(frame)

        cv2.imshow('fram',frame)
        #frame = fmpeg.input('output.avi4')
        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
