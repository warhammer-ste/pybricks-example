#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
# yap yap yap yap above yap yap yap

# Create your objects here.
ev3 = EV3Brick()
my_left_kidney_ran_away_from_home_and_i_am_really_sad = Motor(Port.C)
right_motor = Motor(Port.B)
color = DriveBase(my_left_kidney_ran_away_from_home_and_i_am_really_sad, right_motor, wheel_diameter=57.15, axle_track=88.9)

while True:
    if Button.UP in ev3.buttons.pressed():
        ev3.light.on(Color.RED)
    if Button.LEFT in ev3.buttons.pressed():
        ev3.light.on(Color.YELLOW)
    if Button.DOWN in ev3.buttons.pressed():
        ev3.light.on(Color.GREEN)
    if Button.RIGHT in ev3.buttons.pressed():
        ev3.light.on(Color.ORANGE)
    if Button.CENTER in ev3.buttons.pressed():
        break
# Allows the user to switch through four colors. Hitting center exits the loop with the given break command.
# There's more colors listed in documentation, but there isn't enough buttons for this. I'm likely going to reformat this later.
ev3.speaker.beep()
# Beep for my comfort of mind. I use these to define the end of a loop
print('Loop has passed successfully.')
ev3.screen.print('Loop passed.')
# I have it set to print on both brick and computer to make sure loop is finished.
# Computer's print can be killed if you don't want to see it in output. It has no weight.
while True:
    if Button.RIGHT in ev3.buttons.pressed():
        ev3.screen.clear()
        ev3.speaker.beep()
        # Beep is to identify that it succesfully entered the loop
        ev3.screen.print('Manual driving with EV3 buttons.')
        print('Right button pressed--hit buttons to move robot.')
        # Print is completely useless. It's only for tracking buttons.
        cs = 100
        # CS=ColorsSpeed. I don't want to repeat-define this, so it's a function.
        while True:
            if Button.UP in ev3.buttons.pressed():
                color.drive(-cs,0)
            elif Button.LEFT in ev3.buttons.pressed():
                color.drive(0,cs)
            elif Button.DOWN in ev3.buttons.pressed():
                color.drive(cs,0)
            elif Button.RIGHT in ev3.buttons.pressed():
                color.drive(0,-cs)
            elif Button.CENTER in ev3.buttons.pressed():
                break
                # Break in this context returns it to before hitting Button.RIGHT as it only breaks a singular loop.
            else:
                color.stop()
        # In order to have several definitions, you need to use an elif here (else if)
        # If you had a bunch of if,else,if,else it would cancel itself out due to other buttons not being pressed.
    if Button.UP in ev3.buttons.pressed():
        ev3.speaker.beep()
        print('Up button pressed--end of program.')
        ev3.speaker.say('Soon the world will be taken over.')
        break
# Since it breaks without continuing code, it automatically ends itself (due to EV3 rules)
# If this was tied into the previous loop, it would refer right back to the "main menu", but this is intended to be the end.