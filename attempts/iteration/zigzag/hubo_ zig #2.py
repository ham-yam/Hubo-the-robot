Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from c1srobots import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from c1srobots import *
ModuleNotFoundError: No module named 'c1srobots'
>>> from cs1robots import*
>>> create_world()
>>> hubo = Robot()
>>> 
>>> def turn_right():
...     for i in range(3):
...         hubo.turn_left()
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
>>> def turn_450():
...     for i in range(5)
...     
SyntaxError: expected ':'
>>> def turn_450():
...     for i in range(5):
...         turn_right()
... 
...         
>>> turn_450
<function turn_450 at 0x000001687AEE2D40>
>>> turn_450()
>>> hubo.turn_left()
>>> hubo.turn_left()
>>> 
>>> def one_zig_loop():
...     move_9_steps()
...     turn_450()
...     move_one_step
...     turn_450()
...     move_9_steps()
...     hubo.turn_left()
...     hubo.move()
... 
...     
>>> hubo.set_trace("blue")
>>> one_zig_loop()
