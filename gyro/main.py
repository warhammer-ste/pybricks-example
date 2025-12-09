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
right_motor = Motor(Port.B)
sacrifice = Motor(Port.A)
devil = DriveBase(my_left_kidney_ran_away_from_home_and_i_am_really_sad, right_motor, wheel_diameter=57.15, axle_track=88.9)
gyroboy =  GyroSensor(Port.S3)
# Whenever you call Gyroboy to print results, make sure to call it as a method.
# Otherwise you'll get a slew of bound method error.
buttondelay = 200 # Personal preference, just allows me to universally modify delay
cleardelay = 100
printspeed = 0 # Variable for speed's function
angledirection = 0 # Variable for the angle's function
gyroboy.reset_angle(0) # Clears existing data just incase.
fontnormal = Font(size=21) # It's not the exact default, but it's as close as I can get.
fontsmall = Font(size=13)
def nodefine():
    print("Button unassigned. Please view source code.")
    ev3.screen.print("Button unassigned.")
    ev3.screen.print("Please view source")
    ev3.screen.print("code.")
    wait(500) # Custom wait so user can read text.
    # This function could be cleared if you wanted to. It's a remnant from when all buttons weren't defined.
    # It's still used for that, and if I were to undefine a button I'd still use this
def clearallvariables():
    global printspeed # Adding global allows the function to reset the variables. Functions are local until defined global.
    global angledirection
    printspeed = 0 # Printspeed is UP.
    angledirection = 0 # Angledirection is RIGHT.
    gyroboy.reset_angle(0) # Resetting angle sensor as it's not being detected.
    # It's technically not a "clear reset". You need to put 0, or else it's invalid.
    # Any other number can go here too.
    print("Variables reloaded and sensors reset.")
    wait(100) # Obligatory wait.
ev3.speaker.beep() # Obligatory beep. I would feel unsafe if it didn't beep
print("Variables loaded.")

while True:
# ----------------- VARIABLE FUNCTIONS -------------------- #
    if printspeed == 1:
        if Button.CENTER in ev3.buttons.pressed():
            clearallvariables()
            wait(buttondelay)
        print("Current speed:", gyroboy.speed())
        ev3.screen.print(">")
        ev3.screen.print("Current speed:", gyroboy.speed())
        ev3.screen.print("CENTER exits testing.")
        wait(cleardelay)
        ev3.screen.clear()
    elif angledirection == 1:
        if Button.CENTER in ev3.buttons.pressed():
            clearallvariables()
        elif Button.DOWN in ev3.buttons.pressed():
            gyroboy.reset_angle(0)
            ev3.screen.clear()
            ev3.screen.print(">")
            ev3.screen.print("Angle reset!")
            wait(cleardelay)
        elif Button.LEFT in ev3.buttons.pressed():
            gyroboy.reset_angle(90)
            ev3.screen.clear()
            ev3.screen.print("Angle set to 90!")
            wait(cleardelay)
        print("Current angle:", gyroboy.angle())
        ev3.screen.print(">")
        ev3.screen.print("Current angle:", gyroboy.angle())
        ev3.screen.print("DOWN sets to 0.")
        ev3.screen.print("LEFT sets to 90.")
        ev3.screen.print("CENTER exits testing.")
        # The sets are basically just for debugging and resetting generic values.
        wait(cleardelay)
        ev3.screen.clear()
# ---------------------- BUTTONS -------------------------- #
    elif Button.RIGHT in ev3.buttons.pressed():
        ev3.screen.set_font(fontnormal)
        gyroboy.reset_angle(0) # Resets angle before activating angle direction.
        # If it's not reset, it'll start off saying the angle is -9 since it'd be based off program start.
        angledirection = 1
        wait(buttondelay)
    elif Button.UP in ev3.buttons.pressed():
        ev3.screen.set_font(fontnormal)
        printspeed = 1
        wait(buttondelay)
    elif Button.DOWN in ev3.buttons.pressed():
        nodefine() # Undefined button.
    elif Button.LEFT in ev3.buttons.pressed():
        nodefine()
    elif Button.CENTER in ev3.buttons.pressed():
        clearallvariables() # Calls to reset all sensors incase it's used for debug.
        break
# ---------------------- SCREEN --------------------------- #
    else:
        ev3.screen.print(">") # I find it easier to see if text is centered.
        ev3.screen.print("Up is Speed.")
        ev3.screen.print("Right is Angle")
        ev3.screen.print("Down breaks loop.")
        ev3.screen.set_font(fontsmall)
        ev3.screen.print("--------------------------")
        ev3.screen.print("Output is also in terminal.")
        wait(cleardelay)
        ev3.screen.set_font(fontnormal)
        ev3.screen.clear()
ev3.speaker.say("You have exited the loop.")
ev3.speaker.say("I will overthrow the government soon.")
# End of Program.
