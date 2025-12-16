#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import (TemperatureSensor, SoundSensor, EnergyMeter, VernierAdapter) # This line is necessary for NXT devices
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
def evilasstempies():
    eviltempies = round(theProbe.temperature()) # Default value for referencing temp
    print("eviltempies", eviltempies)
    ev3.screen.print(eviltempies)
    wait(200)
    ev3.screen.clear()
def wiper():
    eviltempies = round(theProbe.temperature())
    ev3.screen.print(eviltempies)
    wait(200)
    ev3.screen.clear()

ev3.speaker.beep()
sacrificespeed = 500

while True:
    eviltempies = round(theProbe.temperature())
    ev3.light.on(Color.GREEN)
    if eviltempies <= 15:
        ev3.light.on(Color.YELLOW)
        sacrifice.run(sacrificespeed)
        print(eviltempies, "Cold")
        ev3.screen.print("Cold!")
        ev3.speaker.say("Cold")
        wiper()
    elif eviltempies >= 25:
        ev3.light.on(Color.RED)
        sacrifice.run(-sacrificespeed)
        print(eviltempies, "Warm")
        ev3.screen.print("Warm!")
        ev3.speaker.say("Warm")
        wiper()
    else:
        sacrifice.stop()
        evilasstempies()
