/*program for saving the hydrophone data as wave file in sd card
  written by Shane 
  2020_12_14
 */
#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
#include<ctime>
#include<cmath>
//for ROS
#include<ros/ros.h>
#include"ntu_msgs/HydrophoneData.h"


using namespace std;

// define standard wave file struct  
struct header{
    char chunk_id[4]={'R', 'I', 'F', 'F'};
    int chunk_size;
    char format[4]={'W', 'A', 'V', 'E'};
    char subchunk1_id[4] = {'f', 'm', 't', ' '};
    int subchunk1_size = 16;
    short int audio_format = 1;
    short int num_channels;
    int sample_rate;
    int byte_rate;
    short int block_align;
    short int bits_per_sample;
    char subchunk2_id[4] = {'d', 'a', 't', 'a'};
    int subchunk2_size;    
}header_file;

// define a funtion getting the current UTC time for the wave file name 
string getTime(){
    time_t now = time(0);
    tm *ts = localtime(&now);
    stringstream ss;
    string date;
    ss<<1900+ts->tm_year<<"-"<<1+ts->tm_mon<<\
    "-"<<ts->tm_mday<<"_"<<ts->tm_hour-8<<":"<<\
    ts->tm_min<<":"<<ts->tm_sec;
    ss>>date;
    return date;
}

class save_data_node
{
public:
    save_data_node();
    ~save_data_node();

    //ROS parameter
    ros::NodeHandle nh_private;
    ros::NodeHandle nh_public;
    ros::Subscriber sub;

private:
    void push(const ntu_msgs::HydrophoneData &);
    
    // config file 
    string  FILE_PATH_;
    int FILE_LENGTH_;
    int NUM_CHANNELS_;
    int SAMPLING_RATE_;
    int RESOLUTION_;

    unsigned int m_count;   // count the data length
    unsigned int m_MAX;
    FILE* fp;               // file pointer 

};

/*                                   */
/************ Constructor ************/
/*                                   */
save_data_node::save_data_node():
nh_private("~"), m_count(0)
{
    // Get setting from yaml file
    nh_private.getParam("FILE_PATH_", FILE_PATH_);
    nh_private.getParam("FILE_LENGTH_", FILE_LENGTH_);
    nh_private.getParam("NUM_CHANNELS_", NUM_CHANNELS_);
    nh_private.getParam("SAMPLING_RATE_", SAMPLING_RATE_);
    nh_private.getParam("RESOLUTION_", RESOLUTION_);
    ROS_INFO_STREAM("setting success\n");
    ROS_INFO_STREAM("file path:\t\t" + FILE_PATH_);
    ROS_INFO_STREAM("file length(min):\t"<<FILE_LENGTH_);
    ROS_INFO_STREAM("NUM_CHANNELS_:\t\t"<<NUM_CHANNELS_);
    ROS_INFO_STREAM("SAMPLING_RATE_:\t\t"<<SAMPLING_RATE_);
    ROS_INFO_STREAM("RESOLUTION_:\t\t"<<RESOLUTION_);

    m_MAX = FILE_LENGTH_*60*SAMPLING_RATE_;
    // Set wave header file
    header_file.chunk_size = FILE_LENGTH_*60*SAMPLING_RATE_*NUM_CHANNELS_*RESOLUTION_/8+44;
    header_file.num_channels = (short int)NUM_CHANNELS_;
    header_file.sample_rate = SAMPLING_RATE_;
    header_file.byte_rate = SAMPLING_RATE_*RESOLUTION_/8*NUM_CHANNELS_;
    header_file.block_align = (short int)(RESOLUTION_/8*NUM_CHANNELS_);
    header_file.bits_per_sample = (short int)(RESOLUTION_);
    header_file.subchunk2_size = FILE_LENGTH_*60*SAMPLING_RATE_*NUM_CHANNELS_*RESOLUTION_/8;

    // Set ROS subscriber
    sub = nh_public.subscribe("/get_sound_data_for2i2/hydrophone_data", 1000, &save_data_node::push, this);
}
/*                                   */
/************* Destructor ************/
/*                                   */
save_data_node::~save_data_node(){
    int data=0;
    for(int i=m_count;i<m_MAX;i++){
        fwrite(&data, 4, 1, fp);
        fwrite(&data, 4, 1, fp);
    }
    fclose(fp);
    ROS_INFO("Close the file.");
}
// Define the push callback function 
void save_data_node::push(const ntu_msgs::HydrophoneData &msg){
    clock_t begin = clock();
    if(m_count==0){
        string filename = getTime()+".wav";
        ROS_INFO_STREAM("OPENNING NEW FILE: "<<filename<<" !!!");
        filename = FILE_PATH_ + filename;
        fp = fopen(filename.c_str(), "wb");
        fwrite(&header_file, 44, 1, fp);
    }
    vector<double> ch1 = msg.data_ch1;
    vector<double> ch2 = msg.data_ch2;
    int length = msg.length;
    int fs = msg.fs;
    int data;
    for(int i=0;i<length;i++){
        data = (int)(ch1.at(i)*pow(2, 31));
        fwrite(&data, 4, 1, fp);
        data = (int)(ch2.at(i)*pow(2, 31));
        fwrite(&data, 4, 1, fp);
    }
    m_count += length;
    if(m_count>=m_MAX){
        m_count = 0;
        fclose(fp);
        ROS_INFO("CLOSING FILE !!!");
    }
    clock_t end = clock();
    double elapsed_secs = double(end-begin)/CLOCKS_PER_SEC;
    ROS_INFO_STREAM("length:"<<length<<",sampling_rate:"<<fs<<",time:"<<elapsed_secs);
}

int main(int argc, char** argv){
    ros::init(argc, argv, "save_data_note");
    save_data_node save_obj;
    ros::spin();
    return 0;
}