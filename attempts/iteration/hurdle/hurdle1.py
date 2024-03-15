Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from cs1robot import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from cs1robot import *
ModuleNotFoundError: No module named 'cs1robot'
from cs1robots import *
create_world()
hubo = Robot()
hubo.set_trace("green")
def turn_right():
    for i in range(3):
        turn_left()

        
hubo.move()
hubo.turn_left()
humo.move()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    humo.move()
NameError: name 'humo' is not defined. Did you mean: 'hubo'?
hubo.move()
turn_right()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    turn_right()
  File "<pyshell#8>", line 3, in turn_right
    turn_left()
NameError: name 'turn_left' is not defined
>>> def turn_right():
...     for i in range(3):
...         hubo.turn_left()
... 
...         
>>> turn_right()
>>> hubo.move()
>>> turn_right()
>>> hubo.move()
>>> hubo.turn_left()
>>> def one():
...     hubo.move()
...     hubo.turn_left()
...     hubo.move()
...     turn_right()
...     hubo.move()
...     turn_right()
...     hubo.move()
...     hubo.turn_left()
... 
...     
>>> one()
>>> one()
>>> one()
>>> one()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    one()
  File "<pyshell#32>", line 6, in one
    hubo.move()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python311\Lib\site-packages\sit22001-0.2.3-py3.11.egg\cs1robots.py", line 444, in move
    raise RobotError("That move really hurt!\n Please, make sure that " +
cs1robots.RobotError: That move really hurt!
 Please, make sure that there is no wall in front of me!
