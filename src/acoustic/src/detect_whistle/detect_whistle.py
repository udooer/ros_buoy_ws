#!/usr/bin/env python3
# basic package you definitly know
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import pandas as pd
import os.path
import time
import copy

# package for image processing
import cv2

# package for clustering
from sklearn.cluster import DBSCAN

# import ros library
import rospy
from ntu_msgs.msg import HydrophoneFFTDataWithClickRemoval

class detect_whistle_node:
    def __init__(self):
        self.getParameters()

        # member variable for subscribing  
        # from /compute_fft/fft_data topic
        self.fft_ch1_click_removal = []
        self.fft_ch2_click_removal = []
        self.fft_ch1 = []
        self.fft_ch2 = []

        self.detection_image_ch1 = np.array([]).reshape(self.END_INDEX_-self.START_INDEX_, 0)
        self.detection_image_ch2 = np.array([]).reshape(self.END_INDEX_-self.START_INDEX_, 0)

        # Whistle Features
        self.whistle_count_ch1 = 0
        self.whistle_duration_ch1 = 0
        self.whistle_count_ch2 = 0
        self.whistle_duration_ch2 = 0
        
        # Plotting Setting
        self.fig, self.ax = plt.subplots(2, 2, figsize=(20,6))
        self.count_t = 0

        # define subscriber and publisher
        rospy.Subscriber("/compute_fft/two_mode_fft_data", HydrophoneFFTDataWithClickRemoval, self.pushFFTData)
    def getParameters(self):
        self.DETECTOR_FRAME_ = rospy.get_param("~DETECTOR_FRAME_")
        # Band Pass
        self.START_FREQ_ = rospy.get_param("~START_FREQ_")
        self.END_FREQ_ = rospy.get_param("~END_FREQ_")
        self.FFT_NUMBER_ = rospy.get_param("~FFT_NUMBER_")
        self.FS_ = rospy.get_param("~FS_")

        self.DF_ = self.FS_/self.FFT_NUMBER_
        self.START_INDEX_ = math.floor((self.START_FREQ_)/self.DF_)
        self.END_INDEX_ = math.ceil((self.END_FREQ_)/self.DF_)
        # Whistle Filter
        self.FREQ_WIDTH_ = rospy.get_param("~FREQ_WIDTH_")
        self.DEFINED_SNR_ = rospy.get_param("~DEFINED_SNR_")
        self.TIME_DURATION_ = rospy.get_param("~TIME_DURATION_")
        # DBScan Clustering
        self.EPS_ = rospy.get_param("~EPS_")
        self.MIN_SAMPLES_ = rospy.get_param("~MIN_SAMPLES_")
        # Figure Length
        self.PLOT_LENGTH_ = rospy.get_param("~PLOT_LENGTH_")
        self.FPS_ = rospy.get_param("~FPS_")
        
        self.INTERVAL_ = int(1000/self.FPS_) #(ms)
    
    def whistleFeatureFilter(self, median_blur):
        width_size = math.ceil(self.FREQ_WIDTH_/2/self.delta_f)
        ## high PSD level and high SNR reference to narrow band level
        SNR = []
        for row in median_blur:
            p2 = row[self.START_INDEX_-width_size:self.END_INDEX_-width_size]
            p1 = row[self.START_INDEX_:self.END_INDEX_]
            p3 = row[self.START_INDEX_+width_size:self.END_INDEX_+width_size]
            snr = 2*p1-(p2+p3)
            SNR.append(snr)
        SNR = np.array(SNR)

        SNR_filter = SNR>self.DEFINED_SNR_
        ## Long time duration
        col_size = math.ceil(self.TIME_DURATION_/self.delta_t)

        image_row = SNR_filter.T.shape[0]
        image_col = SNR_filter.T.shape[1]
        padding = np.zeros((image_row, image_col+col_size-1))
        padding[:,col_size//2:col_size//2+image_col] = SNR_filter.T
        detection = np.zeros((image_row, image_col))
        for i in range(col_size):
            detection += padding[:,i:i+image_col]
        return detection==col_size

    def DBSCANCluster(self, detection, mode):
        (x,y) = np.nonzero(detection.T)
        if len(x) and mode==1:
            point = np.array([x,y]).T
            clustering=DBSCAN(eps=self.EPS_,min_samples=self.MIN_SAMPLES_).fit(point)

            point_without_outlier = point[clustering.labels_!=-1]
            new_label = clustering.labels_[clustering.labels_!=-1]
            point_x = point_without_outlier.T[0]*self.delta_t
            length = len(set(new_label))
            for i in range(length):
                cluster_x = point_x[new_label==i]
                cluster_y = point_y[new_label==i]
                if(cluster_x[-1]-cluster_x[0]>0.05):
                    self.whistle_duration_ch1 += cluster_x[-1]-cluster_x[0]
                    self.whistle_count_ch1 += 1
        elif len(x) and mode==2:
            point = np.array([x,y]).T
            clustering=DBSCAN(eps=self.EPS_,min_samples=self.MIN_SAMPLES_).fit(point)

            point_without_outlier = point[clustering.labels_!=-1]
            new_label = clustering.labels_[clustering.labels_!=-1]
            point_x = point_without_outlier.T[0]*self.delta_t
            length = len(set(new_label))
            for i in range(length):
                cluster_x = point_x[new_label==i]
                cluster_y = point_y[new_label==i]
                if(cluster_x[-1]-cluster_x[0]>0.05):
                    self.whistle_duration_ch2 += cluster_x[-1]-cluster_x[0]
                    self.whistle_count_ch2 += 1
    def pushFFTData(self, data):
        self.fft_ch1_click_removal.append(data.fft_ch1_click_removal)
        self.fft_ch2_click_removal.append(data.fft_ch2_click_removal)
        self.fft_ch1.append(data.fft_ch1)
        self.fft_ch2.append(data.fft_ch2)
        self.delta_t = data.delta_t
        self.delta_f = data.delta_f

        if(self.delta_f != self.DF_):
            print("WARNING!!! DELTA F IS NOT THE SAME.")

        self.N = int(self.PLOT_LENGTH_/self.delta_t)
        if(len(self.fft_ch1)>self.N):
            self.count_t += len(self.fft_ch1)-self.N
            self.fft_ch1 = self.fft_ch1[-self.N:]
            self.fft_ch2 = self.fft_ch2[-self.N:]
            # self.detection_image_ch1 = self.detection_image_ch1[:,-self.N:]
            # self.detection_image_ch2 = self.detection_image_ch2[:,-self.N:]

        self.DETECTOR_FRAME_LENGTH_ = int(self.DETECTOR_FRAME_/self.delta_t)
        # while(len(self.fft_ch1_click_removal)>=self.DETECTOR_FRAME_LENGTH_):
        #     image_ch1 = np.array(self.fft_ch1_click_removal[:self.DETECTOR_FRAME_LENGTH_])
        #     image_ch2 = np.array(self.fft_ch2_click_removal[:self.DETECTOR_FRAME_LENGTH_])
        #     self.fft_ch1_click_removal = self.fft_ch1_click_removal[-self.DETECTOR_FRAME_LENGTH_:]
        #     self.fft_ch1_click_removal = self.fft_ch2_click_removal[self.DETECTOR_FRAME_LENGTH_:]
        #     median_blur_ch1 = cv2.medianBlur(image_ch1.astype(np.float32),3)
        #     median_blur_ch2 = cv2.medianBlur(image_ch2.astype(np.float32),3)
        #     detection_ch1 = self.whistleFeatureFilter(median_blur_ch1)
        #     detection_ch2 = self.whistleFeatureFilter(median_blur_ch2)
        #     self.detection_image_ch1 = np.concatenate((self.detection_image_ch1, detection_ch1), axis=1)
        #     self.detection_image_ch2 = np.concatenate((self.detection_image_ch2, detection_ch2), axis=1)
            # self.DBSCANCluster(detection_ch1, 1)
            # self.DBSCANCluster(detection_ch2, 2)
    def animate(self, i):
        # time_stamp_1 = time.time()
        self.ax[0][0].clear()
        self.ax[0][1].clear()
        self.ax[1][0].clear()
        self.ax[1][1].clear()
        
        fft_ch1 = copy.copy(self.fft_ch1)
        fft_ch2 = copy.copy(self.fft_ch2)
        count_t = copy.copy(self.count_t)
        detection_image_ch1 = np.copy(self.detection_image_ch1)
        detection_image_ch2 = np.copy(self.detection_image_ch2)

        if(len(fft_ch1)>self.N):
            print("inside the hole: fft")
            fft_ch1 = fft_ch1[:self.N]
            fft_ch2 = fft_ch2[:self.N]
        if(len(detection_image_ch1)>self.N):
            print("inside the hole: detection")
            detection_image_ch1 = detection_image_ch1[:self.N]
            detection_image_ch2 = detection_image_ch2[:self.N]
        
        range_number = len(fft_ch1)
        if(range_number<self.N ):
            n = self.FFT_NUMBER_//2+1
            m = [0]*n
            for i in range(self.N-range_number):
                fft_ch1.append(m)
                fft_ch2.append(m)
        range_number = detection_image_ch1.shape[1]
        if(range_number<self.N):
            m = np.zeros((self.END_INDEX_-self.START_INDEX_, self.N-range_number))
            detection_image_ch1 = np.concatenate((detection_image_ch1, m), axis=1)
            detection_image_ch2 = np.concatenate((detection_image_ch2, m), axis=1)
        
        t_max = (len(fft_ch1)+count_t)*self.delta_t
        f_max = self.FS_/2

        half_size = math.ceil((self.FFT_NUMBER_+1)/2)
        f = np.arange(half_size)*self.FS_/self.FFT_NUMBER_
        
        # time_stamp_3 = time.time()
        self.ax[0][0].imshow(np.array(fft_ch1).T, cmap="jet", origin="lower", extent=[t_max-self.PLOT_LENGTH_, t_max, 0, f_max/1000])
        self.ax[0][0].axis('auto')
        self.ax[0][0].set_xlabel("Time(s)")
        self.ax[0][0].set_ylabel("Frequency(kHz)")
        self.ax[0][0].set_ylim([0, 20])
        # cbar_1 = fig.colorbar(im_1)

        self.ax[0][1].imshow(np.array(fft_ch2).T, cmap="jet", origin="lower", extent=[t_max-self.PLOT_LENGTH_, t_max, 0, f_max/1000])
        self.ax[0][1].axis('auto')
        self.ax[0][1].set_xlabel("Time(s)")
        self.ax[0][1].set_ylabel("Frequency(kHz)")
        self.ax[0][1].set_ylim([0, 20])
        # cbar_2 = fig.colorbar(im_2)
        self.ax[0][1].yaxis.set_label_position("right")
        self.ax[0][1].yaxis.set_ticks_position("right")

        # self.ax[1][0].imshow(detection_image_ch1.astype(np.int8), cmap="binary", origin="lower", extent=[t_max-self.PLOT_LENGTH_, t_max, f[self.START_INDEX_]/1000, f[self.END_INDEX_]/1000])
        # self.ax[1][0].axis('auto')
        # self.ax[1][0].set_xlabel("Time(s)")
        # self.ax[1][0].set_ylabel("Frequency(kHz)")
        # self.ax[1][0].set_ylim([0, 20])

        # self.ax[1][1].imshow(detection_image_ch2.astype(np.int8), cmap="binary", origin="lower", extent=[t_max-self.PLOT_LENGTH_, t_max, f[self.START_INDEX_]/1000, f[self.END_INDEX_]/1000])
        # self.ax[1][1].axis('auto')
        # self.ax[1][1].set_xlabel("Time(s)")
        # self.ax[1][1].set_ylabel("Frequency(kHz)")
        # self.ax[1][1].set_ylim([0, 20])
        # self.ax[1][1].yaxis.set_label_position("right")
        # self.ax[1][1].yaxis.set_ticks_position("right")
        print("fft_ch1 length: {}".format(len(self.fft_ch1)))
        print("fft_ch1 click removal length: {}".format(len(self.fft_ch1_click_removal)))

def main():
    rospy.init_node("detect_whistle_node", anonymous=True)
    detect_node = detect_whistle_node()
    ani = FuncAnimation(detect_node.fig, detect_node.animate, interval=detect_node.INTERVAL_)
    plt.show()
    # print("in the spin")
    
    rospy.spin()


if __name__ == "__main__":
    main()