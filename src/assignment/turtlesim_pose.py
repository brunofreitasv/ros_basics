#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def poseCallback(pose_message):
    print 'pose callback'
    print 'x = %f'%pose_message.x
    print 'y = %f' %pose_message.y
    print 'yaw = %f'%pose_message.theta 

if __name__ == '__main__':
    try:
        rospy.init_node('turtlesim_motion_pose', anonymous=True)        
        rospy.Subscriber('/turtle1/pose', Pose, poseCallback)
        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")