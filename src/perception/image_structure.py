#!/usr/bin/env python

from __future__ import division
import numpy as np
import cv2
     
def main():
    image_name = 'chess'
 
    print 'read image from file'
    img = cv2.imread('images/'+image_name+'.png')
 
    print 'display the content of the image'
    print img

    print 'type of the image type(img): %s'%type(img)
    print 'size of the image img.size: %d'%img.size
    print 'shape of the image img.shape: (%d, %d, %d)'%img.shape

if __name__ == '__main__':
    main()