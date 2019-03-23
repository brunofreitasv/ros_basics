cmake_minimum_required(VERSION 2.8.3)
project(ros_basics)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  actionlib_msgs
  cv_bridge
  image_transport
  message_generation
  roslaunch
)


## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   IoTSensor.msg
)

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   AddTwoInts.srv
   )

## Generate actions in the 'action' folder
#add_action_files(
#  DIRECTORY action
#  FILES
#)

## Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   std_msgs
#   actionlib_msgs
#  )


###################################
## catkin specific configuration ##
###################################
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ros_essentials_cpp
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
#  ${OpenCV_INCLUDE_DIRS}
)

roslaunch_add_file_check(launch)
