#!/usr/bin/python3
import ffmpeg
import os

j = 0

while True:  #search for already resized files to save order of resizing
    if (os.path.isfile('new_' + '{n:04d}'.format(n = j) + '.avi')) == True:
        j += 1
    else:
        break
    

while True:
    if (os.path.isfile('output_' + '{n:04d}'.format(n= j + 1) + '.avi')): #check for files to resize
        if (os.path.isfile('output_' + '{n:04d}'.format(n=j) + '.avi')):

            old = ffmpeg.input('output_' + '{n:04d}'.format(n= j) + '.avi')
            new = ffmpeg.output(old, 'new_' + '{n:04d}'.format(n= j) + '.avi', s = '360x240') #resizing and creating new_0000.avi in 240x240 size
            ffmpeg.run(new)
            j += 1
