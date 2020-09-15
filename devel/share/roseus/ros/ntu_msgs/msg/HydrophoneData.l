;; Auto-generated. Do not edit!


(when (boundp 'ntu_msgs::HydrophoneData)
  (if (not (find-package "NTU_MSGS"))
    (make-package "NTU_MSGS"))
  (shadow 'HydrophoneData (find-package "NTU_MSGS")))
(unless (find-package "NTU_MSGS::HYDROPHONEDATA")
  (make-package "NTU_MSGS::HYDROPHONEDATA"))

(in-package "ROS")
;;//! \htmlinclude HydrophoneData.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ntu_msgs::HydrophoneData
  :super ros::object
  :slots (_header _data_ch1 _data_ch2 _data_ch3 _data_ch4 _length _fs _bits _data_type ))

(defmethod ntu_msgs::HydrophoneData
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:data_ch1 __data_ch1) (make-array 0 :initial-element 0 :element-type :integer))
    ((:data_ch2 __data_ch2) (make-array 0 :initial-element 0 :element-type :integer))
    ((:data_ch3 __data_ch3) (make-array 0 :initial-element 0 :element-type :integer))
    ((:data_ch4 __data_ch4) (make-array 0 :initial-element 0 :element-type :integer))
    ((:length __length) 0)
    ((:fs __fs) 0)
    ((:bits __bits) 0)
    ((:data_type __data_type) "")
    )
   (send-super :init)
   (setq _header __header)
   (setq _data_ch1 __data_ch1)
   (setq _data_ch2 __data_ch2)
   (setq _data_ch3 __data_ch3)
   (setq _data_ch4 __data_ch4)
   (setq _length (round __length))
   (setq _fs (round __fs))
   (setq _bits (round __bits))
   (setq _data_type (string __data_type))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:data_ch1
   (&optional __data_ch1)
   (if __data_ch1 (setq _data_ch1 __data_ch1)) _data_ch1)
  (:data_ch2
   (&optional __data_ch2)
   (if __data_ch2 (setq _data_ch2 __data_ch2)) _data_ch2)
  (:data_ch3
   (&optional __data_ch3)
   (if __data_ch3 (setq _data_ch3 __data_ch3)) _data_ch3)
  (:data_ch4
   (&optional __data_ch4)
   (if __data_ch4 (setq _data_ch4 __data_ch4)) _data_ch4)
  (:length
   (&optional __length)
   (if __length (setq _length __length)) _length)
  (:fs
   (&optional __fs)
   (if __fs (setq _fs __fs)) _fs)
  (:bits
   (&optional __bits)
   (if __bits (setq _bits __bits)) _bits)
  (:data_type
   (&optional __data_type)
   (if __data_type (setq _data_type __data_type)) _data_type)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32[] _data_ch1
    (* 4    (length _data_ch1)) 4
    ;; int32[] _data_ch2
    (* 4    (length _data_ch2)) 4
    ;; int32[] _data_ch3
    (* 4    (length _data_ch3)) 4
    ;; int32[] _data_ch4
    (* 4    (length _data_ch4)) 4
    ;; int32 _length
    4
    ;; int32 _fs
    4
    ;; int32 _bits
    4
    ;; string _data_type
    4 (length _data_type)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32[] _data_ch1
     (write-long (length _data_ch1) s)
     (dotimes (i (length _data_ch1))
       (write-long (elt _data_ch1 i) s)
       )
     ;; int32[] _data_ch2
     (write-long (length _data_ch2) s)
     (dotimes (i (length _data_ch2))
       (write-long (elt _data_ch2 i) s)
       )
     ;; int32[] _data_ch3
     (write-long (length _data_ch3) s)
     (dotimes (i (length _data_ch3))
       (write-long (elt _data_ch3 i) s)
       )
     ;; int32[] _data_ch4
     (write-long (length _data_ch4) s)
     (dotimes (i (length _data_ch4))
       (write-long (elt _data_ch4 i) s)
       )
     ;; int32 _length
       (write-long _length s)
     ;; int32 _fs
       (write-long _fs s)
     ;; int32 _bits
       (write-long _bits s)
     ;; string _data_type
       (write-long (length _data_type) s) (princ _data_type s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32[] _data_ch1
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data_ch1 (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data_ch1 i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _data_ch2
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data_ch2 (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data_ch2 i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _data_ch3
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data_ch3 (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data_ch3 i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _data_ch4
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data_ch4 (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data_ch4 i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32 _length
     (setq _length (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _fs
     (setq _fs (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _bits
     (setq _bits (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _data_type
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data_type (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get ntu_msgs::HydrophoneData :md5sum-) "c7632af3f7726d3fc3bf79582f66f89c")
(setf (get ntu_msgs::HydrophoneData :datatype-) "ntu_msgs/HydrophoneData")
(setf (get ntu_msgs::HydrophoneData :definition-)
      "Header header
int32[] data_ch1
int32[] data_ch2
int32[] data_ch3
int32[] data_ch4
int32 length
int32 fs
int32 bits
string data_type

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :ntu_msgs/HydrophoneData "c7632af3f7726d3fc3bf79582f66f89c")


