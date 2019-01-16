#!/usr/bin/env python
import rospy
from ros_basics.msg import IoTSensor
import random

def iot_publisher():
    rospy.init_node('iot_sensor_publisher_node', anonymous = True)
    pub = rospy.Publisher('iot_sensor_topic', IoTSensor, queue_size = 10)
    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        iot_sensor = IoTSensor()
        iot_sensor.id = i
        iot_sensor.name = 'iot_parking_%d'%i
        iot_sensor.temperature = 24.33 + (random.random()*2)
        iot_sensor.humidity = 33.41 + (random.random()*2)
        rospy.loginfo('I publish:')
        rospy.loginfo(iot_sensor)
        pub.publish(iot_sensor)
        rate.sleep()
        i += 1

if __name__ == '__main__':
    try:
        iot_publisher()
    except rospy.ROSInterruptException:
        pass
