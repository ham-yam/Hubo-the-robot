'''
Description: This program will make robot to follow path,
pick up beeper at the grid point and get back to the starting grid point
and recover the orientation'''

from cs1robots import *
load_world("hurdles1.wld")
hubo = Robot()
hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

#jump one hurdle    
def one_hurdle():
    hubo.turn_left()
    for i in range(2):
        hubo.move()
        turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    
def step_hurdle():
    hubo.move()
    one_hurdle()
   
#skip one hurdle and pick up beeper
step_hurdle()
for i in range(3):
    one_hurdle()

hubo.pick_beeper()

#jump one hurdle back to the starting point
def one_hurdle_return():
    turn_right()
    for i in range(2):
        hubo.move()
        hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    
#move one step and jump one hurdle backward to the starting point
def step_hurdle_return():
    hubo.move()
    one_hurdle_return()

#recover the original orientation
for i in range(2):
    hubo.turn_left()
step_hurdle_return()
for i in range(3):
    one_hurdle_return()

#turn robot to recover the original orientation
for i in range(2):
    hubo.turn_left()
