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
roomtemp = 20
mewanttempies = 0
# def printtempies():
#     print("tempies", theProbe.temperature())
#     ev3.screen.print(theProbe.temperature())
#     wait(200)
#     ev3.screen.clear()
def eviltempies():
    evilfuckingtempies = round(theProbe.temperature()) # Default value for referencing temp
    eviltempies = evilfuckingtempies - roomtemp # Value to reference temp changed by roomtemp
    print("eviltempies", evilfuckingtempies)
    ev3.screen.print(evilfuckingtempies)
    wait(200)
    ev3.screen.clear()
while True:
    ev3.screen.print("Room temp = Avg") # Alternatively; "Set room temp the same as the average temperature"
    # Center exits the program. The screen won't fit the text to state this without decreasing font.
    ev3.screen.print("RoomTemp", roomtemp, "°C")
    ev3.screen.print("Left -][Right +")
    if Button.CENTER in ev3.buttons.pressed():
        break
    elif Button.LEFT in ev3.buttons.pressed():
        roomtemp = roomtemp - 1
        wait(200)
    elif Button.RIGHT in ev3.buttons.pressed():
        roomtemp = roomtemp + 1
        wait(200)
    # elif Button.UP in ev3.buttons.pressed():
    #     mewanttempies = 1
    #     wait(200)
    # elif Button.DOWN in ev3.buttons.pressed():
    #     mewanttempies = 0
    #     wait(200)
    # elif mewanttempies == 1:
    #     printtempies()
    #     wait(200)
    elif mewanttempies == 0:
        eviltempies()
evilfuckingtempies() # Runs to define evilfuckingtempies if not ran already
# while True:
#     printtempies()
#     if tempies <= 10:
#         print("#2")
#         ev3.speaker.say("Cold!")
#         ev3.screen.print("Cold!")
#         printtempies()
#     elif tempies >= 30:
#         print("#2")
#         ev3.speaker.say("Hands off.")
#         ev3.screen.print("Warm!")
#         printtempies()
