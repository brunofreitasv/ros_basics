#!/usr/bin/env python

from __future__ import division
import numpy as np
import cv2

def read_image(image_name, show = False):
    rgb_img = cv2.imread(image_name)
    if show:
        print 'display original image'
        cv2.namedWindow('RGB image', cv2.WINDOW_NORMAL)
        cv2.imshow('RGB image', rgb_img)
    return rgb_img

def rgb_to_grey(rgb_image, show = False):
    grey_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    if show:
        print 'display gray image'
        cv2.namedWindow('Grey image', cv2.WINDOW_NORMAL)
        cv2.imshow('Grey image', grey_image)
    return grey_image

def grey_to_binary(grey_image, adaptive, show = False):
    if adaptive:
        binary_image = cv2.adaptiveThreshold(grey_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 155, 2)
    else: 
        ret, binary_image = cv2.threshold(grey_image, 127, 255, cv2.THRESH_BINARY_INV)
    if show:
        print 'display binary image'    
        cv2.namedWindow('Binary image', cv2.WINDOW_NORMAL)
        cv2.imshow('Binary image', binary_image)
    return binary_image

def getContours(binary_image):
    _, contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def get_contour_center(contour):
    M = cv2.moments(contour)
    cx=-1
    cy=-1
    if (M['m00']!=0):
        cx= int(M['m10']/M['m00'])
        cy= int(M['m01']/M['m00'])
    return cx, cy

def draw_contours(image, contours, image_name):
    index = -1
    thickness = 2
    color = (0, 255, 0)
    cv2.drawContours(image, contours, index, color, thickness)
    print 'display contour image'    
    cv2.namedWindow(image_name, cv2.WINDOW_NORMAL)
    cv2.imshow(image_name, image)

def process_contours(binary_image, rgb_image, contours):
    black_image = np.zeros([binary_image.shape[0], binary_image.shape[1],3],'uint8')
    
    for c in contours:
        area = cv2.contourArea(c)
        perimeter= cv2.arcLength(c, True)
        if area > 300:
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            cv2.drawContours(rgb_image, [c], -1, (150,250,150), 1)
            cv2.drawContours(black_image, [c], -1, (150,250,150), 1)
            cx, cy = get_contour_center(c)
            cv2.circle(rgb_image, (cx,cy),int(radius+1),(0,0,255),2)
            cv2.circle(black_image, (cx,cy),int(radius+1),(0,0,255),2)
    print 'number of contours: {}'.format(len(contours))
    cv2.namedWindow('RGB Image Contours', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Black Image Contours', cv2.WINDOW_NORMAL)
    cv2.imshow('RGB Image Contours',rgb_image)
    cv2.imshow('Black Image Contours',black_image)

def main():
    image_name = 'images/flower.jpg'
         
    rgb_img = read_image(image_name, True)
    grey_img = rgb_to_grey(rgb_img, True)
    bin_img = grey_to_binary(grey_img, True, True)
    contours = getContours(bin_img)
    process_contours(bin_img, rgb_img, contours)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows

if __name__ == '__main__':
    main()