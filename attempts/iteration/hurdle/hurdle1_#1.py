Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#setup
from cs1robots import *
create_world()
>>> hubo = Robot()
>>> def turn_right():
...     for i in range(3):
...         hubo.turn_left()
... 
...         
>>> hubo.set_trace('blue')
>>> hubo.move()
>>> hubo.turn_left()
>>> hubo.move()
... 
>>> turn_right()
>>> hubo.move()
>>> turn_right()
... hubo.move()
... 
SyntaxError: multiple statements found while compiling a single statement
>>> turn_right()
>>> hubo.move()
>>> hubo.turn_left()
>>> hubo.move()
>>> def one_hurdle():
...     hubo.move()
...     hubo.turn_left()
...     hubo.move()
...     turn_right()
...     hubo.move()
...     turn_right()
...     hubo.move()
...     hubo.turn_left()
...     hubo.move()
... 
...     
>>> one_hurdle()
>>> one_hurdle()
>>> 
...  
