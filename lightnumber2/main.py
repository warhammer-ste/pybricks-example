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

ev3 = EV3Brick()
ultrasonic =  UltrasonicSensor(Port.S4)
sensor = ColorSensor(Port.S2)
my_left_kidney_ran_away_from_home_and_i_am_really_sad = Motor(Port.C)
right_motor = Motor(Port.B)
sacrifice = Motor(Port.A)
devil = DriveBase(my_left_kidney_ran_away_from_home_and_i_am_really_sad, right_motor, wheel_diameter=57.15, axle_track=88.9)
one = 2
t = 60
w = 1000
noturning = 0

# This loop is for debugging. You can view the current reflection and adjust values based off it.
# You can hit center to exit debugger. In Visual Code, highlighting it and pressing Ctrl+/ will uncomment it.
ev3.speaker.beep()
print('Program start')
devil.reset()
while True:
    while noturning == 0:
        print ('#1,', sensor.reflection())
        if ultrasonic.distance() <= 300:
            noturning = 1
        elif sensor.reflection() <= one:
            devil.drive(150, 0)
            t = 60
            w = 1000
        elif sensor.reflection() == 0:
            devil.drive(0, 120)
            print("No line nor paper detected.")
        else:
            while sensor.reflection() > one:
                print ('#2,', sensor.reflection())
                devil.drive(0, t)
                print("positive turn")
                if sensor.reflection() == one:
                    break
                wait(w)
                devil.drive(0, -t)
                print("negative turn")
                if sensor.reflection() == one:
                    break
                wait(w)
                devil.drive(0, -t)
                if sensor.reflection() == one:
                    break
                wait(w)
                devil.drive(0, t)
                if sensor.reflection() == one:
                    break
                wait(w)
                devil.drive(0, -t)
                if sensor.reflection() == one:
                    break
                t = t + 10
                if t <= 90:
                    w = w + 10
                elif t >= 120:
                    w = w + 25
                # If the turn amount is still under 120 per turn, it only adds a wait amount of 10(ms)
                # Once it goes above 120, it starts adding 25(ms) as a result of the wider turns. The wider turns make it harder for the sensor to update fast enough.
    while noturning == 1:
        devil.straight(-10)
        devil.turn(240)
        wait(500)
        noturning = 0