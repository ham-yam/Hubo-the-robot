Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from cs1robots import *
>>> create_world()
>>> hubo = Robot()
>>> def turn_right():
...     for i in range(3):
...         hubo.turn_left()
... 
...         
>>> def move_9_steps():
...     for i in range(9):
...         hubo.move()
... 
...         
>>> def zigzag():
...     move_9_steps()
...     turn_right()
...     hubo.move()
...     turn_right()
...     move_9_steps()
... 
...     
>>> def zig():
...     zigzag()
...     hubo.turn_left()
...     hubo.move()
...     hubo.turn_left()
... 
...     
>>> hubo.set_trace('blue')
>>> hubo.turn_left()
>>> for i in range(4):
...     zig()
... 
...     
>>> zigzag()
