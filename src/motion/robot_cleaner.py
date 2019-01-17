#!/usr/bin/env python

from __future__ import division
import math
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def poseCallback(pose_message):
    turtlesim_pose.x = pose_message.x
    turtlesim_pose.y = pose_message.y
    turtlesim_pose.theta = pose_message.theta

def deg_to_rad(degrees):
    return (math.pi/180)*degrees

def getDistance(x, y, xl, yl):
    return abs(math.sqrt((xl-x)**2 + (yl-y)**2))

def move(speed, distance, IsForward):
    vel_msg = Twist()
    if IsForward:
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)

    rate = rospy.Rate(100)
    t0 = rospy.get_time()
    current_distance = 0

    while True:
        velocity_publisher.publish(vel_msg)
        current_distance = speed*(rospy.get_time()-t0)
        rate.sleep()
        if current_distance >= distance:
            break
    
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

def rotate(angular_speed, relative_angle, clockwise):
    vel_msg = Twist()
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)

    rate = rospy.Rate(100)
    t0 = rospy.get_time()
    current_angle = 0

    while True:
        velocity_publisher.publish(vel_msg)
        current_angle = angular_speed*(rospy.get_time()-t0)
        rate.sleep()
        if current_angle >= relative_angle:
            break
    
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def setDesiredOrientation(desired_angle):
    relative_angle = desired_angle - turtlesim_pose.theta
    print desired_angle
    print turtlesim_pose.theta
    print relative_angle
    if relative_angle < 0:
        clockwise = True
    else:
        clockwise = False
    rotate(deg_to_rad(30), abs(relative_angle), clockwise)

def moveGoal(goal_position, distance_tolerance):
    vel_msg = Twist()
    rate = rospy.Rate(100)

    while True:
        distance = getDistance(turtlesim_pose.x, turtlesim_pose.y, goal_position.x, goal_position.y)
        vel_msg.linear.x = 0.5*distance
        vel_msg.angular.z = 4*(math.atan2(goal_position.y-turtlesim_pose.y, goal_position.x-turtlesim_pose.x)-turtlesim_pose.theta)
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        if distance < distance_tolerance:
            break

    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def spiralClean():
    vel_msg = Twist()
    rate = rospy.Rate(10)
    rk = 0
    
    while True:
        rk += 0.15
        vel_msg.linear.x = rk
        vel_msg.angular.z = 4.0
        velocity_publisher.publish(vel_msg)
        rate.sleep()       
        if turtlesim_pose.x >= 10.5 or turtlesim_pose.y >= 10.5:
            break
    
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def gridClean():
    des_pose = Pose()
    des_pose.x = 1
    des_pose.y = 1
    des_pose.theta = 0
 
    moveGoal(des_pose, 0.01)
   
    setDesiredOrientation(deg_to_rad(des_pose.theta))
    
    move(2.0, 9.0, True)
    rotate(deg_to_rad(20), deg_to_rad(90), False)
    
    while turtlesim_pose.x > 1:
        move(2.0, 9.0, True)
        rotate(deg_to_rad(20), deg_to_rad(90), False)
        move(2.0, 1.0, True)
        rotate(deg_to_rad(20), deg_to_rad(90), False)
        move(2.0, 9.0, True)
        rotate(deg_to_rad(30), deg_to_rad(90), True)
        move(2.0, 1.0, True)
        rotate(deg_to_rad(30), deg_to_rad(90), True)
     
def main():
    try:
        rospy.loginfo('**************STARTING TEST************')
        
        rate = rospy.Rate(0.5)

        '''
        goal_pose = Pose()
        goal_pose.x = 1
        goal_pose.y = 1
        moveGoal(goal_pose, 0.01)
        rate.sleep()
        setDesiredOrientation(deg_to_rad(0))
        rate.sleep()

        s = input('Enter the speed:')
        d = input('Enter the distance:')
        f = input('Moving forward, True or False?')

        ang_s = input('Enter the angular speed:')
        rel_a = input('Enter the desired angle:')
        cw = input('Moving clockwise, True or False?')

        move(s,d, f)
        rate.sleep()
        rotate(deg_to_rad(ang_s), deg_to_rad(rel_a), cw)
        rate.sleep()

        goal_pose.x = 5.5
        goal_pose.y = 5.5
        moveGoal(goal_pose, 0.01)
        rate.sleep()
        setDesiredOrientation(deg_to_rad(0))
        rate.sleep()
        spiralClean()
        '''

        gridClean()
        

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")

if __name__ == '__main__':
    rospy.init_node('robot_cleaner', anonymous = True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, poseCallback)
    turtlesim_pose = Pose()
    main()
    