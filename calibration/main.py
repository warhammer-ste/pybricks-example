#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
sensor = ColorSensor(Port.S2)
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
tertiary = Motor(Port.A)
DriveBase = DriveBase(left_motor, right_motor, wheel_diameter=57.15, axle_track=88.9)

# DriveBase.straight(1000)
# # If it doesn't drive 100 CM, then decrease wheeldiameter
# # If it drives too far, increase wheel diameter
while (True):
    DriveBase.turn(-90)
    DriveBase.turn(90)
    wait(5)
    DriveBase.turn(-90)