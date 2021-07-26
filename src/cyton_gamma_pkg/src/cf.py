#!/usr/bin/env python
from __future__ import division 
import sys
from sensor_msgs.msg import JointState
import copy
import rospy
from std_msgs.msg import Float64
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import PyQt5
from PyQt5 import QtWidgets
import tf
from math import degrees, radians
import rviz
import robot_planning_class

class CommandCenter(QtWidgets.QMainWindow):

    def __init__(self,parent=None):

        # get input for specific robot
        self.robot = '1500'

        #make window and initialize ROS node
        PyQt5.QtWidgets.QWidget.__init__(self, parent)
        rospy.init_node('planning_background',
                    anonymous=True)
       
        self.init()
        self.action = robot_planning_class.CytonMotion()


    def init(self):
        #initilize the window and populate

        PyQt5.QtWidgets.QToolTip.setFont(PyQt5.QtGui.QFont(
                                        'SansSerif', 10))

        self.init_buttons()     
        self.init_labels()
        self.init_fields()
        
        self.setGeometry(500, 500, 240, 500)
        self.setWindowTitle('Command Center')    
        self.show()

    def init_buttons(self):
        #initialize all the buttons and locations

        self.commandButJ = PyQt5.QtWidgets.QPushButton(
                                  'CommandJ', self)
        self.commandButJ.setToolTip('Command trajectory')
        self.commandButJ.resize(self.commandButJ.sizeHint())
        self.commandButJ.move(120, 340) 
        self.commandButJ.clicked.connect(self.commandJF)
        
        self.planButtonJ = PyQt5.QtWidgets.QPushButton('PlanJ', self)
        self.planButtonJ.setToolTip('Plan Trajectory')
        self.planButtonJ.resize(self.commandButJ.sizeHint())
        self.planButtonJ.move(120, 300)  
        self.planButtonJ.clicked.connect(self.planJF)

        self.commandButL = PyQt5.QtWidgets.QPushButton(
                                   'CommandL', self)
        self.commandButL.setToolTip('Command trajectory')
        self.commandButL.resize(self.commandButL.sizeHint())
        self.commandButL.move(20, 340) 
        self.commandButL.clicked.connect(self.commandLF)

        self.planButtonL = PyQt5.QtWidgets.QPushButton('PlanL', self)
        self.planButtonL.setToolTip('Plan Trajectory')
        self.planButtonL.resize(self.commandButL.sizeHint())
        self.planButtonL.move(20, 300)  
        self.planButtonL.clicked.connect(self.planLF)

        self.Gripbutton = PyQt5.QtWidgets.QPushButton('Move Gripper\n[0 100]', self)

        self.Gripbutton.setToolTip('Close Grippers')
        self.Gripbutton.resize(180,80)
        self.Gripbutton.move(20, 380)  
        self.Gripbutton.clicked.connect(self.moveGripper)

        self.deltaBox = PyQt5.QtWidgets.QCheckBox(self)
        self.deltaBox.setToolTip("Indicate Delta Moves")
        self.deltaBox.move(60,250)
        self.deltaBox.resize(20,20)


    def init_labels(self):
        #initialize all the labels and locations
        LinearLab = PyQt5.QtWidgets.QLabel('Delta Moves',self)
        LinearLab.move(30,220)


        LinearLab = PyQt5.QtWidgets.QLabel('  Linear',self)
        LinearLab.move(50,0)
        LinearLab.resize(60,20)

        JointLab = PyQt5.QtWidgets.QLabel('    Joint',self)
        JointLab.move(150,0)
        JointLab.resize(60,20)

        inputXLab = PyQt5.QtWidgets.QLabel('X',self)
        inputXLab.move(10,20)
        inputXLab.resize(60,30)

        inputYLab = PyQt5.QtWidgets.QLabel('Y',self)
        inputYLab.move(10,50)
        inputYLab.resize(60,30)

        inputZLab = PyQt5.QtWidgets.QLabel('Z',self)
        inputZLab.move(10,80)
        inputZLab.resize(60,30)

        inputXLab = PyQt5.QtWidgets.QLabel('J1',self)
        inputXLab.move(120,20)
        inputXLab.resize(60,30)

        inputYLab = PyQt5.QtWidgets.QLabel('J2',self)
        inputYLab.move(120,50)
        inputYLab.resize(60,30)

        inputZLab = PyQt5.QtWidgets.QLabel('J3',self)
        inputZLab.move(120,80)
        inputZLab.resize(60,30)

        inputXLab = PyQt5.QtWidgets.QLabel('J4',self)
        inputXLab.move(120,110)
        inputXLab.resize(60,30)

        inputYLab = PyQt5.QtWidgets.QLabel('J5',self)
        inputYLab.move(120,140)
        inputYLab.resize(60,30)

        inputZLab = PyQt5.QtWidgets.QLabel('J6',self)
        inputZLab.move(120,170)
        inputZLab.resize(60,30)

        inputZLab = PyQt5.QtWidgets.QLabel('J7',self)
        inputZLab.move(120,200)
        inputZLab.resize(60,30)

        inputZLab = PyQt5.QtWidgets.QLabel('Grip',self)
        inputZLab.move(120,240)
        inputZLab.resize(60,30)

        inputRXLab = PyQt5.QtWidgets.QLabel('RotX',self)
        inputRXLab.move(10,125)
        inputRXLab.resize(60,20)

        inputRYLab = PyQt5.QtWidgets.QLabel('RotY',self)
        inputRYLab.move(10,150)
        inputRYLab.resize(60,30)

        inputRZLab = PyQt5.QtWidgets.QLabel('RotZ',self)
        inputRZLab.move(10,180)
        inputRZLab.resize(60,30)

    def init_fields(self):
        #initialize all the fields and locations
        self.inputX = PyQt5.QtWidgets.QLineEdit(self)
        self.inputX.move(50,20)
        self.inputX.resize(60,30)

        self.inputY = PyQt5.QtWidgets.QLineEdit(self)
        self.inputY.move(50,50)
        self.inputY.resize(60,30)

        self.inputZ = PyQt5.QtWidgets.QLineEdit(self)
        self.inputZ.move(50,80)
        self.inputZ.resize(60,30)

        self.inputRotX = PyQt5.QtWidgets.QLineEdit(self)
        self.inputRotX.move(50,120)
        self.inputRotX.resize(60,30)

        self.inputRotY = PyQt5.QtWidgets.QLineEdit(self)
        self.inputRotY.move(50,150)
        self.inputRotY.resize(60,30)

        self.inputRotZ = PyQt5.QtWidgets.QLineEdit(self)
        self.inputRotZ.move(50,180)
        self.inputRotZ.resize(60,30)

        self.inputR1 = PyQt5.QtWidgets.QLineEdit(self)
        self.inputR1.move(150,20)
        self.inputR1.resize(60,30)

        self.inputR2 = PyQt5.QtWidgets.QLineEdit(self)
        self.inputR2.move(150,50)
        self.inputR2.resize(60,30)

        self.inputR3 = PyQt5.QtWidgets.QLineEdit(self)
        self.inputR3.move(150,80)
        self.inputR3.resize(60,30)

        self.inputR4 = PyQt5.QtWidgets.QLineEdit(self)
        self.inputR4.move(150,110)
        self.inputR4.resize(60,30)

        self.inputR5 = PyQt5.QtWidgets.QLineEdit(self)
        self.inputR5.move(150,140)
        self.inputR5.resize(60,30)

        self.inputR6 = PyQt5.QtWidgets.QLineEdit(self)
        self.inputR6.move(150,170)
        self.inputR6.resize(60,30)

        self.inputR7 = PyQt5.QtWidgets.QLineEdit(self)
        self.inputR7.move(150,200)
        self.inputR7.resize(60,30)

        self.inputRG = PyQt5.QtWidgets.QLineEdit(self)
        self.inputRG.move(150,240)
        self.inputRG.resize(60,30)


    def commandJF(self):
        #send command to the joint task in the planning class
        J1 = radians(float(self.inputR1.text()))
        J2 = radians(float(self.inputR2.text()))
        J3 = radians(float(self.inputR3.text()))
        J4 = radians(float(self.inputR4.text()))
        J5 = radians(float(self.inputR5.text()))
        J6 = radians(float(self.inputR6.text()))
        J7 = radians(float(self.inputR7.text()))

        if self.deltaBox.isChecked():
            self.action.deltaMoveJoint(
           [J1,J2,J3,J4,J5,J6,J7],True)
        else:
            self.action.moveJoint([J1,J2,J3,J4,J5,J6,J7],True)


    def planJF(self):
        #send plan request to the joint task in the planning class
        J1 = radians(float(self.inputR1.text()))
        J2 = radians(float(self.inputR2.text()))
        J3 = radians(float(self.inputR3.text()))
        J4 = radians(float(self.inputR4.text()))
        J5 = radians(float(self.inputR5.text()))
        J6 = radians(float(self.inputR6.text()))
        J7 = radians(float(self.inputR7.text()))

        if self.deltaBox.isChecked():
            self.action.deltaMoveJoint([J1,J2,J3,J4,J5,J6,J7],
                                                        False)
        else:
            self.action.moveJoint([J1,J2,J3,J4,J5,J6,J7],
                                                        False)

    def commandLF(self):
        #send command to the linear task in the planning class
        x = float(self.inputX.text())
        y = float(self.inputY.text())
        z = float(self.inputZ.text())
        Ex = radians(float(self.inputRotX.text()))
        Ey = radians(float(self.inputRotY.text()))
        Ez = radians(float(self.inputRotZ.text()))

        if self.deltaBox.isChecked():
            self.action.deltaMoveCartesian([Ex,Ey,Ez],[x,y,z],True)
        else:
            self.action.moveCartesian([Ex,Ey,Ez],[x,y,z],True)


    def planLF(self):
        #send planning request to the linear task in the planning class
        x = float(self.inputX.text())
        y = float(self.inputY.text())
        z = float(self.inputZ.text())
        Ex = radians(float(self.inputRotX.text()))
        Ey = radians(float(self.inputRotY.text()))
        Ez = radians(float(self.inputRotZ.text()))

        if self.deltaBox.isChecked():
            self.action.deltaMoveCartesian([Ex,Ey,Ez],
                                                 [x,y,z],False)
        else:
            self.action.moveCartesian([Ex,Ey,Ez],[x,y,z],False)

    def moveGripper(self):
        #send command to the gripper task in the hardware
        move = float(self.inputRG.text())

        if self.rob == '1500':
            move = ((move/100.)*2.4)-.5
        else:
            move = ((move/100.)*1.3)-.6
        print move

        self.action.moveGripper(move)


if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    myapp = CommandCenter()
    myapp.show()
    sys.exit(app.exec_())