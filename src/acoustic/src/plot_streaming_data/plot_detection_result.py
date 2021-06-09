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
from ntu_msgs.msg import HydrophoneFFTData, DetectionImage

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
        self.col_ch1 = np.array([])
        self.col_ch2 = np.array([])
        self.df = 0
        self.dt = 0
        self.start_freq = 0
        self.end_freq = 0
        self.count_D = 0

        # plot setting 
        self.fig, self.ax = plt.subplots(2, 2, figsize=(20,6))
        self.M_detection = 75
        self.count_t = 0
        self.M_fft = 513
        self.N = 0

        rospy.Subscriber("/detect_whistle/detection_image", DetectionImage, self.push_detection_data)
        rospy.Subscriber("/compute_fft/fft_data", HydrophoneFFTData, self.push_fft_data)
    # define the function to get the private node parameters setting 
    # for this node from plot_streaming_data.yaml file
    def getParameters(self):
        self.PLOT_LENGTH_ = rospy.get_param("~PLOT_LENGTH_")
        self.first = True
        # self.FPS_ = rospy.get_param("~FPS_")
        # self.INTERVAL_ = int(1000/self.FPS_) #(ms)

    def push_detection_data(self, data):
        if(self.first):
            self.col_ch1 = self.col_ch1.reshape((0,data.col_length))
            self.col_ch2 = self.col_ch2.reshape((0,data.col_length))
            self.first = False
        d_ch1 = np.array(data.col_ch1).reshape(data.col_number, data.col_length)
        d_ch2 = np.array(data.col_ch2).reshape(data.col_number, data.col_length)
        self.col_ch1 = np.concatenate((self.col_ch1, d_ch1))
        self.col_ch2 = np.concatenate((self.col_ch2, d_ch2))
        self.df = data.df
        self.dt = data.dt
        self.start_freq = data.start_freq
        self.end_freq = data.end_freq
        self.M_detection = data.col_length
        if(self.dt!=self.delta_t):
            print("Warning!!! Check the parameters of detection node and compute fft node: dt is not match.")

        
    def push_fft_data(self, data):
        self.fft_ch1.append(data.fft_ch1)
        self.fft_ch2.append(data.fft_ch2)
        self.delta_t = data.delta_t
        self.delta_f = data.delta_f

        self.M_fft = len(data.fft_ch1)
    def animate(self, i):
        time_stamp_1 = time.time()
        self.ax[0][0].clear()
        self.ax[0][1].clear()
        self.ax[1][0].clear()
        self.ax[1][1].clear()
        if(self.dt == 0):
            self.dt = 512/96000
            self.N = int(self.PLOT_LENGTH_/self.dt)
        else:
            self.N = int(self.PLOT_LENGTH_/self.dt)
        if(self.df == 0):
            self.df = 93.75
        f = np.arange(self.M_fft)*self.delta_f/1000
        start_index = math.floor((self.start_freq)/self.df)
        end_index = math.ceil((self.end_freq)/self.df)

        fft_ch1 = copy.copy(self.fft_ch1)
        fft_ch2 = copy.copy(self.fft_ch2)
        col_ch1 = np.copy(self.col_ch1)
        col_ch2 = np.copy(self.col_ch2)
        print("fft ch1 length: {}".format(len(fft_ch1)))
        print("fft ch2 length: {}".format(len(fft_ch2)))
        print("col ch1 length: {}".format(len(col_ch1)))
        print("col ch2 length: {}".format(len(col_ch2)))
        fft_length = len(fft_ch1)
        col_length = len(col_ch1)
        if(col_length>self.N and fft_length>self.N):
            length = len(self.col_ch1)-self.N
            self.count_t += length
            self.fft_ch1 = self.fft_ch1[length:]
            self.fft_ch2 = self.fft_ch2[length:]
            self.col_ch2 = self.col_ch2[length:]
            self.col_ch1 = self.col_ch1[length:]        
        
        
        range_number = len(fft_ch1)
        if(range_number<self.N):
            m = [0]*self.M_fft
            for i in range(self.N-range_number):
                fft_ch1.append(m)
                fft_ch2.append(m)

        
        range_number = len(col_ch1)
        if(range_number==0):
            m = np.zeros((self.N, 75))
            col_ch1 = m
            col_ch2 = m
        elif(range_number<self.N):
            m = np.zeros((self.N-range_number,self.M_detection))
            col_ch1 = np.concatenate((col_ch1, m))
            col_ch2 = np.concatenate((col_ch2, m))

        if(len(col_ch1)>self.N):
            col_ch1 = col_ch1[:self.N]
            col_ch2 = col_ch2[:self.N]
        if(len(fft_ch1)>self.N):
            fft_ch1 = fft_ch1[:self.N]
            fft_ch2 = fft_ch2[:self.N]
        print("fft ch1 length: {}".format(len(fft_ch1)))
        print("fft ch2 length: {}".format(len(fft_ch2)))
        print("col ch1 length: {}".format(len(col_ch1)))
        print("col ch2 length: {}".format(len(col_ch2)))
        print("count t : {}".format(self.count_t))
        print("\n\n\n")

        # time_stamp_3 = time.time()
        self.ax[0][0].imshow(np.array(fft_ch1).T, cmap="jet", origin="lower", extent=[self.count_t*self.dt, self.count_t*self.dt+self.PLOT_LENGTH_, 0, f[self.M_fft-1]])
        self.ax[0][0].axis('auto')
        self.ax[0][0].set_xlabel("Time(s)")
        self.ax[0][0].set_ylabel("Frequency(kHz)")
        self.ax[0][0].set_ylim([2, 12])

        self.ax[0][1].imshow(np.array(fft_ch2).T, cmap="jet", origin="lower", extent=[self.count_t*self.dt, self.count_t*self.dt+self.PLOT_LENGTH_, 0, f[self.M_fft-1]])
        self.ax[0][1].axis('auto')
        self.ax[0][1].set_xlabel("Time(s)")
        self.ax[0][1].set_ylabel("Frequency(kHz)")
        self.ax[0][1].set_ylim([2, 12])
        self.ax[0][1].yaxis.set_label_position("right")
        self.ax[0][1].yaxis.set_ticks_position("right")
        
        # time_stamp_4 = time.time()

        self.ax[1][0].imshow(np.array(col_ch1).T.astype(np.int8), cmap="binary", origin="lower", extent=[self.count_t*self.dt, self.count_t*self.dt+self.PLOT_LENGTH_, f[start_index], f[end_index]])
        self.ax[1][0].axis('auto')
        self.ax[1][0].set_xlabel("Time(s)")
        self.ax[1][0].set_ylabel("Frequency(kHz)")
        self.ax[1][0].set_ylim([2, 12])

        self.ax[1][1].imshow(np.array(col_ch2).T.astype(np.int8), cmap="binary", origin="lower", extent=[self.count_t*self.dt, self.count_t*self.dt+self.PLOT_LENGTH_, f[start_index], f[end_index]])
        self.ax[1][1].axis('auto')
        self.ax[1][1].set_xlabel("Time(s)")
        self.ax[1][1].set_ylabel("Frequency(kHz)")
        self.ax[1][1].set_ylim([2, 12])
        self.ax[1][1].yaxis.set_label_position("right")
        self.ax[1][1].yaxis.set_ticks_position("right")
        print("Ploting detection result for FPS 0.5 takes {} seconds.".format(str(round(time.time()-time_stamp_1,6))))
def main():
    rospy.init_node("plot_streaming_data_node", anonymous=True)
    plot_node = plot_detection_result_node()
    # ani = FuncAnimation(plot_node.fig, plot_node.animate, interval=plot_node.INTERVAL_)
    ani = FuncAnimation(plot_node.fig, plot_node.animate, interval=2000)
    plt.show()
    rospy.spin()

if __name__ == "__main__":
    main()
