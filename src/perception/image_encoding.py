#!/usr/bin/env python

from __future__ import division
import numpy as np
import cv2
     
def main():
    image_name = 'tree'
 
    print 'read image from file'
    color_img = cv2.imread('images/'+image_name+'.jpg', cv2.IMREAD_COLOR)
    
    print 'display the image in native color'
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.imshow('Original image', color_img)
    cv2.moveWindow('Original Image', 0, 0)
    print color_img.shape
    height, width, channel = color_img.shape
    
    print 'Split the image into Red, Green and Blue channels'
    red, green, blue = cv2.split(color_img)
    rgb_image = np.concatenate((red, green, blue), axis = 1)
    cv2.namedWindow('Red, Green, Blue image', cv2.WINDOW_NORMAL)
    cv2.imshow('Red, Green, Blue image', rgb_image)
    cv2.moveWindow('Red, Green, Blue image', 0, height)
    
    print 'Split the image into Hue, Saturation and Value channels'
    hsv = cv2.cvtColor(color_img, cv2.COLOR_BGR2HSV)
    hue, sat, value = cv2.split(hsv)
    hsv_image = np.concatenate((hue, sat, value), axis = 1)
    cv2.namedWindow('Hue, Saturation, Value image', cv2.WINDOW_NORMAL)
    cv2.imshow('Hue, Saturation, Value image', hsv_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()