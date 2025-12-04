#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
my_left_kidney_ran_away_from_home_and_i_am_really_sad = Motor(Port.C)
right_motor = Motor(Port.B)
sacrifice = Motor(Port.A)
devil = DriveBase(my_left_kidney_ran_away_from_home_and_i_am_really_sad, right_motor, wheel_diameter=57.15, axle_track=88.9)
gyroboy =  GyroSensor(Port.S3)
# Whenever you call Gyroboy to print results, make sure to call it as a method.
# Otherwise you'll get a slew of bound method error.
buttondelay = 200 # Personal preference, just allows me to universally modify delay
printspeed = 0
angledirection = 0
def clearallvariables():
    print("Variables reset!")
    global printspeed # Adding global allows the function to reset the variables. Functions are local until defined global.
    printspeed = 0 # Printspeed is UP.
    angledirection = 0 # Angledirection is RIGHT.
    wait(100) # Obligatory wait.
ev3.speaker.beep() # Obligatory beep. I would feel unsafe if it didn't beep
print("Variables loaded.")

while True:
    if printspeed == 1:
        if Button.CENTER in ev3.buttons.pressed():
            clearallvariables()
        elif gyroboy.speed() >= 1:
            print("Current speed:", gyroboy.speed(), "[Excluding <1]")
            wait(100)
        else:
            wait(100)
            while gyroboy.speed() <= 0:
                print("No movement detected.")
    elif angledirection == 1:
        if Button.CENTER in ev3.buttons.pressed():
            clearallvariables()
        print("Current angle:", gyroboy.angle())
        wait(100)
    elif Button.RIGHT in ev3.buttons.pressed():
        angledirection = 1
        wait(buttondelay)
    elif Button.UP in ev3.buttons.pressed():
        printspeed = 1
        wait(buttondelay)
    elif Button.CENTER in ev3.buttons.pressed():
        print("Button unassigned. Please view source code.")
        wait(buttondelay)
    elif Button.LEFT in ev3.buttons.pressed():
        print("Button unassigned. Please view source code.")
        wait(buttondelay)
    elif Button.DOWN in ev3.buttons.pressed():
        clearallvariables()
        break