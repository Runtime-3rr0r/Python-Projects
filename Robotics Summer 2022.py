#!/usr/bin/env python3

"""
Name: Robotics Testing.py
Project Number: 3
Author: Christian M
Date: Aug 3, 2022
"""

from vex import *
import urandom

brain = Brain()

Left_motor_a = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
Left_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
Left = MotorGroup(Left_motor_a, Left_motor_b)
Right_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
Right_motor_b = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
Right = MotorGroup(Right_motor_a, Right_motor_b)
controller_1 = Controller(PRIMARY)
launch_motor_a = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
launch_motor_b = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)
launch = MotorGroup(launch_motor_a, launch_motor_b)
red1 = Led(brain.three_wire_port.a)
red2 = Led(brain.three_wire_port.b)
red3 = Led(brain.three_wire_port.c)
red4 = Led(brain.three_wire_port.d)
red5 = Led(brain.three_wire_port.e)
Yellow = Led(brain.three_wire_port.f)

wait(30, MSEC)

def pre_autonomous():
    speed = 100
    direction = 'forward'

    Left.set_velocity(speed, PERCENT)
    Right.set_velocity(speed, PERCENT)

    launch.set_max_torque(100, PERCENT)
    launch.set_velocity(100, PERCENT)
    
    wait(1, SECONDS)

def autonomous():
    brain.screen.clear_screen()

def user_control():
    brain.screen.clear_screen
    count = 0

    while True:
        count += 1

        if launch_motor_a.velocity(RPM) >= 11:
            red1.on()
        else:
            red1.off()
            red2.off()
            red3.off()
            red4.off()
            red5.off()
            Yellow.off()

        if launch_motor_a.velocity(RPM) >= 22:
            red2.on()

        if launch_motor_a.velocity(RPM) >= 33:
            red3.on()

        if launch_motor_a.velocity(RPM) >= 44:
            red4.on()

        if launch_motor_a.velocity(RPM) >= 55:
            red5.on()

        if launch_motor_a.velocity(RPM) >= 66: # Check this area
            if count <= 10:
                Yellow.on()
            else:
                Yellow.off()
            
            controller_1.rumble('...')

        if controller_1.buttonA.pressing():
            launch.spin(FORWARD)
        elif controller_1.buttonB.pressing():
            launch.stop()
        
        if count == 20: # make sure this works
            count = 0

        if launch_motor_a.velocity(RPM) >= 66: # Change to optimal value
            brain.screen.set_cursor(1, 1)
            brain.screen.set_pen_color(Color.GREEN)
            brain.screen.print('Launch A RPM:', launch_motor_a.velocity(PERCENT))
        else:
            brain.screen.set_cursor(1, 1)
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print('Launch A RPM:', launch_motor_a.velocity(PERCENT))
        
        if launch_motor_b.velocity(RPM) >= 66: # change to optimal value
            brain.screen.set_cursor(2, 1)
            brain.screen.set_pen_color(Color.GREEN)
            brain.screen.print('Launch B RPM:', launch_motor_b.velocity(PERCENT))
        else:
            brain.screen.set_cursor(2, 1)
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print('Launch B RPM:', launch_motor_b.velocity(PERCENT))

        brain.screen.set_cursor(4, 1)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.print('Motor Temperatures:')

        if launch_motor_a.temperature(PERCENT) >= 40:
            brain.screen.set_cursor(5, 1)
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print('Launch A Temp:', launch_motor_a.temperature(PERCENT))
        else:
            brain.screen.set_cursor(5, 1)
            brain.screen.set_pen_color(Color.GREEN)
            brain.screen.print('Launch A Temp:', launch_motor_a.temperature(PERCENT))

        if launch_motor_b.temperature(PERCENT) >= 40:
            brain.screen.set_cursor(6, 1)
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print('Launch B Temp:', launch_motor_b.temperature(PERCENT))
        else:
            brain.screen.set_cursor(6, 1)
            brain.screen.set_pen_color(Color.GREEN)
            brain.screen.print('Launch B Temp:', launch_motor_b.temperature(PERCENT))

        if Left_motor_a.temperature(PERCENT) >= 40 or Left_motor_b.temperature(PERCENT) >= 40:
            brain.screen.set_cursor(8, 1)
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print('Left Side Overheated')
        
        if Right_motor_a.temperature(PERCENT) >= 40 or Right_motor_b.temperature(PERCENT) >= 40:
            brain.screen.set_cursor(9, 1)
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print('Right Side Overheated')

        forward_control = controller_1.axis1.position() * 0.75
        turning_control = controller_1.axis3.position()

        Left.set_velocity(forward_control + turning_control, PERCENT)
        Right.set_velocity(forward_control - turning_control, PERCENT)
        
        if controller_1.buttonY.pressing() == False and last == True:
            last = False

        if controller_1.buttonY.pressing() and last == False:
            last = True
            
            if direction == 'reverse':
                direction = 'forward'
                Left.spin(FORWARD)
                Right.spin(FORWARD)
            else:
                direction = 'reverse'
                Left.spin(REVERSE)
                Right.spin(REVERSE)

        wait(10, MSEC)

comp = Competition(user_control, autonomous)
pre_autonomous()