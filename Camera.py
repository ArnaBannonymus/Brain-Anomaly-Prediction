# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 13:22:02 2018

@author: Arnab Bhowmik
"""

import cv2
import numpy as np
cap=cv2.VideoCapture(1)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #hsv hue sat value
    lower_red=np.array([0,0,0])
    upper_red=np.array([255,255,255])
    
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,mask=mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k=cv2.waitKey(5) & 0xFF
    if (k==27):
        break
    
cv2.destroyAllWindows()
cap.release()
        