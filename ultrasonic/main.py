#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.media.ev3dev import Font
# By the way, in order to change your font, you NEED to import Font (above line)
# If something is in the documents and does not work, you need to import it.
# Keep imports & variables up here so they boot first.
ev3 = EV3Brick()
font = Font(size=17)
my_left_kidney_ran_away_from_home_and_i_am_really_sad = Motor(Port.C)
right_motor = Motor(Port.B)
sacrifice = Motor(Port.A)
soulsofdamned = DriveBase(my_left_kidney_ran_away_from_home_and_i_am_really_sad, right_motor, wheel_diameter=57.15, axle_track=88.9)
sensor = UltrasonicSensor(Port.S4)
# Here, UltraSonicSensor is defined by its port as usual. However, it uses the sensor (#) ports.
# To define a sensor port, you have to put an S before the port as seen here. It will not function without an S.
# Outside of that, it can be defined and used as you would Drivebase & EV3
lah = sensor.distance(silent=False)
# Defines sensor distance so I don't have to type this fat string
cah = 150
# Cah is the speed for reversal.
letswait = 500
# letswait is used for the button statements. It makes it easier to modify all the wait times.
keh = 50
# Value to minus cah by
zero = 50
thous = 950
# 0 and 1000 are given variables in order to be used for if/else statements.
# A raw number will render these statements an invalid syntax.
cah = cah + keh
# Having code with this many variables ends up giving it a longer time to boot.
# Having a start-up noise (like the beep below, and 'spoken' text helps you be aware of when your robot has actually started.
# Similar to a boot up sequence. EV3's hardware isn't meant to run fifty lines of code.

ev3.screen.set_font(font)
ev3.speaker.beep()
ev3.speaker.say('View the screen.')
ev3.screen.print('Configuration will')
ev3.screen.print('show next. Please')
ev3.screen.print('press CENTER to')
ev3.screen.print('OK any prompt.')
while True:
    if Button.CENTER in ev3.buttons.pressed():
        ev3.speaker.beep()
# All beeps are unnecessary. They sound satisfying to play when button is pressed though
        break
    else:
        wait(0.1)
ev3.screen.clear()
ev3.screen.print('Loading..')
wait(1000)
ev3.screen.clear()
sent='Input or Sensor?'
ev3.screen.print(sent)
ev3.screen.print('Manual ][ Auto')
while True:
    if Button.LEFT in ev3.buttons.pressed():
        ev3.screen.clear()
        ev3.screen.print(sent)
        ev3.screen.print('<Manual> ][ Auto')
        loh = cah
    if Button.RIGHT in ev3.buttons.pressed():
        ev3.screen.clear()
        ev3.screen.print(sent)
        ev3.screen.print('Manual ][ <Auto>')
        loh = lah
    if Button.CENTER in ev3.buttons.pressed():
        ev3.screen.clear
        ev3.screen.print('After hitting CENTER, the')
        ev3.screen.print('program will start.')
        break
while True:
    if Button.CENTER in ev3.buttons.pressed():
        break
ev3.screen.clear()
ev3.screen.print('Loading..')
wait(1000)
while loh == cah:
    ev3.screen.print('How fast should the')
    ev3.screen.print('robot go in reverse?')
    ev3.screen.print('Current speed(mm):')
    sacrifice.run(-cah)
    # The default is 500, so it should display 500 first. Also tells user that its in mm
    ev3.screen.print(cah)
    if Button.UP in ev3.buttons.pressed():
        ev3.speaker.beep()
        cah = cah + keh
        # Adds to cah whenever UP is pressed, and updates the variable accordingly
        ev3.screen.clear()
        ev3.screen.print('Updating..')
        wait(letswait)
        # Wait exists to prevent button spam. Otherwise, you would accidentally do several button presses.
    elif Button.DOWN in ev3.buttons.pressed():
        ev3.speaker.beep()
        cah = cah - keh
        # Removes from cah whenever DOWN is pressed, and updates the variable accordingly
        ev3.screen.clear()
        ev3.screen.print('Updating..')
        wait(letswait)
    elif Button.LEFT in ev3.buttons.pressed():
        ev3.screen.print('Decreasing amount..')
        if keh < zero:
            ev3.screen.clear()
            ev3.screen.print('Value is negative')
            ev3.screen.print('Cannot go lower.')
            wait(letswait)
            ev3.screen.clear()
        else:
            ev3.speaker.beep()
            keh = keh - 50
            ev3.screen.clear()
            ev3.screen.print('Updating..')
            ev3.screen.print(keh)
            wait(letswait)
    elif Button.CENTER in ev3.buttons.pressed():
        sacrifice.stop()
        ev3.speaker.beep()
        ev3.screen.print('Settings confirmed.')
        wait(500)
        ev3.speaker.beep()
        # Adds a wait delay for human to read the text & prepare
        break
    elif Button.RIGHT in ev3.buttons.pressed():
        ev3.screen.print('Increasing amount..')
        if keh > thous:
            ev3.screen.clear()
            ev3.screen.print('Value is too high')
            ev3.screen.print('Cannot go higher.')
            wait(letswait)
            ev3.screen.clear()
        else:
            ev3.speaker.beep()
            keh = keh + 50
            ev3.screen.clear()
            ev3.screen.print('Updating..')
            ev3.screen.print(keh)
            wait(letswait)
    else:
        wait(10)
        ev3.screen.clear()
ev3.speaker.beep()
ev3.screen.print('Program starting.')
wait(1500)
ev3.screen.clear()
# Clears the screen to remove junk.
while True:
    if sensor.distance() >= 300:
        #sacrifice.run(lah)
        soulsofdamned.straight(lah)
        continue
    elif sensor.distance() <= 100:
        #sacrifice.run(-cah)
        soulsofdamned.straight(-loh)
        continue
        # Loh is defined by whatever it was set to earlier.
        # If it was set to Cah, then value based on set speed.
        # If it's Lah, then it's based on distance.
    else:
        #sacrifice.stop()
        soulsofdamned.stop()
        # Gives the robot something to do if values are between 150-250 mm