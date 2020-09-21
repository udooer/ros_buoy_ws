#!/usr/bin/env python3 
import matplotlib.pyplot as plt
import numpy as np

# ros python 
import rospy
from ntu_msgs.msg import HydrophoneData
class streaming_plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([],[],'b-')
        self.ax.set_xlabel("Time(s)")
        self.ax.set_ylabel("Voltage(volt)")
        self.ax.set_title("Streaming plot for Hydrophone data")
        self.ax.grid(True)
    def update(self, x ,y):
        self.line.set_data(x, y)
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

class plot_hydrophone_data_node:
    def __init__(self):
        # init the streaming plot
        self.s_plot_ch1 = streaming_plot()
        self.s_plot_ch1.ax.set_title("Streaming plot for Hydrophone data CH1")
        self.s_plot_ch2 = streaming_plot()
        self.s_plot_ch2.ax.set_title("Streaming plot for Hydrophone data CH2")
        self.plot_length = 1 # total plot length(sec) showed on the plot
        self.count = 0 # counting for adding time 
        
        self.data_frame_ch1 = np.array([]) # node container for data 
        self.data_frame_ch2 = np.array([])
        self.fs = 96000 
        self.data_length = 9600
        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback)   


    def callback(self, data):
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
        time = np.arange(len(self.data_frame_ch1))/self.fs + self.count*self.data_length/self.fs
        self.s_plot_ch1.update(time, self.data_frame_ch1)
        self.s_plot_ch2.update(time, self.data_frame_ch2)

def main():
    rospy.init_node('plot_hydrophone_data_node', anonymous=True)
    plt.ion()
    pn = plot_hydrophone_data_node()
    rospy.spin()

if __name__ == "__main__":
    main()
