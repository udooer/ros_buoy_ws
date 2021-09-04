#!/bin/bash
#IP=$(ifconfig | grep wl -A 1 | grep inet | awk '{print $2}')
source /home/ual/ros_buoy_ws/devel/setup.bash
IP=192.168.2.102
SHORESIDE_IP=192.168.2.100
export ROS_IP=$IP
#export ROS_MASTER_URI=http://192.168.1.102:11311
export ROS_MASTER_URI=http://$IP:11311
ifconfig
printenv | grep ROS
sudo sh -c "echo 0 >/proc/sys/net/ipv4/icmp_echo_ignore_broadcasts"
cat /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts

