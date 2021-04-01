/* Description:		program for saving the battery voltage data while executing
 * Data: 			2021_4_1
 * Author:			Shane
 */
#include<iostream>
#include<ctime>
#include<cstdio>
#include<string>
#include<sstream>
//for ros
#include<ros/ros.h>
#include<ros/console.h>
#include<std_msgs/Float64.h>

class monitor_battery_voltage_node{
public:
	monitor_battery_voltage_node();
	~monitor_battery_voltage_node();
private:
	void save_comm(const std_msgs::Float64&);
	void save_sys(const std_msgs::Float64&);
	ros::NodeHandle m_n_private;
	ros::NodeHandle m_n_public;
	ros::Subscriber m_sub_comm;
	ros::Subscriber m_sub_sys;

	FILE *m_fp_comm;
	FILE *m_fp_sys; 

	std::string m_file_path;
	int m_time_interval;
};

/*
 * Constructor
 */
monitor_battery_voltage_node::monitor_battery_voltage_node():
m_n_private("~")
{
	m_n_private.getParam("FILE_PATH_", m_file_path);
	m_n_private.getParam("TIME_INTERVAL_", m_time_interval);
	
	m_sub_comm = m_n_public.subscribe("/communication_battery", 1, &monitor_battery_voltage_node::save_comm, this);
	m_sub_sys = m_n_public.subscribe("/system_battery", 1, &monitor_battery_voltage_node::save_sys, this);
	std::string filename = m_file_path + "communication_bat.csv";
	m_fp_comm = fopen(filename.c_str(), "w");
	filename = m_file_path + "system_bat.csv";
	m_fp_sys = fopen(filename.c_str(), "w");

	ROS_INFO("setting finished.\n");
	ROS_INFO("file path:\t%s", m_file_path.c_str());
	ROS_INFO("time interval:\t%d", m_time_interval);
}

/*
 * communication battery callback function
 */
void monitor_battery_voltage_node::save_comm(const std_msgs::Float64 &msg){
	clock_t now = clock();
	std::stringstream ss;
	ss.str("");ss.clear();
	std::string s = "";

	ss<<msg.data<<",";
	ss>>s;
	
	fwrite(s.c_str(), 1, s.length(), m_fp_comm);
	while(double(clock()-now)/CLOCKS_PER_SEC < (m_time_interval/2));

	ROS_INFO("get communication battery data:\t%s", s.c_str());
}

/*
 * system battery callback function
 */
void monitor_battery_voltage_node::save_sys(const std_msgs::Float64 &msg){
	clock_t now = clock();
	std::stringstream ss;
	ss.str("");ss.clear();
	std::string s = "";

	ss<<msg.data<<",";
	ss>>s;
	
	fwrite(s.c_str(), 1, s.length(), m_fp_sys);
	while(double(clock()-now)/CLOCKS_PER_SEC < (m_time_interval/2));

	ROS_INFO("get system battery data:\t%s", s.c_str());
}

monitor_battery_voltage_node::~monitor_battery_voltage_node(){
	fseek(m_fp_comm, 1, SEEK_END);
	fseek(m_fp_sys, 1, SEEK_END);
	fwrite(" ", 1, 1, m_fp_comm);
	fwrite(" ", 1, 1, m_fp_sys);
	fclose(m_fp_comm);
	fclose(m_fp_sys);
	ROS_INFO("closing file");
}

/*
 *  Main function
 */
int main(int argc, char **argv){
	ros::init(argc, argv, "monitor_battery_voltage_node");
	monitor_battery_voltage_node node;
	ros::spin();
	return 0;
}
