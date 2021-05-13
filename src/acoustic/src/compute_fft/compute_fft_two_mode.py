#!/usr/bin/env python3
# import python library 
from scipy.fftpack import fft 
import numpy as np
import time 

# import ros library
import rospy
from ntu_msgs.msg import HydrophoneData, HydrophoneFFTDataWithClickRemoval


class compute_fft_node:
    def __init__(self):
        self.getParameters()
        
        # member variable for subscribing 
        # from /get_hydrophone_data_for2i2/hydrophone_data topic   
        self.data_ch1 = np.array([])
        self.data_ch2 = np.array([])
        self.length = 1024
        self.fs = 96000

        # member variable for publishing 
        # to /compute_fft/fft_data topic  
        self.msg = HydrophoneFFTDataWithClickRemoval()

        # define subscriber and publisher 
        rospy.Subscriber("/get_sound_data_for2i2/hydrophone_data", HydrophoneData, self.callback)
        self.pub = rospy.Publisher("/compute_fft/two_mode_fft_data", HydrophoneFFTDataWithClickRemoval, queue_size=200)
    # define the function to get the private node parameters setting 
    # for this node from compute_fft.yaml file
    def getParameters(self):
        self.WINDOW_LENGTH_ = rospy.get_param("~WINDOW_LENGTH_")
        self.WINDOW_TYPE_ = rospy.get_param("~WINDOW_TYPE_")
        self.OVERLAP_ = rospy.get_param("~OVERLAP_")

        self.STEP_ = int(self.WINDOW_LENGTH_*(1-self.OVERLAP_))

        self.THRESHOLD_ = 5
        self.POWER_ = 6
        self.SENSITIVITY_ = -211
    # define windowed-fft function 
    def windowedFFT(self, x):
        if(self.WINDOW_TYPE_ == 0):
            window = np.hanning(len(x))
            n = int(len(x)//2+1)
            half_mag_fft = abs(fft(window*x)[:n])
            ans = 20*np.log10(half_mag_fft**2) - self.SENSITIVITY_
            return tuple(ans)
        elif(self.WINDOW_TYPE_ == 1):
            window = np.hamming(len(x))
            n = int(len(x)//2+1)
            half_mag_fft = abs(fft(window*x)[:n])
            ans = 20*np.log10(half_mag_fft**2) - self.SENSITIVITY_
            return tuple(ans)
        elif(self.WINDOW_TYPE_ == 2):
            window = np.blackman(len(x))
            n = int(len(x)//2+1)
            half_mag_fft = abs(fft(window*x)[:n])
            ans = 20*np.log10(half_mag_fft**2) - self.SENSITIVITY_
            return tuple(ans)

    def removeClick(self,x):
        x = np.array(x*100)
        m = np.mean(x)
        SD = np.std(x)
        w = 1.0/(1+((x-m)/self.THRESHOLD_*SD)**self.POWER_)
        return w*x/100

    # callback function when we get the data 
    # from get_sound_data_for2i2/hydrophone_data topic
    def callback(self, data):
        start = time.time()
        self.data_ch1 = np.concatenate((self.data_ch1, data.data_ch1))
        self.data_ch2 = np.concatenate((self.data_ch2, data.data_ch2))
        self.length = data.length
        self.fs = data.fs

        self.msg.fs = self.fs
        self.msg.delta_f = self.fs/self.WINDOW_LENGTH_
        self.msg.delta_t = self.WINDOW_LENGTH_*(1-self.OVERLAP_)/self.fs
        count = 0
        while(len(self.data_ch1)>=self.WINDOW_LENGTH_):
            windowed_ch1 = self.data_ch1[:self.WINDOW_LENGTH_]
            windowed_ch2 = self.data_ch2[:self.WINDOW_LENGTH_]
            self.data_ch1 = self.data_ch1[self.STEP_:]
            self.data_ch2 = self.data_ch2[self.STEP_:]
            self.msg.fft_ch1 = self.windowedFFT(windowed_ch1)
            self.msg.fft_ch2 = self.windowedFFT(windowed_ch2)
            self.msg.fft_ch1_click_removal = self.windowedFFT(self.removeClick(windowed_ch1))
            self.msg.fft_ch2_click_removal = self.windowedFFT(self.removeClick(windowed_ch2))
            self.pub.publish(self.msg)
            count += 1
        end = time.time()
        sec = count*self.STEP_/self.fs
        # rospy.loginfo("Computing fft of " + str(round(sec, 6)) + " sec data takes " + str(round(end-start, 6)) + " sec")
        print("one callback function deals with {} seconds of data and takes {} seconds".format(sec,end-start))
def main():
    rospy.init_node('compute_fft_two_mode_node', anonymous=True)
    rosnode = compute_fft_node()
    rospy.spin()

if __name__ == "__main__":
    main()