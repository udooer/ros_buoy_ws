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
        self.fig, self.ax = plt.subplots(1,2, figsize=(10,6))

        self.plot_length = 1 # frame length(sec) in the plot
        self.count = 0 # set the adding time  
        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback)

    # after we get the data from ros master put it inside our container 
    def callback(self, data):
        data_ch1 = np.array(data.data_ch1)
        data_ch2 = np.array(data.data_ch2)
        self.fs = data.fs
        
        number = self.fs*self.plot_length
        self.data_frame_ch1 = np.concatenate((self.data_frame_ch1, data_ch1))
        self.data_frame_ch2 = np.concatenate((self.data_frame_ch2, data_ch2))
        if(len(self.data_frame_ch1)>number):
            self.count+=1;
            self.data_frame_ch1 = self.data_frame_ch1[-number:]
            self.data_frame_ch2 = self.data_frame_ch2[-number:]
    def animate(self, i):
        time_start = time.time()
        self.ax[0].clear()
        self.ax[1].clear()
        
        data_ch1 = self.data_frame_ch1
        data_ch2 = self.data_frame_ch2
        count = self.count
        t1 = np.arange(len(data_ch1))/self.fs + count*self.data_length/self.fs
        t2 = np.arange(len(data_ch2))/self.fs + count*self.data_length/self.fs
        self.ax[0].plot(t1, data_ch1)
        self.ax[0].set_xlabel("Time(s)")
        self.ax[0].set_ylabel("Voltage(volt)")
        self.ax[0].set_title("Streaming plot for CH1")
        self.ax[0].grid(True)

        self.ax[1].plot(t2, data_ch2)
        self.ax[1].set_xlabel("Time(s)")
        self.ax[1].set_ylabel("Voltage(volt)")
        self.ax[1].yaxis.set_label_position("right")
        self.ax[1].yaxis.set_ticks_position("right")
        self.ax[1].set_title("Streaming plot for CH2")
        self.ax[1].grid(True)

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
