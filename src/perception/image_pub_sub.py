#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import numpy as np
import cv2
import cv_bridge as cvb
import sys

def image_callback(image_message):
    print 'got an image'
    global bridge

    try:
        cv_image = bridge.imgmsg_to_cv2(image_message, 'bgr8')
    except cvb.CvBridgeError as e:
        print e
    height, width, channels = cv_image.shape
    if width > 200 and height > 200:
        cv2.rectangle(cv_image,(100, 100),(190, 190), (0, 255, 0), 3)
    text = "Bruno's web cam using ROS and OpenCV"
    cv2.putText(cv_image, text, (10, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('Camera image', cv_image)
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