from cs1robots import *
create_world()
hubo = Robot()

def turn_right():
    for i in range(3):
        hubo.turn_left()

        
def turn_450():
    for i in range(5):
        turn_right()

        
def turn_180():
     for i in range(2):
         turn_right()
... 
...         
>>> def turn_360():
...     for i in range(3):
...         turn_right()
... 
...         
>>> def move_one_step():
...     hubo.move()
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
>>> hubo.set_trace("blue")
>>> hubo.set_trace("blue")
>>> hubo.turn_left()
>>> zig()
>>> zig()
>>> zig()
>>> zig()
zig()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    zig()
  File "<pyshell#40>", line 4, in zig
    hubo.move()
  File "C:\Users\USER\AppData\Local\Programs\Python\Python311\Lib\site-packages\sit22001-0.2.3-py3.11.egg\cs1robots.py", line 444, in move
    raise RobotError("That move really hurt!\n Please, make sure that " +
cs1robots.RobotError: That move really hurt!
 Please, make sure that there is no wall in front of me!
