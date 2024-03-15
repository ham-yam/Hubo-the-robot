#I need to load this from hurdle1_set  +  add function, beeper
#
#background setup
from cs1robots import*
create_world()
hubo = Robot()

def turn_right():
    for i in range(3):
        hubo.turn_left()
    
def one_hurdle():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    
def step_hurdle():
    hubo.move()
    one_hurdle()
   
hubo.set_trace('blue')

#hubo moving to pick up beeper
step_hurdle()
for i in range(3):
    one_hurdle()

#pick up beeper
#hubo.pick_up_beeper()

#returing to spawn point
def one_hurdle_return():
    turn_right()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()

def step_hurdle_return():
    hubo.move()
    one_hurdle_return()


hubo.turn_left()
hubo.turn_left()
step_hurdle_return()
for i in range(3):
    one_hurdle_return()
