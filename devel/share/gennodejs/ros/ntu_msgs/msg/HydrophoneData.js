// Auto-generated. Do not edit!

// (in-package ntu_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class HydrophoneData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.data_ch1 = null;
      this.data_ch2 = null;
      this.data_ch3 = null;
      this.data_ch4 = null;
      this.length = null;
      this.fs = null;
      this.bits = null;
      this.data_type = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('data_ch1')) {
        this.data_ch1 = initObj.data_ch1
      }
      else {
        this.data_ch1 = [];
      }
      if (initObj.hasOwnProperty('data_ch2')) {
        this.data_ch2 = initObj.data_ch2
      }
      else {
        this.data_ch2 = [];
      }
      if (initObj.hasOwnProperty('data_ch3')) {
        this.data_ch3 = initObj.data_ch3
      }
      else {
        this.data_ch3 = [];
      }
      if (initObj.hasOwnProperty('data_ch4')) {
        this.data_ch4 = initObj.data_ch4
      }
      else {
        this.data_ch4 = [];
      }
      if (initObj.hasOwnProperty('length')) {
        this.length = initObj.length
      }
      else {
        this.length = 0;
      }
      if (initObj.hasOwnProperty('fs')) {
        this.fs = initObj.fs
      }
      else {
        this.fs = 0;
      }
      if (initObj.hasOwnProperty('bits')) {
        this.bits = initObj.bits
      }
      else {
        this.bits = 0;
      }
      if (initObj.hasOwnProperty('data_type')) {
        this.data_type = initObj.data_type
      }
      else {
        this.data_type = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type HydrophoneData
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [data_ch1]
    bufferOffset = _arraySerializer.int32(obj.data_ch1, buffer, bufferOffset, null);
    // Serialize message field [data_ch2]
    bufferOffset = _arraySerializer.int32(obj.data_ch2, buffer, bufferOffset, null);
    // Serialize message field [data_ch3]
    bufferOffset = _arraySerializer.int32(obj.data_ch3, buffer, bufferOffset, null);
    // Serialize message field [data_ch4]
    bufferOffset = _arraySerializer.int32(obj.data_ch4, buffer, bufferOffset, null);
    // Serialize message field [length]
    bufferOffset = _serializer.int32(obj.length, buffer, bufferOffset);
    // Serialize message field [fs]
    bufferOffset = _serializer.int32(obj.fs, buffer, bufferOffset);
    // Serialize message field [bits]
    bufferOffset = _serializer.int32(obj.bits, buffer, bufferOffset);
    // Serialize message field [data_type]
    bufferOffset = _serializer.string(obj.data_type, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type HydrophoneData
    let len;
    let data = new HydrophoneData(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [data_ch1]
    data.data_ch1 = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [data_ch2]
    data.data_ch2 = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [data_ch3]
    data.data_ch3 = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [data_ch4]
    data.data_ch4 = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [length]
    data.length = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [fs]
    data.fs = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [bits]
    data.bits = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [data_type]
    data.data_type = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 4 * object.data_ch1.length;
    length += 4 * object.data_ch2.length;
    length += 4 * object.data_ch3.length;
    length += 4 * object.data_ch4.length;
    length += object.data_type.length;
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ntu_msgs/HydrophoneData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c7632af3f7726d3fc3bf79582f66f89c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new HydrophoneData(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.data_ch1 !== undefined) {
      resolved.data_ch1 = msg.data_ch1;
    }
    else {
      resolved.data_ch1 = []
    }

    if (msg.data_ch2 !== undefined) {
      resolved.data_ch2 = msg.data_ch2;
    }
    else {
      resolved.data_ch2 = []
    }

    if (msg.data_ch3 !== undefined) {
      resolved.data_ch3 = msg.data_ch3;
    }
    else {
      resolved.data_ch3 = []
    }

    if (msg.data_ch4 !== undefined) {
      resolved.data_ch4 = msg.data_ch4;
    }
    else {
      resolved.data_ch4 = []
    }

    if (msg.length !== undefined) {
      resolved.length = msg.length;
    }
    else {
      resolved.length = 0
    }

    if (msg.fs !== undefined) {
      resolved.fs = msg.fs;
    }
    else {
      resolved.fs = 0
    }

    if (msg.bits !== undefined) {
      resolved.bits = msg.bits;
    }
    else {
      resolved.bits = 0
    }

    if (msg.data_type !== undefined) {
      resolved.data_type = msg.data_type;
    }
    else {
      resolved.data_type = ''
    }

    return resolved;
    }
};

module.exports = HydrophoneData;
