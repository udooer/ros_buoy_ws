# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(WARNING "Invoking generate_messages() without having added any message or service file before.
You should either add add_message_files() and/or add_service_files() calls or remove the invocation of generate_messages().")
message(STATUS "get_sound_data: 0 messages, 0 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Intu_msgs:/home/yong/ros_buoy_ws/src/ntu_msgs/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(get_sound_data_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_cpp(get_sound_data
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/get_sound_data
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(get_sound_data_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(get_sound_data_generate_messages get_sound_data_generate_messages_cpp)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(get_sound_data_gencpp)
add_dependencies(get_sound_data_gencpp get_sound_data_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_sound_data_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_eus(get_sound_data
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/get_sound_data
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(get_sound_data_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(get_sound_data_generate_messages get_sound_data_generate_messages_eus)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(get_sound_data_geneus)
add_dependencies(get_sound_data_geneus get_sound_data_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_sound_data_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_lisp(get_sound_data
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/get_sound_data
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(get_sound_data_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(get_sound_data_generate_messages get_sound_data_generate_messages_lisp)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(get_sound_data_genlisp)
add_dependencies(get_sound_data_genlisp get_sound_data_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_sound_data_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_nodejs(get_sound_data
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/get_sound_data
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(get_sound_data_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(get_sound_data_generate_messages get_sound_data_generate_messages_nodejs)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(get_sound_data_gennodejs)
add_dependencies(get_sound_data_gennodejs get_sound_data_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_sound_data_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_py(get_sound_data
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_sound_data
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(get_sound_data_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(get_sound_data_generate_messages get_sound_data_generate_messages_py)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(get_sound_data_genpy)
add_dependencies(get_sound_data_genpy get_sound_data_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS get_sound_data_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/get_sound_data)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/get_sound_data
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(get_sound_data_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET ntu_msgs_generate_messages_cpp)
  add_dependencies(get_sound_data_generate_messages_cpp ntu_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/get_sound_data)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/get_sound_data
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(get_sound_data_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET ntu_msgs_generate_messages_eus)
  add_dependencies(get_sound_data_generate_messages_eus ntu_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/get_sound_data)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/get_sound_data
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(get_sound_data_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET ntu_msgs_generate_messages_lisp)
  add_dependencies(get_sound_data_generate_messages_lisp ntu_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/get_sound_data)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/get_sound_data
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(get_sound_data_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET ntu_msgs_generate_messages_nodejs)
  add_dependencies(get_sound_data_generate_messages_nodejs ntu_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_sound_data)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_sound_data\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/get_sound_data
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(get_sound_data_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET ntu_msgs_generate_messages_py)
  add_dependencies(get_sound_data_generate_messages_py ntu_msgs_generate_messages_py)
endif()
