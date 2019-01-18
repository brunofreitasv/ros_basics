#!/usr/bin/env python

from __future__ import division
import numpy as np
import cv2
     
def main():
    image_name = 'ball'
 
    print 'read image from file'
    color_img = cv2.imread('images/'+image_name+'.jpeg')
    
    print 'display the image in native color'
    cv2.namedWindow('Original image', cv2.WINDOW_NORMAL)
    cv2.imshow('Original image', color_img)
    cv2.moveWindow('Original Image', 0, 0)
        
    #Split the image into Hue, Saturation and Value channels
    print 'display the HSV image'
    hsv = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
    cv2.namedWindow('HSV image', cv2.WINDOW_NORMAL)
    cv2.imshow('HSV image', hsv)

    magLower = (150, 100, 50)
    magUpper = (180, 255, 255)

    #creating a mask for the image
    print 'display the mask image'
    mask = cv2.inRange(hsv, magLower, magUpper)
    cv2.namedWindow('Mask image', cv2.WINDOW_NORMAL)
    cv2.imshow('Mask image', mask)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()