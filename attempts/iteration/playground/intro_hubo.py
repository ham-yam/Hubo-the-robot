from cs1robots import *
create_world()
hubo = Robot()

#움직인 궤적을 남김
hubo.set_trace('black')


def step():
    for i in range(2):
        hubo.move()

    hubo.turn_left()

for i in range(4):
    step()
