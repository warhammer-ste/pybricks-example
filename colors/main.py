#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
color = DriveBase(left_motor, right_motor, wheel_diameter=57.15, axle_track=88.9)
pause=1000
# wait is in MS
# I made a function because I didn't wanna change all the waits. I am very lazy.

# Write your program here.
while True:
    ev3.light.on(Color.RED)
    wait(pause)
    ev3.light.on(Color.ORANGE)
    wait(pause)
    ev3.light.on(Color.GREEN)
    wait(pause)
    ev3.light.on(Color.YELLOW)
    wait(pause)
ev3.speaker.beep
# I was trying to do R,B,G but Blue is apparently invalid! It doesn't display any color