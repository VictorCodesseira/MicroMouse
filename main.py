from maze import Maze
from time import sleep
import random

full = Maze(1)
memory = Maze(0)

dire = [2,4,2,1,2,2,2,2,8,4,4,8,1]

for direction in dire:
    sleep(1)
    full.moveMouse(direction)
    memory.moveMouse(direction)
    x, y = full.mousePosition()
    if full.mouseValue() & 1:
        memory.addWall([x,y], 1)
    if full.mouseValue() & 2:
        memory.addWall([x,y], 2)
    if full.mouseValue() & 4:
        memory.addWall([x,y], 4)
    if full.mouseValue() & 8:
        memory.addWall([x,y], 8)

while(1):
    full.inter.update()
    memory.inter.update()
    pass


