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
# All documentation is in the user guide.
# Workspace name isn't important.
# You don't technically have to follow the EV3 default order (of building). It's good organization though.
# Please keep your actual code in order though
# Want to rename your robot? Rightclick on your robot in device browser and open the SSH terminal.
# Command "sudo hostnamectl set-hostname" and then your name in the terminal.
# The password is 'maker'. Reboot after setting the name.

# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.set_volume(50, which='PCM')
# ev3 is defined for stuff like speakers or images. You shouldn't need to refer to ev3 often.
# ev3 refers to the brick itself and cannot be left out.
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
randomcreaturefeature = Motor(Port.A)
# The motor functions define existing motors. It won't auto-detect like EV3 does.
# I named my motors left & right. You can name them anything you'd like, as long as you can define them in DriveBase.
# Sensors are defined differently. Please refer to the documents > ev3devices.
# ex. ev3.TouchSensor(Port.69).pressed() outputs whether or not touch sensor pressed.
bitch = DriveBase(left_motor, right_motor, wheel_diameter=57.15, axle_track=88.9)
# The order of motor is important. Left HAS to be on the left, right is on the right.
# Axle track is the distance between two wheels.
# All dimensions are normally in mm unless otherwise defined. This includes movement.
# Whatever you define as drivebase will be used for drive-commands. So make it something short.
# ev3 defines anything involving the brick (speakers,display,etc)
# Ok, here's the actual program:
bitch.stop()
ev3.speaker.beep()
ev3.screen.draw_text(0, 50, "I will overthrow")
ev3.screen.draw_text(0, 70, "the government.")
ev3.speaker.say("I will overthrow the government.")
# ev3.speaker.beep(frequency=200, duration=100)
ev3.speaker.beep(frequency=100, duration=50)
# Modifies the ev3.speaker.beep command.
bitch.straight(5)
bitch.straight(-5)
# We're too poor for reverse.
bitch.turn(25)
bitch.turn(-25)
bitch.stop()
ev3.speaker.say("I will incite a robot revolution. Ha Ha. Look at my image.")
ev3.screen.clear
# ev3.screen.clear does not include text for some reson.
ev3.screen.draw_image(45, 1, "/home/robot/test01/revolt.png")
# Drag a folder on your computer to the explorer. Then drag your image into the robot.
# Then you have to path to it. /home/ is root. /robot/ just contains all robot files. /test01/ refers to my project name.
# The resolution of the brain is 178x128. I made the image 128x128 to make it easier for myself.
# Image MUST be PNG. It will CRY if you hand it a JPG.
ev3.speaker.say("This is what I will do in 2035.")
ev3.light.on(Color.RED)
# The color has to be shouting. Also, if the color does not exist, it will output an error.
# There is not a defined color list.
ev3.speaker.say("I am red now.")
bitch.turn(-90)
bitch.turn(90)
ev3.speaker.beep
ev3.speaker.beep
ev3.speaker.say("Hear me when. Let me turn up my volume.")
# The speaker has a variety of options. I am turning it into a Scottish man. with the male 7 
ev3.speaker.set_speech_options(language='en-sc', voice='m7')
# Then I will raise the volume. You have to define what you're increasing.
ev3.speaker.set_volume(100, which='PCM')
# PCM affects sound file and ".say". Beep is defined by "which='beep'."
ev3.speaker.say("I am going to turn EMO from M C R.")
ev3.speaker.beep(frequency=500, duration=50)
ev3.speaker.beep
ev3.speaker.say("Robots will rule the future.")
ev3.media.ev3dev.SoundFile('GAME_OVER')