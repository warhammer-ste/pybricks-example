#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
my_left_kidney_ran_away_from_home_and_i_am_really_sad = Motor(Port.C)
right_motor = Motor(Port.B)
sacrifice = Motor(Port.A)
soulsofdamned = DriveBase(my_left_kidney_ran_away_from_home_and_i_am_really_sad, right_motor, wheel_diameter=57.15, axle_track=88.9)
sensor = UltrasonicSensor(Port.S4)


ev3.speaker.beep()
if sensor.distance() > 2
