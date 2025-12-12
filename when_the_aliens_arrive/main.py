#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import (TemperatureSensor) # This line is necessary for NXT devices.
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


ev3 = EV3Brick()
left_thing_that_runs = Motor(Port.C)
right_motor = Motor(Port.B)
sacrifice = Motor(Port.A) # Third evil motor that does usually nothing
creek4win = DriveBase(left_thing_that_runs, right_motor, wheel_diameter=57.15, axle_track=88.9)
theProbe = TemperatureSensor(Port.S1)
tempies = theProbe.temperature()
def printtempies():
    ev3.screen.print(theProbe.temperature())
    wait(200)
    ev3.screen.clear()


while True:
    printtempies()
    if tempies <= 10:
        ev3.speaker.say("Cold!")
        ev3.screen.print("Cold!")
        printtempies()
    elif tempies >= 30
        ev3.speaker.say("Warm!")
        ev3.screen.print("Warm!")
        printtempies()