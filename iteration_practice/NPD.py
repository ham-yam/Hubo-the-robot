'''
Description: This program will make robot to climb up the top of the stairs 
drop beeper, and return to starting point '''

from cs1robots import *
load_world("newspaper.wld")
hubo = Robot(beepers =1)

hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()
hubo.move()

#robot climb up one stair 
def climb_up_one_stair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    for i in range(2):
        hubo.move()
for i in range(4):
    climb_up_one_stair()

hubo.drop_beeper()

#change direction and two steps forward 
for i in range(2):
    hubo.turn_left()
for i in range(2):
    hubo.move()

#climb down one stair and two steps forward 
def climb_down_stair_two_step_forward():
    hubo.turn_left()
    hubo.move()
    turn_right()
    for i in range(2):
        hubo.move()

for i in range(3):
    climb_down_stair_two_step_forward()

#climb one stair
def climb_down_one_stair():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()

climb_down_one_stair()

#turn robot to recover the original orientation
for i in range(2):
    turn_right()
