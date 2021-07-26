# Install script for directory: /home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/magor/ws_cyton/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/industrial_msgs/msg" TYPE FILE FILES
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/msg/DebugLevel.msg"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/msg/DeviceInfo.msg"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/msg/RobotMode.msg"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/msg/RobotStatus.msg"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/msg/ServiceReturnCode.msg"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/msg/TriState.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/industrial_msgs/srv" TYPE FILE FILES
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/srv/CmdJointTrajectory.srv"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/srv/GetRobotInfo.srv"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/srv/SetDrivePower.srv"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/srv/SetRemoteLoggerLevel.srv"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/srv/StartMotion.srv"
    "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/srv/StopMotion.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/industrial_msgs/cmake" TYPE FILE FILES "/home/magor/ws_cyton/build/industrial_core-indigo-devel/industrial_msgs/catkin_generated/installspace/industrial_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/magor/ws_cyton/devel/include/industrial_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/magor/ws_cyton/devel/share/roseus/ros/industrial_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/magor/ws_cyton/devel/share/common-lisp/ros/industrial_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/magor/ws_cyton/devel/share/gennodejs/ros/industrial_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/magor/ws_cyton/devel/lib/python2.7/dist-packages/industrial_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/magor/ws_cyton/devel/lib/python2.7/dist-packages/industrial_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/magor/ws_cyton/build/industrial_core-indigo-devel/industrial_msgs/catkin_generated/installspace/industrial_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/industrial_msgs/cmake" TYPE FILE FILES "/home/magor/ws_cyton/build/industrial_core-indigo-devel/industrial_msgs/catkin_generated/installspace/industrial_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/industrial_msgs/cmake" TYPE FILE FILES
    "/home/magor/ws_cyton/build/industrial_core-indigo-devel/industrial_msgs/catkin_generated/installspace/industrial_msgsConfig.cmake"
    "/home/magor/ws_cyton/build/industrial_core-indigo-devel/industrial_msgs/catkin_generated/installspace/industrial_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/industrial_msgs" TYPE FILE FILES "/home/magor/ws_cyton/src/industrial_core-indigo-devel/industrial_msgs/package.xml")
endif()
