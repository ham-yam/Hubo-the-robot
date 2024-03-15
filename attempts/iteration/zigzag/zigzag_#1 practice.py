Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from cs1robots import *
>>> create_world()
>>> hubo.Robot()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    hubo.Robot()
NameError: name 'hubo' is not defined
>>> hubo = Robot()
>>> def turn_right():
...     hubo.turn_left()
...     hubo.turn_left()
...     hubo.turn_left()
... 
>>> for i in range(3):
...     turn_right()
... 
>>> hubo.set_trace("blue")
>>> for i in range(9):
...     hubo.move()
... 
>>> turn_right
<function turn_right at 0x000002CA78D0D580>
>>> turn_right()
>>> hubo.move()
>>> 
>>> for i in range(5):
...     turn_right()
... 
>>> for i in range(9):
...     hubo.move()
... 
...     
>>> hubo.turn_left()
>>> hubo.move()
>>> hubo.turn_left()
>>> for i in range(9):
...     hubo.move()
... 
for i in range(3):
    turn_right()

    
for i in range(2):
    turn_right()

    
hubo.move()
def turn_180():
    for i in range(4):
        turn_right()

turn_180
<function turn_180 at 0x000002CA78D0D3A0>
turn_180()
def turn_180()
SyntaxError: expected ':'
def turn_180():
    for i in range(2):
        turn_right()
turn_180
SyntaxError: invalid syntax
turn_180()

turn_right
<function turn_right at 0x000002CA78D0D580>
turn_right()
for i in range(9):
    hubo.move()

hubo.turn_left()
hubo.move()
hubo.turn_left()
for i in range(9):
    hubo.move()

    
for i in range(5):
    turn_right()

hubo.move()
def turn_270():
    for i in range(5):
        turn_right()
turn_270()
SyntaxError: invalid syntax
turn_270()
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    turn_270()
NameError: name 'turn_270' is not defined. Did you mean: 'turn_180'?
def turn_270():
    for i in range(5):
        turn_right()

        
turn_270()
def move_one_step():
    hubo.move()

    
def move_9_steps():
    for i in range(9):
        hubo.move()

move_9_steps()
hubo.turn_left()
move_one_step()
hubo.turn_left()
move_9_steps()
turn_270()
move_one_step()
turn_270()
move_9_steps()
hubo.turn_left()
move_one_step()
hubo.turn_left()
move_9_steps()
turn_270()
move_one_step()
turn_270()
move_9_steps
<function move_9_steps at 0x000002CA78DFEFC0>
move_9_steps()
