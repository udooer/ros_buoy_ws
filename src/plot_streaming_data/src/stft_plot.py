#!/usr/bin/env python3
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
# import ros library
import rospy
from ntu_msgs.msg import HydrophoneFFTData


class plot_stft_node:
    def __init__(self):
        self.fft_ch1 = [] # node container for data 
        self.fft_ch2 = []
        self.fs = 96000 
        self.delta_t = 0
        # plot setting
        self.fig, self.ax = plt.subplots(1,2, figsize=(10,6))


        self.plot_length = 1 # frame length(sec) in the plot
        self.count = 0 # set the adding time  
        rospy.Subscriber("/compute_fft/fft_data", HydrophoneFFTData, self.callback)
        self.M = 0 # imshow length 
        self.N = 0 # imshow length

    # after we get the data from ros master put it inside our container 
    def callback(self, data):
        # time_start = time.time()
        abs_fft_ch1 = data.abs_fft_ch1
        abs_fft_ch2 = data.abs_fft_ch2
        
        self.fs = data.fs
        self.delta_t = data.delta_t 
        self.M = int(len(abs_fft_ch1))
        self.N = int(self.plot_length/self.delta_t)
        self.fft_ch1.append(abs_fft_ch1)
        self.fft_ch2.append(abs_fft_ch2)
        # print("add into our container: ",len(self.fft_ch1))
        if(len(self.fft_ch1)>self.N):
            self.count+=1;
            self.fft_ch1 = self.fft_ch1[-self.N:]
            self.fft_ch2 = self.fft_ch2[-self.N:]
            # print("filter the frame into plot length: ", len(self.fft_ch1))
        # time_end = time.time()
        # print("header:", self.count, "time consuming: ", time_end-time_start, "sec")
    def animate(self, i):
        time_start = time.time()
        self.ax[0].clear()
        self.ax[1].clear()
        
        fft_ch1 = self.fft_ch1
        fft_ch2 = self.fft_ch2
        count = self.count
        t1_max = (len(fft_ch1)+count)*self.delta_t
        t2_max = (len(fft_ch2)+count)*self.delta_t
        f_max = self.fs/4
        m = [0]*self.M
        if(len(fft_ch1)<self.N):
            for i in range(self.N-len(fft_ch1)):
                fft_ch1.append(m)
                fft_ch2.append(m) 
        print(len(fft_ch1), ": ", i)
        self.ax[0].imshow(np.array(fft_ch1).T, origin="lower", extent=[t1_max-1,t1_max,0,f_max])
        self.ax[0].axis('auto')
        self.ax[0].set_xlabel("Time(s)")
        self.ax[0].set_ylabel("PSD")
        self.ax[0].set_title("STFT of CH1")

        self.ax[1].imshow(np.array(fft_ch2).T, origin="lower", extent=[t2_max-1,t2_max,0,f_max])
        self.ax[1].axis('auto')
        self.ax[1].set_xlabel("Time(s)")
        self.ax[1].set_ylabel("PSD")
        self.ax[1].set_title("STFT of CH2")

        time_end = time.time()
        print("time consuming: ", time_end-time_start, "sec")




def main():
    rospy.init_node('plot_stft_node', anonymous=True)
    pn = plot_stft_node()
    ani = FuncAnimation(pn.fig, pn.animate, interval=100)
    plt.show()   
    rospy.spin()

if __name__ == "__main__":
    main()
