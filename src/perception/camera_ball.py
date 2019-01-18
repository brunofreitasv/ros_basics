#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import numpy as np
import cv2
import cv_bridge as cvb

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

def rgb_to_hsv(rgb_image, show = False):
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    if show:
        print 'display hsv image'
        cv2.namedWindow('HSV image', cv2.WINDOW_NORMAL)
        cv2.imshow('HSV image', hsv_image)
    return hsv_image

def create_mask(hsv_image, colorLower, colorUpper, show = False):
    mask = cv2.inRange(hsv_image, colorLower, colorUpper)
    if show:
        print 'display the mask image'
        cv2.namedWindow('Mask image', cv2.WINDOW_NORMAL)
        cv2.imshow('Mask image', mask)
    return mask

def grey_to_binary(grey_image, adaptive, show = False):
    if adaptive:
        binary_image = cv2.adaptiveThreshold(grey_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)
    else: 
        ret, binary_image = cv2.threshold(grey_image, 127, 255, cv2.THRESH_BINARY)
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

def process_contours(binary_image, rgb_image, contours, show = False):
    for c in contours:
        area = cv2.contourArea(c)
        perimeter= cv2.arcLength(c, True)
        if area > 150:
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            #cv2.drawContours(rgb_image, [c], -1, (150,250,150), 2)
            cx, cy = get_contour_center(c)
            cv2.circle(rgb_image, (cx,cy),int(radius+1),(0,255,0),3)
    if show:
        print 'number of contours: {}'.format(len(contours))
        cv2.namedWindow('RGB Image Contours', cv2.WINDOW_NORMAL)
        cv2.imshow('RGB Image Contours',rgb_image)
    return rgb_image

def image_callback(image_message):
    global bridge

    try:
        cv_image = bridge.imgmsg_to_cv2(image_message, 'bgr8')
    except cvb.CvBridgeError as e:
        print e

    magLower = (160, 150, 110)
    magUpper = (180, 250, 250)
         
    hsv_img = rgb_to_hsv(cv_image)
    mask_img = create_mask(hsv_img, magLower, magUpper)
    contours = getContours(mask_img)
    rgb_contour = process_contours(mask_img, cv_image, contours)

    cv2.imshow('Camera image', rgb_contour)
    cv2.waitKey(3)

def main():
    rospy.init_node('image_node', anonymous = True)
    image_subscriber = rospy.Subscriber('/usb_cam/image_raw', Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print 'Shutting down'

    cv2.destroyAllWindows()

if __name__ == '__main__':
    bridge = cvb.CvBridge()
    main()