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
sensor = ColorSensor(Port.S2              )
my_left_kidney_ran_away_from_home_and_i_am_really_sad = Motor(Port.C)
right_motor = Motor(Port.B)
sacrifice = Motor(Port.A)
devil = DriveBase(my_left_kidney_ran_away_from_home_and_i_am_really_sad, right_motor, wheel_diameter=57.15, axle_track=88.9)

# This loop is for debugging. You can view the current reflection and adjust values based off it.
# You can hit center to exit debugger. In Visual Code, highlighting it and pressing Ctrl+/ will uncomment it.
ev3.speaker.beep()
print('Program start')
# while True:
#     ev3.screen.print(sensor.reflection())
#     print(sensor.reflection())
#     if Button.CENTER in ev3.buttons.pressed():
#         ev3.screen.clear()
#         break
#     else:
#         wait(100)
#         ev3.screen.clear()

one = 2
two = 3
t = 60
w = 500
a = 1

# W is wait time, T is turn radius to decide how much sensitivity is placed in the turn.
# One decides the first loop's threshold (meaning it will trigger if reflectively is less or equal to value)
# Two decides the second loop's threshold (it will only trigger if reflectively is equal to or higher than 3)
# I think I can shorten it by just stating "greater than (one)"

while True:
    print ('#1,', sensor.reflection())
    if sensor.reflection() <= one:
        t = 60
        w = 500
        devil.drive(150, 0)
        a = 1
    else:
        while sensor.reflection() >= two:
            print ('#2,', sensor.reflection())
            devil.drive(0, t)
            if sensor.reflection() <= one:
                break
            wait(w)
            devil.drive(0, -t)
            if sensor.reflection() <= one:
                break
            wait(w)
            # devil.turn(0,-t)
            # if sensor.reflection() <= one:
            #     break
            # wait(w)
            # devil.turn(0,t)
            # if sensor.reflection() <= one:
            #     break
            t = t + 10
            # w = w + 10
            # Updates values by 5 and 10 respectively. The wait gets a higher value to prevent overswing going bby a value.
            # This code likely isn't as efficient as it can be, but it functions.