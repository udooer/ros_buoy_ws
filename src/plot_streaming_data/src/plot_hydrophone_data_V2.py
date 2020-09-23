#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import time 
# import ros library
import rospy
from ntu_msgs.msg import HydrophoneData


class plot_hydrophone_data_node:
    def __init__(self):
        self.data_frame_ch1 = np.array([]) # node container for data 
        self.data_frame_ch2 = np.array([])
        self.fs = 96000 
        self.data_length = 9600

        # plot setting
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([],[],'b-')
        self.ax.set_xlabel("Time(s)")
        self.ax.set_ylabel("Voltage(volt)")
        self.ax.set_title("Streaming plot for Hydrophone data")
        self.ax.grid(True)
        

        self.plot_length = 1 # frame length(sec) in the plot
        self.count = 0 # set the adding time  
        self.time = np.array([])
        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback)

    # after we get the data from ros master put it inside our container 
    def callback(self, data):
        
        data_ch1 = np.array(data.data_ch1)/pow(2,31)
        # data_ch2 = np.array(data.data_ch2)/pow(2,31)

        self.fs = data.fs
        number = self.fs*self.plot_length
        self.data_frame_ch1 = np.concatenate((self.data_frame_ch1, data_ch1))
        # self.data_frame_ch2 = np.concatenate((self.data_frame_ch2, data_ch2))
        if(len(self.data_frame_ch1)>number):
            self.count+=1;
            self.data_frame_ch1 = self.data_frame_ch1[-number:]
            # self.data_frame_ch2 = self.data_frame_ch2[-number:]
        
        # update the data on the plot
        time_start = time.time() 
        t = np.arange(len(self.data_frame_ch1))/self.fs + self.count*self.data_length/self.fs
        self.line.set_data(t, self.data_frame_ch1)
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        time_end = time.time()
        print("time consuming: ", time_end-time_start, "sec")

def main():
    rospy.init_node('plot_hydrophone_data_node', anonymous=True)
    plt.ion()
    pn = plot_hydrophone_data_node()
    rospy.spin()

if __name__ == "__main__":
    main()
