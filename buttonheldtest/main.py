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

ev3.speaker.beep()
while True:
    if Button.RIGHT in ev3.buttons.pressed():
        ev3.screen.clear()
        ev3.speaker.beep()
        ev3.screen.print('Manual driving')
        print('Right button pressed--hit buttons to move robot.')
        # Print is completely useless. It's only for tracking buttons.
        cs = 100
        # CS=ColorsSpeed. I don't want to repeat-define this
        while True:
            if Button.UP in ev3.buttons.pressed():
                color.drive(-cs,0)
            elif Button.LEFT in ev3.buttons.pressed():
                color.drive(0,cs)
            else:
                color.stop()
# Since it breaks without continuing code, it automatically ends itself (due to EV3 rules)
#            if Button.LEFT in ev3.buttons.pressed():
#                color.drive(0,cs)
#            if Button.DOWN in ev3.buttons.pressed():
#                color.drive(cs,0)
#            if Button.RIGHT in ev3.buttons.pressed():
#                color.drive(0,-cs)