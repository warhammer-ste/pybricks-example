#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import (TemperatureSensor, SoundSensor, EnergyMeter, VernierAdapter)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.media.ev3dev import Font

ev3 = EV3Brick()
left_thing_that_runs = Motor(Port.C)
right_motor = Motor(Port.B)
sacrifice = Motor(Port.A) # Third evil motor that does usually nothing
creek4win = DriveBase(left_thing_that_runs, right_motor, wheel_diameter=57.15, axle_track=88.9)

# This file entirely exists because the presets stay the same basically all the time.
# It has most of my preferred imports and it contains definitions. Please feel free to remove and edit things as you need.
