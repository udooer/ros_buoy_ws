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
from ntu_msgs.msg import HydrophoneFFTDataWithClickRemoval, DetectionImage

class plot_detection_result_node:
    def __init__(self):
        self.getParameters()
        # member variable for subscribing  
        # from /compute_fft/two_mode_fft_data topic
        self.fft_ch1 = []
        self.fft_ch2 = []
        self.delta_f = 0
        self.delta_t = 0
        self.count_F = 0

        # member variable for subscribing  
        # from /detect_whistle/detection_image topic
        self.col_ch1 = []
        self.col_ch2 = []
        self.df = 0
        self.dt = 0
        self.start_freq = 0
        self.end_freq = 0
        self.count_D = 0

        # plot setting 
        self.fig, self.ax = plt.subplots(2, 2, figsize=(20,6))
        self.M_detection = 75
        self.M_fft = 513
        self.N = 0

        rospy.Subscriber("detect_whistle/detection_image", DetectionImage, self.push_detection_data)
        rospy.Subscriber("compute_fft/two_mode_fft_data", HydrophoneFFTDataWithClickRemoval, self.push_fft_data)
    # define the function to get the private node parameters setting 
    # for this node from plot_streaming_data.yaml file
    def getParameters(self):
        self.PLOT_LENGTH_ = rospy.get_param("~PLOT_LENGTH_")

        # self.FPS_ = rospy.get_param("~FPS_")
        # self.INTERVAL_ = int(1000/self.FPS_) #(ms)

    def push_detection_data(self, data):
        self.col_ch1.append(data.col_ch1)
        self.col_ch2.append(data.col_ch2)
        self.df = data.df
        self.dt = data.dt
        self.start_freq = data.start_freq
        self.end_freq = data.end_freq

        self.M_detection = len(data.col_ch1)
        self.N = int(self.PLOT_LENGTH_/self.dt)
        
        col_length = len(self.col_ch1)
        if(col_length>self.N):
            self.count_D += col_length-self.N
            self.col_ch2 = self.col_ch2[col_length-self.N:]
            self.col_ch1 = self.col_ch1[col_length-self.N:]
    def push_fft_data(self, data):
        self.fft_ch1.append(data.fft_ch1)
        self.fft_ch2.append(data.fft_ch2)
        self.delta_t = data.delta_t
        self.delta_f = data.delta_f

        self.M_fft = len(data.fft_ch1)
        self.N = int(self.PLOT_LENGTH_/self.delta_t)
        
        fft_length = len(self.fft_ch1)
        if(fft_length>self.N):
            self.count_F += fft_length-self.N
            self.fft_ch2 = self.fft_ch2[fft_length-self.N:]
            self.fft_ch1 = self.fft_ch1[fft_length-self.N:]
    def animate(self, i):
        time_stamp_1 = time.time()
        self.ax[0][0].clear()
        self.ax[0][1].clear()
        self.ax[1][0].clear()
        self.ax[1][1].clear()
        
        fft_ch1 = copy.copy(self.fft_ch1)
        fft_ch2 = copy.copy(self.fft_ch2)
        col_ch1 = copy.copy(self.col_ch1)
        col_ch2 = copy.copy(self.col_ch2)   
        print("fft ch1 length: {}".format(len(fft_ch1)))
        print("fft ch2 length: {}".format(len(fft_ch2)))
        print("col ch1 length: {}".format(len(col_ch1)))
        print("col ch2 length: {}".format(len(col_ch2)))
        print("count D: {}".format(self.count_D))
        print("count F: {}".format(self.count_F))

        if(self.df == 0):
            self.df = 93.75
        f = np.arange(self.M_fft)*self.delta_f/1000
        start_index = math.floor((self.start_freq)/self.df)
        end_index = math.ceil((self.end_freq)/self.df)
        
        if(self.dt == 0):
            self.dt = 512/96000
            self.N = int(self.PLOT_LENGTH_/self.dt)
        else:
            self.N = int(self.PLOT_LENGTH_/self.dt)
        
        m = [0]*self.M_fft
        range_number = len(fft_ch1)
        if(range_number<self.N):
            print("fft")
            for i in range(self.N-range_number):
                fft_ch1.append(m)
                fft_ch2.append(m)

        m = [0]*self.M_detection
        range_number = len(col_ch1)
        if(range_number<self.N):
            print("col")
            for i in range(self.N-range_number):
                col_ch1.append(m)
                col_ch2.append(m)

        # time_stamp_3 = time.time()
        self.ax[0][0].imshow(np.array(fft_ch1).T, cmap="jet", origin="lower", extent=[self.count_F*self.dt, self.count_F*self.dt+self.PLOT_LENGTH_, 0, f[self.M_fft-1]])
        self.ax[0][0].axis('auto')
        self.ax[0][0].set_xlabel("Time(s)")
        self.ax[0][0].set_ylabel("Frequency(kHz)")
        self.ax[0][0].set_ylim([2, 12])

        self.ax[0][1].imshow(np.array(fft_ch2).T, cmap="jet", origin="lower", extent=[self.count_F*self.dt, self.count_F*self.dt+self.PLOT_LENGTH_, 0, f[self.M_fft-1]])
        self.ax[0][1].axis('auto')
        self.ax[0][1].set_xlabel("Time(s)")
        self.ax[0][1].set_ylabel("Frequency(kHz)")
        self.ax[0][1].set_ylim([2, 12])
        self.ax[0][1].yaxis.set_label_position("right")
        self.ax[0][1].yaxis.set_ticks_position("right")
        
        # time_stamp_4 = time.time()

        self.ax[1][0].imshow(np.array(col_ch1).T.astype(np.int8), cmap="binary", origin="lower", extent=[self.count_D*self.dt, self.count_D*self.dt+self.PLOT_LENGTH_, f[start_index], f[end_index]])
        self.ax[1][0].axis('auto')
        self.ax[1][0].set_xlabel("Time(s)")
        self.ax[1][0].set_ylabel("Frequency(kHz)")
        self.ax[1][0].set_ylim([2, 12])

        self.ax[1][1].imshow(np.array(col_ch2).T.astype(np.int8), cmap="binary", origin="lower", extent=[self.count_D*self.dt, self.count_D*self.dt+self.PLOT_LENGTH_, f[start_index], f[end_index]])
        self.ax[1][1].axis('auto')
        self.ax[1][1].set_xlabel("Time(s)")
        self.ax[1][1].set_ylabel("Frequency(kHz)")
        self.ax[1][1].set_ylim([2, 12])
        self.ax[1][1].yaxis.set_label_position("right")
        self.ax[1][1].yaxis.set_ticks_position("right")
        print("Using 1 FPS for animation takes {} seconds.".format(time.time()-time_stamp_1))

def main():
    rospy.init_node("plot_streaming_data_node", anonymous=True)
    plot_node = plot_detection_result_node()
    # ani = FuncAnimation(plot_node.fig, plot_node.animate, interval=plot_node.INTERVAL_)
    ani = FuncAnimation(plot_node.fig, plot_node.animate, interval=1000)
    plt.show()
    rospy.spin()

if __name__ == "__main__":
    main()
