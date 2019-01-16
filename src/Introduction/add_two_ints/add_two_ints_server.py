#!/usr/bin/env python
import rospy
from ros_basics.srv import AddTwoInts
from ros_basics.srv import AddTwoIntsRequest
from ros_basics.srv import AddTwoIntsResponse

def handle_two_ints(req):
    print 'Returning: %d + %d = %d'%(req.x, req.y, req.x + req.y)
    resp = AddTwoIntsResponse(req.x + req.y)
    return resp
    

def add_two_ints_server():
    rospy.init_node('add_two_ints_server', anonymous = True)
    rospy.Service('add_two_ints', AddTwoInts, handle_two_ints)
    rospy.loginfo("I'm ready to add two integers")
    rospy.spin()

if __name__ == '__main__':
    add_two_ints_server()    