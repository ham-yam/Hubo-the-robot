'''
Description: This program will make robot to move
entire world in zig and aigzag style
'''
from cs1robots import *
create_world()
hubo = Robot()

hubo.set_trace('blue')

def turn_right():
    for i in range(3):
        hubo.turn_left()

def move_9_steps():
    for i in range(9):
        hubo.move()

#move two rows in zigzag style
def zigzag():
    move_9_steps()
    turn_right()
    hubo.move()
    turn_right()
    move_9_steps()

#move two rows in zigzag style and change direction
def zig():
    zigzag()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()

#hubo visiting the entire world in zig and zigzag style
hubo.turn_left()

for i in range(4):
    zig()
zigzag()

#turn robot to recover the original orientation
hubo.turn_left()

