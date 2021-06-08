#!/bin/bash
#IP=$(ifconfig | grep wl -A 1 | grep inet | awk '{print $2}')
IP=192.168.2.101
SHORESIDE_IP=192.168.2.103
export ROS_IP=$IP
#export ROS_MASTER_URI=http://192.168.1.102:11311
export ROS_MASTER_URI=http://$SHORESIDE_IP:11311
printenv | grep ROS
ifconfig
