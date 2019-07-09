#!/usr/bin/python
import numpy as np
import cv2
import ffmpeg
import os

j = 1

while True:
    if (os.path.isfile('output_' + '{n:04d}'.format(n = j) + '.avi')) != True:
        break
    j += 1

while True:
    if (os.path.isfile('output_' + '{n:04d}'.format(n= j - 1) + '.avi')):
        if (os.path.isfile('output_' + '{n:04d}'.format(n=j) + '.avi')):
            input = ffmpeg.input('output_' + '{n:04d}'.format(n= j - 1) + '.avi')
            input = ffmpeg.output(input, 'new_' + '{n:04d}'.format(n= j - 1) + '.avi', s = '360x240')
            ffmpeg.run(input)
            j += 1
