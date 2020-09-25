#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.fftpack import fft 
# import ros library
import rospy
from ntu_msgs.msg import HydrophoneData, HydrophoneFFTData


class compute_fft_node:
    def __init__(self):
        self.data_frame_ch1 = np.array([]) # node container for Hydrophone data 
        self.data_frame_ch2 = np.array([])
        self.fs = 96000 
        self.window_length = 1024
        self.overlap = 0.9
        self.step = int(self.window_length*(1-self.overlap))

        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback)
        self.pub = rospy.Publisher('/compute_fft/fft_data', HydrophoneFFTData, queue_size=10)
        self.msg = HydrophoneFFTData()
        self.msg.delta_f = self.fs/self.window_length
        self.msg.delta_t = self.window_length*(1-self.overlap)/self.fs

    def windowed_fft(self, x):
        w = np.hanning(len(x))
        n = len(x)//2+1
        mag_fft = tuple(abs(fft(w*x)[:n]))
        return mag_fft
    # after we get the data from ros master put it inside in our container 
    def callback(self, data):
        data_ch1 = np.array(data.data_ch1)
        data_ch2 = np.array(data.data_ch2)
        self.fs = data.fs
        self.msg.fs = self.fs
        self.data_frame_ch1 = np.concatenate((self.data_frame_ch1, data_ch1))
        self.data_frame_ch2 = np.concatenate((self.data_frame_ch2, data_ch2))
        while(len(self.data_frame_ch1)>self.window_length):
            data_ch1 = self.data_frame_ch1[:self.window_length]
            data_ch2 = self.data_frame_ch2[:self.window_length]
            self.data_frame_ch1 = self.data_frame_ch1[self.step:]
            self.data_frame_ch2 = self.data_frame_ch2[self.step:]
            self.msg.abs_fft_ch1 = self.windowed_fft(data_ch1)
            self.msg.abs_fft_ch2 = self.windowed_fft(data_ch2)
            self.pub.publish(self.msg)

def main():
    rospy.init_node('compute_fft_node', anonymous=True)
    fn = compute_fft_node()
    rospy.spin()

if __name__ == "__main__":
    main()
