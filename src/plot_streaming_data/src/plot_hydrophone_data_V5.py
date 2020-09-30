#!/usr/bin/env python3
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
# import ros library
import rospy
from ntu_msgs.msg import HydrophoneData, HydrophoneFFTData


class plot_hydrophone_data_node:
    def __init__(self):
        self.data_frame_ch1 = np.array([]) # node container for data 
        self.data_frame_ch2 = np.array([])
        self.fft_matrix_ch1 = []
        self.fft_matrix_ch2 = []
        self.fs = 96000
        self.data_length = 9600
        self.N = 0 # length of the imshow
        self.M = 0
        self.delta_t = 0

        # plot setting
        self.fig, self.ax = plt.subplots(2,2, figsize=(20,6), sharex=True)

        self.plot_length = 1 # frame length(sec) in the plot
        self.count_t = 0 # set the adding time for time series  
        # self.count_f = 0
        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback_1)
        rospy.Subscriber("/compute_fft/fft_data", HydrophoneFFTData, self.callback_2)


    # after we get the data from ros master put it inside our container 
    def callback_1(self, data):
        data_ch1 = np.array(data.data_ch1)
        data_ch2 = np.array(data.data_ch2)
        self.fs = data.fs
        self.data_length = data.length
        
        number = self.fs*self.plot_length
        self.data_frame_ch1 = np.concatenate((self.data_frame_ch1, data_ch1))
        self.data_frame_ch2 = np.concatenate((self.data_frame_ch2, data_ch2))
        if(len(self.data_frame_ch1)>number):
            self.count_t+=1;
            self.data_frame_ch1 = self.data_frame_ch1[-number:]
            self.data_frame_ch2 = self.data_frame_ch2[-number:]
    def callback_2(self, data):
        abs_fft_ch1 = data.abs_fft_ch1
        abs_fft_ch2 = data.abs_fft_ch2
        
        self.N = int(self.plot_length//data.delta_t)
        self.M = len(abs_fft_ch1)
        self.delta_t = data.delta_t

        self.fft_matrix_ch1.append(abs_fft_ch1)
        self.fft_matrix_ch2.append(abs_fft_ch2)
        if(len(self.fft_matrix_ch1)>self.N):
            # self.count_f+=1
            self.fft_matrix_ch1 = self.fft_matrix_ch1[-self.N:]
            self.fft_matrix_ch2 = self.fft_matrix_ch2[-self.N:]

    def animate(self, i):
        time_start = time.time()
        self.ax[0][0].clear()
        self.ax[0][1].clear()
        self.ax[1][0].clear()
        self.ax[1][1].clear()
        
        data_ch1 = self.data_frame_ch1
        data_ch2 = self.data_frame_ch2
        count_t = self.count_t
        fft_matrix_ch1 = self.fft_matrix_ch1
        fft_matrix_ch2 = self.fft_matrix_ch2

        t1 = np.arange(len(data_ch1))/self.fs + count_t*self.data_length/self.fs
        t2 = np.arange(len(data_ch2))/self.fs + count_t*self.data_length/self.fs
        t3_max = np.max(t1)
        t4_max = np.max(t2)
        f_max = self.fs/2
        m = [0]*self.M
        if(len(fft_matrix_ch1)<self.N):
            for i in range(self.N-len(fft_matrix_ch1)):
                fft_matrix_ch1.append(m)
                fft_matrix_ch2.append(m)
        
        self.ax[0][0].plot(t1, data_ch1)
        self.ax[0][0].set_xlabel("Time(s)")
        self.ax[0][0].set_ylabel("Voltage(volt)")
        self.ax[0][0].set_title("Streaming plot for CH1")
        self.ax[0][0].grid(True)

        self.ax[0][1].plot(t2, data_ch2)
        self.ax[0][1].set_xlabel("Time(s)")
        self.ax[0][1].set_ylabel("Voltage(volt)")
        self.ax[0][1].yaxis.set_label_position("right")
        self.ax[0][1].yaxis.set_ticks_position("right")
        self.ax[0][1].set_title("Streaming plot for CH2")
        self.ax[0][1].grid(True)

        self.ax[1][0].imshow(np.array(fft_matrix_ch1).T, origin="lower", extent=[t3_max-self.plot_length, t3_max, 0, f_max])
        self.ax[1][0].axis('auto')

        self.ax[1][1].imshow(np.array(fft_matrix_ch2).T, origin="lower", extent=[t4_max-self.plot_length, t4_max, 0, f_max])
        self.ax[1][1].axis('auto')

        plt.tight_layout()

        time_end = time.time()
        print("time consuming: ", time_end-time_start, "sec")




def main():
    rospy.init_node('plot_hydrophone_data_node', anonymous=True)
    pn = plot_hydrophone_data_node()
    ani = FuncAnimation(pn.fig, pn.animate, interval=500)
    plt.show()   
    rospy.spin()

if __name__  == "__main__":
    main()
