#!/usr/bin/env sh
IP=192.168.`(ifconfig | grep wlan0 -A 1 | grep inet | awk '{print $2}'| cut -d"." -f 3-4)`
export ROS_IP=$(IP)
export ROS_MASTER_URI=http://192.168.1.102:11311
