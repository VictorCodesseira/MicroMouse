from maze import Maze
from time import sleep

while(1):
    a = Maze(1)
    sleep(2)
    a.addWall([0,0],2)
    sleep(2)
    a.moveMouse(4)
    sleep(10)
