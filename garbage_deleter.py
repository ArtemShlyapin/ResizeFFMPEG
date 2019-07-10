#!/usr/bin/python3
import os

j = 0

while (os.path.isfile('output_' + '{n:04d}'.format(n = j) + '.avi')):
    os.remove('output_' + '{n:04d}'.format(n = j) + '.avi')
    j += 1

j = 0

while (os.path.isfile('new_' + '{n:04d}'.format(n = j) + '.avi')):
    os.remove('new_' + '{n:04d}'.format(n = j) + '.avi')
    j += 1