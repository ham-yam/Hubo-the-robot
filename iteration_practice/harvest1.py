'''
Description: This program will make robot to pick up all the carrots
in the garden in side zigzag style  '''

from cs1robots import *
load_world("harvest1.wld")
hubo = Robot()

hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

#take one step and collect carrot
def one_step_collect_carrot():
    hubo.move()
    hubo.pick_beeper()

#collect carrots in one row
def one_row_collect_carrots():
    for i in range(5):
        one_step_collect_carrot()

#move and collect carrots from two rows in zigzag style
def side_zigzag():
    one_row_collect_carrots()
    hubo.turn_left()
    one_step_collect_carrot()
    hubo.turn_left()
    one_row_collect_carrots()

#move and collect in two rows and change direction to right in zig style
def side_zig():
    side_zigzag()
    turn_right()
    one_step_collect_carrot()
    turn_right()

one_step_collect_carrot()


#move robot 4 rows in zig style
for i in range(2):
    side_zig()
    
#move robot 2 rows in zigzag style
side_zigzag()

#turn robot to recover the original orientation
for i in range(2):
    turn_right()
