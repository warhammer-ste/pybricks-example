#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.nxtdevices import (TemperatureSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.media.ev3dev import Font

ev3 = EV3Brick()
# left_thing_that_runs = Motor(Port.C)
# right_motor = Motor(Port.B)
# creek4win = DriveBase(left_thing_that_runs, right_motor, wheel_diameter=57.15, axle_track=88.9)
sacrifice = Motor(Port.A) # Third evil motor that does usually nothing
theProbe = TemperatureSensor(Port.S1)
LARGER_LARGER = Font(size=300)
shortpeoplekilledmyfamily = Font(size=12)
SuperEvilHot = 0
MyBallsAreFreezing = 0
def evilasstempies():
    eviltempies = round(theProbe.temperature()) # Default value for referencing temp
    if Button.DOWN in ev3.buttons.pressed():
        print("-------^OLD^------")
        print("evil tempies", eviltempies)
        print("------------------")
        print(theProbe.temperature(), "Real Temp")
    ev3.screen.print(eviltempies)
    wait(200)
    ev3.screen.clear()
def wiper():
    global eviltempies
    eviltempies = round(theProbe.temperature())
    ev3.screen.print(eviltempies, "Celsius")
    wait(200)
    ev3.screen.clear()
def cold():
    ev3.light.on(Color.YELLOW)
    sacrifice.run(sacrificespeed)
    ev3.screen.print("Cold!")
    if Button.DOWN in ev3.buttons.pressed():
        print("-------^OLD^------")
        print(eviltempies, "Cold")
        print("------------------")
        print(theProbe.temperature(), "Real Temp")
def hot():
    ev3.light.on(Color.RED)
    sacrifice.run(-sacrificespeed)
    ev3.screen.print("Warm!")
    if Button.DOWN in ev3.buttons.pressed():
        print("-------^OLD^------")
        print(eviltempies, "Warm")
        print("------------------")
        print(theProbe.temperature(), "Real Temp")
def gabagagagoo():
    global SuperEvilHot
    global MyBallsAreFreezing
    ev3.screen.set_font(LARGER_LARGER)
    SuperEvilHot = 0
    MyBallsAreFreezing = 0
def villainousdebugtext():
    ev3.screen.set_font(shortpeoplekilledmyfamily)
    ev3.screen.print("DEBUG RUN. RESULTS FAKE.")
    ev3.screen.print("CENTER TO EXIT.")
    ev3.screen.set_font(LARGER_LARGER)

sacrificespeed = 150
ev3.screen.set_font(LARGER_LARGER)
ev3.speaker.beep()
# You can hit down button regardless of temperature action to view current temp, evil or not.
# Center exits out of any debug prompt
# Left is cold prompt.
# Right is warm prompt.
# Hold buttons, it usually doesnt instantly register presses unfortunately

while True:
    ev3.light.on(Color.GREEN)
    eviltempies = round(theProbe.temperature())
    if Button.CENTER in ev3.buttons.pressed():
        gabagagagoo()
    elif Button.RIGHT in ev3.buttons.pressed():
        MyBallsAreFreezing = 0
        # Above resets other variable so it doesn't dupe.
        SuperEvilHot = 1
    elif Button.LEFT in ev3.buttons.pressed():
        SuperEvilHot = 0
        # Above resets other variable so it doesn't dupe.
        MyBallsAreFreezing = 1
    elif SuperEvilHot == 1:
        hot()
        villainousdebugtext()
        wiper()
    elif MyBallsAreFreezing == 1:
        cold()
        villainousdebugtext()
        wiper()
    elif eviltempies <= 15:
        cold()
        wiper()
    elif eviltempies >= 25:
        hot()
        wiper()
    else:
        sacrifice.stop()
        ev3.screen.print("Room Tempies")
        evilasstempies()
