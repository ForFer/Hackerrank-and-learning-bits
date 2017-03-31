"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/count-the-balls
"""

# Small remark: this does not compile on hrank, as they do not provide openCV
# support, but, if the did, this script looks for circles using HoughCircles on
# a grey img (cv2.Canny makes the change to grey)

import cv2 
import cv2.cv
import numpy as np
import matplotlib.pyplot as plt 
import math

def detect(img):
    img_g = np.zeros( (img.shape[0], img.shape[1]), dtype=np.uint8 )
    img_g[:,:] = img[:,:,0]

    h_threshold = 100 
    l_threshold = 50
    edges = cv2.Canny(img_g, h_threshold, l_threshold)   
    
    circles = cv2.HoughCircles(img_g, cv2.cv.CV_HOUGH_GRADIENT, dp=1,minDist=75,\
        param1=60, param2=27, minRadius=30, maxRadius=70
        )
    print(len(circles))

def parse_line(line):
    temp = []
    for l in line:
        temp.append(map(int,l.split(',')))
    return temp

stop = False
img = []
try:
    while True:
        line = [x for x in raw_input().split()]
        if len(line) != 0:
            img.append(parse_line(line))
        else:
            break
except EOFError:
    detect(img)

