#!/usr/bin/env python

from __future__ import division
import numpy as np
import cv2
     
def main(name):
    image_name = name
 
    print 'read image from file'
    color_img = cv2.imread('images/'+image_name+'.jpg', cv2.IMREAD_COLOR)
    grey_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original image', color_img)

    print 'Thresholding the image'
    ret, simplethre_img = cv2.threshold(grey_img, 155, 255, cv2.THRESH_BINARY)
    cv2.imshow('Basic binary image', simplethre_img)

    adapthre_img = cv2.adaptiveThreshold(grey_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 2)
    cv2.imshow('Adaptive binary image', adapthre_img)

    print color_img.shape
    print simplethre_img.shape
    print adapthre_img.shape
    '''
    print 'Comparing the images'
    comp_image = np.concatenate((color_img, simplethre_img, adapthre_img), axis = 1)
    cv2.imshow('Original, Basic Binary, Adaptive Binary image', comp_image)
    '''
    print 'Press any key to save the binary images as a copy'        
    cv2.waitKey(0)
    cv2.imwrite('images/copy/'+image_name+'-basic.jpg', simplethre_img)
    cv2.imwrite('images/copy/'+image_name+'-adaptive.jpg', adapthre_img)
    cv2.destroyAllWindows

if __name__ == '__main__':
    name = raw_input('Enter the name of the image: ')
    main(name)