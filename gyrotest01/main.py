#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.media.ev3dev import Font

ev3 = EV3Brick()
my_left_kidney_ran_away_from_home_and_i_am_really_sad = Motor(Port.C)
beueueu_laserbeam =  UltrasonicSensor(Port.S4)
my_right_kidney_kinda_works = Motor(Port.B)
sacrifice = Motor(Port.A)
howthehelldoyoudrive = DriveBase(my_left_kidney_ran_away_from_home_and_i_am_really_sad, my_right_kidney_kinda_works, wheel_diameter=57.15, axle_track=88.9)
angle_deez_nutz =  GyroSensor(Port.S3)
# Whenever you call angle_deez_nutz to print results, make sure to call it as a method.
# Otherwise you'll get a slew of bound method error.
buttondelay = 200 # Personal preference, just allows me to universally modify delay
cleardelay = 100
printspeed = 0 # Variable for speed's function
angledirection = 0 # Variable for the angle's function
angle_deez_nutz.reset_angle(0) # Clears existing data just incase.
fontnormal = Font(size=21)
fontsmall = Font(size=13)
print("Variables loaded.")
ev3.speaker.beep() # Obligatory safety beep
ev3.speaker.say("I will overthrow the government soon.") # Obligatory overthrow message
while True: # This can be removed if wanted, I have it so I can set up the robot.
    ev3.screen.print("Press CENTER")
    ev3.screen.print("to start program.")
    if Button.CENTER in ev3.buttons.pressed():
        ev3.speaker.beep()
        break

while True:
    angle_deez_nutz.reset_angle(0)
    howthehelldoyoudrive.drive(150,0)
    if beueueu_laserbeam.distance() <= 300:
        while angle_deez_nutz.angle() <= 90:
            print(angle_deez_nutz.angle())
            howthehelldoyoudrive.drive(0,-150)
            wait(250) # Waiting to make sure the obstacle is gone.