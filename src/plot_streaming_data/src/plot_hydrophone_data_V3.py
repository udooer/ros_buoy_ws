#!/usr/bin/env python3 
import matplotlib.pyplot as plt
import numpy as np
import time

# ros python 
import rospy
from ntu_msgs.msg import HydrophoneData
class streaming_plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1,2,figsize=(5,3))
        # plotting element of ch1
        self.line1, = self.ax[0].plot([],[],'b-')
        self.ax[0].set_xlabel("Time(s)")
        self.ax[0].set_ylabel("Voltage(volt)")
        self.ax[0].set_title("Streaming plot for Hydrophone data")
        self.ax[0].grid(True)
        # plotting element of ch2
        self.line2, = self.ax[1].plot([],[],'b-')
        self.ax[1].set_xlabel("Time(s)")
        self.ax[1].set_ylabel("Voltage(volt)")
        self.ax[1].yaxis.set_label_position("right")
        self.ax[1].yaxis.set_ticks_position("right")
        self.ax[1].set_title("Streaming plot for Hydrophone data")
        self.ax[1].grid(True)
    def update_ch1(self, x ,y):
        self.line1.set_data(x, y)
        self.ax[0].relim()
        self.ax[0].autoscale_view(True, True, True)
        
    def update_ch2(self, x ,y):
        self.line2.set_data(x, y)
        self.ax[1].relim()
        self.ax[1].autoscale_view(True, True, True)
    def show(self):
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

class plot_hydrophone_data_node:
    def __init__(self):
        # init the streaming plot
        self.s_plot = streaming_plot()
        self.s_plot.ax[0].set_title("Streaming plot of CH1")
        self.s_plot.ax[1].set_title("Streaming plot of CH2")
        self.plot_length = 1 # total plot length(sec) showed on the plot
        self.count = 0 # counting for adding time 
        
        self.data_frame_ch1 = np.array([]) # node container for data 
        self.data_frame_ch2 = np.array([])
        self.fs = 96000 
        self.data_length = 9600
        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback)   


    def callback(self, data):
        time_start = time.time()
        data_ch1 = np.array(data.data_ch1)/pow(2,31)
        data_ch2 = np.array(data.data_ch2)/pow(2,31)

        self.fs = data.fs
        number = self.fs*self.plot_length
        self.data_frame_ch1 = np.concatenate((self.data_frame_ch1, data_ch1))
        self.data_frame_ch2 = np.concatenate((self.data_frame_ch2, data_ch2))
        if(len(self.data_frame_ch1)>number):
            self.count+=1;
            self.data_frame_ch1 = self.data_frame_ch1[-number:]
            self.data_frame_ch2 = self.data_frame_ch2[-number:]
        t = np.arange(len(self.data_frame_ch1))/self.fs + self.count*self.data_length/self.fs
        self.s_plot.update_ch1(t, self.data_frame_ch1)
        self.s_plot.update_ch2(t, self.data_frame_ch2)
        self.s_plot.show()
        time_end = time.time()
        print("update plot using time: ", time_end-time_start)

def main():
    rospy.init_node('plot_hydrophone_data_node', anonymous=True)
    plt.ion()
    pn = plot_hydrophone_data_node()
    rospy.spin()

if __name__ == "__main__":
    main()
