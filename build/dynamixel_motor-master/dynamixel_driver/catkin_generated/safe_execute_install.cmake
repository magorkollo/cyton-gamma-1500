execute_process(COMMAND "/home/magor/ws_cyton/build/dynamixel_motor-master/dynamixel_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/magor/ws_cyton/build/dynamixel_motor-master/dynamixel_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
