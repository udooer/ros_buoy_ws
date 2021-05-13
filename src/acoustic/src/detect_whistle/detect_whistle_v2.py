#!/usr/bin/env python3
# basic package you definitly know
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import pandas as pd
import os.path
import time

# package for image processing
import cv2

# package for clustering
from sklearn.cluster import DBSCAN

# import ros library
import rospy
from ntu_msgs.msg import HydrophoneFFTDataWithClickRemoval, DetectionImage

class detect_whistle_node:
    def __init__(self):
        self.getParameters()

        # member variable for subscribing  
        # from /compute_fft/two_mode_fft_data topic
        self.fft_ch1_click_removal = []
        self.fft_ch2_click_removal = []

        # Whistle Features
        self.whistle_count_ch1 = 0
        self.whistle_duration_ch1 = 0
        self.whistle_count_ch2 = 0
        self.whistle_duration_ch2 = 0


        self.msg = DetectionImage()
        # define subscriber and publisher
        rospy.Subscriber("/compute_fft/two_mode_fft_data", HydrophoneFFTDataWithClickRemoval, self.pushFFTData)
        self.pub = rospy.Publisher('/detect_whistle/detection_image', DetectionImage, queue_size=1)
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
        self.delta_t = data.delta_t
        self.delta_f = data.delta_f

        if(self.delta_f != self.DF_):
            print("WARNING!!! DELTA F IS NOT THE SAME.")

        self.DETECTOR_FRAME_LENGTH_ = int(self.DETECTOR_FRAME_/self.delta_t)
        if(len(self.fft_ch1_click_removal)>=self.DETECTOR_FRAME_LENGTH_):
            start_time = time.time()
            image_ch1 = np.array(self.fft_ch1_click_removal[:self.DETECTOR_FRAME_LENGTH_])
            image_ch2 = np.array(self.fft_ch2_click_removal[:self.DETECTOR_FRAME_LENGTH_])
            self.fft_ch1_click_removal = self.fft_ch1_click_removal[self.DETECTOR_FRAME_LENGTH_:]
            self.fft_ch2_click_removal = self.fft_ch2_click_removal[self.DETECTOR_FRAME_LENGTH_:]
            median_blur_ch1 = cv2.medianBlur(image_ch1.astype(np.float32),3)
            median_blur_ch2 = cv2.medianBlur(image_ch2.astype(np.float32),3)
            detection_ch1 = self.whistleFeatureFilter(median_blur_ch1)
            detection_ch2 = self.whistleFeatureFilter(median_blur_ch2)
            self.msg.col_ch1 = detection_ch1.flatten('F')
            self.msg.col_ch2 = detection_ch2.flatten('F')
            self.msg.df = self.delta_f
            self.msg.dt = self.delta_t
            self.msg.start_freq = self.START_FREQ_
            self.msg.end_freq = self.END_FREQ_
            self.msg.col_number = detection_ch1.shape[1]
            self.msg.col_length = detection_ch1.shape[0]
            self.pub.publish(self.msg)
            print("detection shape: {}".format(detection_ch1.shape))
            print("Computing {} seconds of data takes {} sec".format(self.DETECTOR_FRAME_, time.time()-start_time))
            print()
            # self.DBSCANCluster(detection_ch1, 1)
            # self.DBSCANCluster(detection_ch2, 2)

def main():
    rospy.init_node("detect_whistle_node", anonymous=True)
    detect_node = detect_whistle_node()
    rospy.spin()

if __name__ == "__main__":
    main()