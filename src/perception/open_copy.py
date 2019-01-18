#!/usr/bin/env python

from __future__ import division
import numpy as np
import cv2
     
def main():
   image_name = 'ball'

   print 'read image from file'
   img = cv2.imread('images/'+image_name+'.jpeg')

   print 'create a window holder for the image'
   cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

   print 'display the image'
   cv2.imshow('Image', img)

   print 'press a key inside the image to make a copy'
   cv2.waitKey(0)

   print 'image copied to the folder images/copy/'
   cv2.imwrite('images/copy/'+image_name+'-copy.jpg', img)

if __name__ == '__main__':
    main()
    