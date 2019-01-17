#!/usr/bin/env python

from __future__ import division
import math
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
turtlesim_pose = Pose()

def poseCallback(pose_message):
    global turtlesim_pose

    turtlesim_pose.x = pose_message.x
    turtlesim_pose.y = pose_message.y
    turtlesim_pose.theta = pose_message.theta

def deg_to_rad(degrees):
    return (math.pi/180)*degrees

def move(speed, distance, IsForward):
    global velocity_publisher

    vel_msg = Twist()
    if IsForward:
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    rospy.init_node('robot_cleaner', anonymous = True)
    rate = rospy.Rate(100)
    t0 = rospy.get_time()
    current_distance = 0

    while current_distance < distance:
        velocity_publisher.publish(vel_msg)
        current_distance = speed*(rospy.get_time()-t0)
        rate.sleep()
    
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

def rotate(angular_speed, relative_angle, clockwise):
    global velocity_publisher

    vel_msg = Twist()
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)

    rospy.init_node('robot_cleaner', anonymous = True)
    rate = rospy.Rate(100)
    t0 = rospy.get_time()
    current_angle = 0

    while current_angle < relative_angle:
        velocity_publisher.publish(vel_msg)
        current_angle = angular_speed*(rospy.get_time()-t0)
        rate.sleep()
    
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def setDesiredOrientation(desired_angle):
    global turtlesim_pose
    
    relative_angle = desired_angle - turtlesim_pose.theta
    print desired_angle
    print turtlesim_pose.theta
    print relative_angle
    if relative_angle < 0:
        clockwise = True
    else:
        clockwise = False
    rotate(deg_to_rad(30), abs(relative_angle), clockwise)

def main():
    try:
        pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, poseCallback)
        
        rospy.loginfo('**************STARTING TEST************')
    
        s = input('Enter the speed:')
        d = input('Enter the distance:')
        f = input('Moving forward, True or False?')

        ang_s = input('Enter the angular speed:')
        rel_a = input('Enter the desired angle:')
        cw = input('Moving clockwise, True or False?')

        move(s,d, f)
        rotate(deg_to_rad(ang_s), deg_to_rad(rel_a), cw)
        setDesiredOrientation(deg_to_rad(90))

    except Exception, e:
        print 'A error has occured:%s'%e


if __name__ == '__main__':
    main()
    