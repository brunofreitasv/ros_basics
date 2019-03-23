#!/usr/bin/env python

from __future__ import division
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import numpy as np
import cv2
import cv_bridge as cvb

def image_callback(image_message):
    try:
        cv_image = bridge.imgmsg_to_cv2(image_message, 'bgr8')
    except cvb.CvBridgeError as e:
        print e

    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    frontal = face_frontal.detectMultiScale(gray, 1.3, 5)
    profile = face_profile.detectMultiScale(gray, 1.3, 5)
    

    if frontal is not ():
        for (x,y,h,w) in frontal:
            cv2.rectangle(cv_image, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(cv_image, "Face", (x,y-1), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,255,0), 2)
    elif profile is not ():
        for (x,y,h,w) in profile:
            cv2.rectangle(cv_image, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(cv_image, "Face", (x,y-1), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,255,0), 2)
    else:
        print "No faces found!"

    cv2.imshow('Faces', cv_image)
    cv2.waitKey(3)

def main():
    rospy.init_node('image_node', anonymous = True)
    rospy.Subscriber('/usb_cam/image_raw', Image, image_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print 'Shutting down'

    cv2.destroyAllWindows()

if __name__ == '__main__':
    bridge = cvb.CvBridge()
    face_frontal = cv2.CascadeClassifier('/home/brunofreitas/catkin_ws/src/ros_basics/src/perception/Faces/haarcascades/haarcascade_frontalface_default.xml')
    face_profile = cv2.CascadeClassifier('/home/brunofreitas/catkin_ws/src/ros_basics/src/perception/Faces/haarcascades/haarcascade_profileface.xml')

    main()