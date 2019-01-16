#!/usr/bin/env python
import rospy
from ros_basics.msg import IoTSensor

def iot_callback(message):
    rospy.loginfo('new IoT data received:')
    rospy.loginfo('id:%d, name:%s, temp:%f, hum:%f'%(message.id, message.name, message.temperature, message.humidity))

def iot_subscriber():
    rospy.init_node('iot_sensor_subscriber_node', anonymous = True)
    rospy.Subscriber('iot_sensor_topic', IoTSensor, iot_callback)
    rospy.spin()

if __name__ == '__main__':
    iot_subscriber()    