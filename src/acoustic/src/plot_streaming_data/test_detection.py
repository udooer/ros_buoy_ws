#!/usr/bin/env python3
# import python library
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time 
import copy
import math

# import ROS library
import rospy
from ntu_msgs.msg import HydrophoneFFTDataWithClickRemoval, DetectionImage, HydrophoneData

class plot_detection_result_node:
    def __init__(self):
        self.count_F = 0
        self.count_D = 0
        self.count_C = 0
        rospy.Subscriber("/detect_whistle/detection_image", DetectionImage, self.push_detection_data)
        rospy.Subscriber("/compute_fft/two_mode_fft_data", HydrophoneFFTDataWithClickRemoval, self.push_fft_data)
        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback)
        self.fig, self.ax = plt.subplots(2, 2, figsize=(20,6))

    def push_detection_data(self, data):
        self.count_D += 1
        
    def push_fft_data(self, data):
        self.count_F += 1
    def callback(self, data):
        self.count_C += 1

    def animate(self, i):  
        print("count D: {}".format(self.count_D))
        print("count F: {}".format(self.count_F))
        print("count C: {}".format(self.count_C))

def main():
    rospy.init_node("plot_streaming_data_node", anonymous=True)
    plot_node = plot_detection_result_node()
    # ani = FuncAnimation(plot_node.fig, plot_node.animate, interval=plot_node.INTERVAL_)
    ani = FuncAnimation(plot_node.fig, plot_node.animate, interval=1000)
    plt.show()
    rospy.spin()

if __name__ == "__main__":
    main()
