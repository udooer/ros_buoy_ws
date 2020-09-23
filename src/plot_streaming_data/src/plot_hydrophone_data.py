#!/usr/bin/env python3
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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

        self.plot_length = 1 # frame length(sec) in the plot
        self.count = 0 # set the adding time  
        self.time = np.array([])
        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback)

    # after we get the data from ros master put it inside our container 
    def callback(self, data):
        data_ch1 = np.array(data.data_ch1)/pow(2,31)
        #data_ch2 = np.array(data.data_ch2)
        self.fs = data.fs
        
        number = self.fs*self.plot_length
        self.data_frame_ch1 = np.concatenate((self.data_frame_ch1, data_ch1))
        #self.data_frame_ch2 = np.concatenate((self.data_frame_ch2, data_ch2))
        if(len(self.data_frame_ch1)>number):
            self.count+=1;
            self.data_frame_ch1 = self.data_frame_ch1[-number:]
        #    self.data_frame_ch2 = self.data_frame_ch2[-number:]
    def animate(self, i):
        time_start = time.time()
        plt.cla()
        
        data = self.data_frame_ch1
        count = self.count
        t = np.arange(len(data))/self.fs + count*self.data_length/self.fs
        
        self.ax.plot(t, data)
        self.ax.set_xlabel("Time(s)")
        self.ax.set_ylabel("Voltage(volt)")
        self.ax.set_title("Streaming plot for Hydrophone data")
        self.ax.grid(True)
        time_end = time.time()
        print("time consuming: ", time_end-time_start, "sec")




def main():
    rospy.init_node('plot_hydrophone_data_node', anonymous=True)
    pn = plot_hydrophone_data_node()
    ani = FuncAnimation(pn.fig, pn.animate, interval=100)
    plt.show()   
    rospy.spin()

if __name__ == "__main__":
    main()
