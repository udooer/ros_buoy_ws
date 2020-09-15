; Auto-generated. Do not edit!


(cl:in-package ntu_msgs-msg)


;//! \htmlinclude HydrophoneData.msg.html

(cl:defclass <HydrophoneData> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (data_ch1
    :reader data_ch1
    :initarg :data_ch1
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (data_ch2
    :reader data_ch2
    :initarg :data_ch2
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (data_ch3
    :reader data_ch3
    :initarg :data_ch3
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (data_ch4
    :reader data_ch4
    :initarg :data_ch4
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0))
   (length
    :reader length
    :initarg :length
    :type cl:integer
    :initform 0)
   (fs
    :reader fs
    :initarg :fs
    :type cl:integer
    :initform 0)
   (bits
    :reader bits
    :initarg :bits
    :type cl:integer
    :initform 0)
   (data_type
    :reader data_type
    :initarg :data_type
    :type cl:string
    :initform ""))
)

(cl:defclass HydrophoneData (<HydrophoneData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HydrophoneData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HydrophoneData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ntu_msgs-msg:<HydrophoneData> is deprecated: use ntu_msgs-msg:HydrophoneData instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:header-val is deprecated.  Use ntu_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'data_ch1-val :lambda-list '(m))
(cl:defmethod data_ch1-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:data_ch1-val is deprecated.  Use ntu_msgs-msg:data_ch1 instead.")
  (data_ch1 m))

(cl:ensure-generic-function 'data_ch2-val :lambda-list '(m))
(cl:defmethod data_ch2-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:data_ch2-val is deprecated.  Use ntu_msgs-msg:data_ch2 instead.")
  (data_ch2 m))

(cl:ensure-generic-function 'data_ch3-val :lambda-list '(m))
(cl:defmethod data_ch3-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:data_ch3-val is deprecated.  Use ntu_msgs-msg:data_ch3 instead.")
  (data_ch3 m))

(cl:ensure-generic-function 'data_ch4-val :lambda-list '(m))
(cl:defmethod data_ch4-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:data_ch4-val is deprecated.  Use ntu_msgs-msg:data_ch4 instead.")
  (data_ch4 m))

(cl:ensure-generic-function 'length-val :lambda-list '(m))
(cl:defmethod length-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:length-val is deprecated.  Use ntu_msgs-msg:length instead.")
  (length m))

(cl:ensure-generic-function 'fs-val :lambda-list '(m))
(cl:defmethod fs-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:fs-val is deprecated.  Use ntu_msgs-msg:fs instead.")
  (fs m))

(cl:ensure-generic-function 'bits-val :lambda-list '(m))
(cl:defmethod bits-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:bits-val is deprecated.  Use ntu_msgs-msg:bits instead.")
  (bits m))

(cl:ensure-generic-function 'data_type-val :lambda-list '(m))
(cl:defmethod data_type-val ((m <HydrophoneData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ntu_msgs-msg:data_type-val is deprecated.  Use ntu_msgs-msg:data_type instead.")
  (data_type m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HydrophoneData>) ostream)
  "Serializes a message object of type '<HydrophoneData>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data_ch1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'data_ch1))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data_ch2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'data_ch2))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data_ch3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'data_ch3))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data_ch4))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'data_ch4))
  (cl:let* ((signed (cl:slot-value msg 'length)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'fs)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'bits)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data_type))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HydrophoneData>) istream)
  "Deserializes a message object of type '<HydrophoneData>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data_ch1) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data_ch1)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data_ch2) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data_ch2)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data_ch3) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data_ch3)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data_ch4) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data_ch4)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'length) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'fs) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'bits) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HydrophoneData>)))
  "Returns string type for a message object of type '<HydrophoneData>"
  "ntu_msgs/HydrophoneData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HydrophoneData)))
  "Returns string type for a message object of type 'HydrophoneData"
  "ntu_msgs/HydrophoneData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HydrophoneData>)))
  "Returns md5sum for a message object of type '<HydrophoneData>"
  "c7632af3f7726d3fc3bf79582f66f89c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HydrophoneData)))
  "Returns md5sum for a message object of type 'HydrophoneData"
  "c7632af3f7726d3fc3bf79582f66f89c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HydrophoneData>)))
  "Returns full string definition for message of type '<HydrophoneData>"
  (cl:format cl:nil "Header header~%int32[] data_ch1~%int32[] data_ch2~%int32[] data_ch3~%int32[] data_ch4~%int32 length~%int32 fs~%int32 bits~%string data_type~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HydrophoneData)))
  "Returns full string definition for message of type 'HydrophoneData"
  (cl:format cl:nil "Header header~%int32[] data_ch1~%int32[] data_ch2~%int32[] data_ch3~%int32[] data_ch4~%int32 length~%int32 fs~%int32 bits~%string data_type~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HydrophoneData>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data_ch1) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data_ch2) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data_ch3) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data_ch4) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4
     4
     4
     4 (cl:length (cl:slot-value msg 'data_type))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HydrophoneData>))
  "Converts a ROS message object to a list"
  (cl:list 'HydrophoneData
    (cl:cons ':header (header msg))
    (cl:cons ':data_ch1 (data_ch1 msg))
    (cl:cons ':data_ch2 (data_ch2 msg))
    (cl:cons ':data_ch3 (data_ch3 msg))
    (cl:cons ':data_ch4 (data_ch4 msg))
    (cl:cons ':length (length msg))
    (cl:cons ':fs (fs msg))
    (cl:cons ':bits (bits msg))
    (cl:cons ':data_type (data_type msg))
))
