#!/usr/bin/env python

import rospy
import std_msgs
from rospy import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import time
from std_msgs.msg import Float64
import sys
import robot_planning_class
from math import degrees, radians

import moveit_commander
import moveit_msgs.msg

def functional():
    pub_rosey = rospy.Publisher(
      '/cyton_joint_trajectory_action_controller/command',
      JointTrajectory, queue_size=10)
    rospy.init_node('traj_maker', anonymous=True)
    time.sleep(1)
   

    rate = rospy.Rate(0.01)
    while not rospy.is_shutdown():

           #  first way to define a point
           traj_waypoint_1_rosey = JointTrajectoryPoint()

           traj_waypoint_1_rosey.positions = [0,0,0,0,0,0,0]
           traj_waypoint_1_rosey.time_from_start = Duration(1)
           
           #  second way to define a point
           traj_waypoint_2_rosey = JointTrajectoryPoint()
           traj_waypoint_2_rosey.time_from_start = Duration(2)
           traj_waypoint_2_rosey.positions = [0,0,0,0,0, 1,0.25]
           
           time.sleep(1)

           traj_waypoint_3_rosey = JointTrajectoryPoint()
           traj_waypoint_3_rosey.time_from_start = Duration(3)
           traj_waypoint_3_rosey.positions = [0,0,0,0,0,-1,-0.25]

           traj_waypoint_4_rosey = JointTrajectoryPoint()
           traj_waypoint_4_rosey.time_from_start = Duration(4)
           traj_waypoint_4_rosey.positions = [0,0,0,0,0,0,0]

           #traj_waypoint_2_rosey = JointTrajectoryPoint(positions=[.31, -.051, .33, -.55, .28, .60,0],
            #time_from_start = Duration(4))
           #traj_waypoint_3_rosey = JointTrajectoryPoint(positions=[.14726, -.014151, .166507, -.33571, .395997, .38657,0],
            #time_from_start = Duration(6))
           #traj_waypoint_4_rosey = JointTrajectoryPoint(positions=[-.09309, .003150, .003559, .16149, .524427, -.1867,0],
            #time_from_start = Duration(8))
           #traj_waypoint_5_rosey = JointTrajectoryPoint(positions=[-.27752, .077886, -.1828, .38563, .682589, -.44665,0],
            #time_from_start = Duration(10))   
           #traj_waypoint_6_rosey = JointTrajectoryPoint(positions=[0,0,0,0,0,0,0],time_from_start = Duration(12))
           
           #  making message
           message_rosey = JointTrajectory()
           
           #  required headers
           header_rosey = std_msgs.msg.Header(stamp=rospy.Time.now())
           message_rosey.header = header_rosey
           
           #  adding in joints
           joint_names = ['shoulder_roll_joint', \
            'shoulder_pitch_joint', 'shoulder_yaw_joint', 'elbow_pitch_joint', \
            'elbow_yaw_joint', 'wrist_pitch_joint', 'wrist_roll_joint']
           message_rosey.joint_names = joint_names
           
           #  appending up to 100 points
           # ex. for i in enumerate(len(waypoints)): append(waypoints[i])

           message_rosey.points.append(traj_waypoint_1_rosey)
           message_rosey.points.append(traj_waypoint_2_rosey)
           message_rosey.points.append(traj_waypoint_3_rosey)
           message_rosey.points.append(traj_waypoint_4_rosey)
           #message_rosey.points.append(traj_waypoint_5_rosey)
           #message_rosey.points.append(traj_waypoint_6_rosey)
           #  publishing to ROS node
           pub_rosey.publish(message_rosey)
           print("Finished")
           rate.sleep()
           
           if rospy.is_shutdown():
               break
               

def gripperMove(move):
        gripper_publisher = rospy.Publisher(
            '/gripper_position_controller/command',
            Float64,queue_size=10)
        rospy.init_node('planning_background', anonymous=True)
        plan = ((move/100.)*2.4)-.5
        gripper_publisher.publish(plan)
        print("Finished: ", plan)

def initial():
    #rate = rospy.Rate(0.01)
    pub_rosey = rospy.Publisher(
      '/cyton_joint_trajectory_action_controller/command',
      JointTrajectory, queue_size=10)
    rospy.init_node('traj_maker', anonymous=True)
    time.sleep(1)

    traj_waypoint_1_rosey = JointTrajectoryPoint()
    traj_waypoint_1_rosey.positions = [0,0,0,0,0, 0,0]
    traj_waypoint_1_rosey.time_from_start = Duration(1)
    message_rosey = JointTrajectory()
    header_rosey = std_msgs.msg.Header(stamp=rospy.Time.now())
    message_rosey.header = header_rosey
    joint_names = ['shoulder_roll_joint', \
      'shoulder_pitch_joint', 'shoulder_yaw_joint', 'elbow_pitch_joint', \
      'elbow_yaw_joint', 'wrist_pitch_joint', 'wrist_roll_joint']
    message_rosey.joint_names = joint_names
    message_rosey.points.append(traj_waypoint_1_rosey)
    pub_rosey.publish(message_rosey)
    #rate.sleep()
    print("Gripper finished")
 

# def xyz(orientation, pose):

#     moveit_commander.roscpp_initialize(sys.argv)
#     robot = moveit_commander.RobotCommander(robot_description = "robot_description")
#     scene = moveit_commander.PlanningSceneInterface()
#     group = moveit_commander.MoveGroupCommander("manipulator_planning_group")
#     group.set_goal_position_tolerance(0.001)
#     group.set_goal_orientation_tolerance(0.01)
#     group.allow_replanning(True)
#     num_joints = len(group.get_active_joints())
#     display_trajectory_publisher = rospy.Publisher(
#         '/move_group/display_planned_path',
#         moveit_msgs.msg.DisplayTrajectory,queue_size=10)

#     group.clear_pose_targets()
#     waypoints = []
#     waypoints.append(group.get_current_pose().pose)

#     quaternion = tf.transformations.quaternion_from_euler(
#         orientation[0], orientation[1], orientation[2])
#     wpose = geometry_msgs.msg.Pose()
#     wpose.orientation.x = quaternion[0]
#     wpose.orientation.y = quaternion[1]
#     wpose.orientation.z = quaternion[2]
#     wpose.orientation.w = quaternion[3]
#     wpose.position.x = pose[0]
#     wpose.position.y = pose[1]
#     wpose.position.z = pose[2]
#     waypoints.append(copy.deepcopy(wpose))

#     (plan, fraction) = group.compute_cartesian_path(waypoints, 0.01, 0.0)
#     plan = timeParamzn(plan, True)
#     try:
#         if execute:
#                 # execute path
#             group.execute(plan, wait=False)
#         else:
#             stored_plan = plan
#     except:
#         print("Cannot be executed")
    


# def timeParamzn(plan, cart=False):
#     #paramaterize time based on a velocity scaling factor
#     new_traj = moveit_msgs.msg.RobotTrajectory()
#     new_traj.joint_trajectory = plan.joint_trajectory
#     n_joints = len(plan.joint_trajectory.joint_names)
#     n_points = len(plan.joint_trajectory.points)

#     spd = 1

#     for i in range(n_points):
#         new_traj.joint_trajectory.points[i].time_from_start = \
#             plan.joint_trajectory.points[i].time_from_start / spd

#         if (cart and i==n_points-1):
#             return new_traj   

#     for i in range(n_points):

#         new_traj.joint_trajectory.points[i].velocities = \
#             list(new_traj.joint_trajectory.points[i].velocities)

#         new_traj.joint_trajectory.points[i].accelerations = \
#             list(new_traj.joint_trajectory.points[i].accelerations)

#         new_traj.joint_trajectory.points[i].positions = \
#             list(new_traj.joint_trajectory.points[i].positions)

#         for j in range(n_joints):

#             new_traj.joint_trajectory.points[i].velocities[j] = \
#                 plan.joint_trajectory.points[i].velocities[j] * spd
#             new_traj.joint_trajectory.points[i].accelerations[j] = \
#                 plan.joint_trajectory.points[i].accelerations[j] * spd * spd
#             new_traj.joint_trajectory.points[i].positions[j] = \
#                 plan.joint_trajectory.points[i].positions[j]

#         new_traj.joint_trajectory.points[i].velocities = \
#             tuple(new_traj.joint_trajectory.points[i].velocities)

#         new_traj.joint_trajectory.points[i].accelerations = \
#             tuple(new_traj.joint_trajectory.points[i].accelerations)

#         new_traj.joint_trajectory.points[i].positions = \
#             tuple(new_traj.joint_trajectory.points[i].positions)

#     return new_traj



if __name__ == '__main__':
    axis = sys.argv[1]
    axis = int(axis)
    if(axis == 0):
        try:
            functional()
        except rospy.ROSInterruptException:
            pass
    elif(axis == 1):
        rospy.init_node('planning_background', anonymous=True)
        action = robot_planning_class.CytonMotion()
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        z = float(sys.argv[4])
        Ex = float(sys.argv[5])
        Ey = float(sys.argv[6])
        Ez = float(sys.argv[7])
        action.moveCartesian([Ex,Ey,Ez],[x,y,z],True)
        print(x , " " , y , " " , z)
        print("Finished")
    elif(axis == 2):
       move = float(sys.argv[2])
       gripperMove(move)
    elif(axis == 3):
        rospy.init_node('planning_background', anonymous=True)
        action = robot_planning_class.CytonMotion()
        action.moveJoint([0,0,0,0,0,1,0], False)
    elif(axis == 4):
        try:
            initial()
        except rospy.ROSInterruptException:
            pass
    elif(axis == 5):
        Ex = 0
        Ey = 0
        Ez = 0
        x = -1
        y = 0
        z = 0
        xyz([Ex,Ey,Ez],[x,y,z])







