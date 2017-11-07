from maze import Maze
from time import sleep
import random
a = Maze(1)
sleep(1)
a.addWall([9,7], 1)
sleep(1)
a.addWall([9,7], 2)
sleep(1)
a.addWall([9,7], 4)
sleep(1)
a.addWall([9,7], 8)
sleep(1)

while(1):
    a.moveMouse(random.choice([1,2,4,8]))
    sleep(0.1)
