from maze import Maze, Mouse
from time import sleep
from floodfill import *

def main():
    real = Maze(1)
    memory = Maze(0,1)
    sleep(1)
    floodFill(memory, real)
    sleep(1)
    memory.setMouse([0,15])
    sleep(2)
    fastRun(memory)




    while(1):
        memory.update()
        real.update() # Caso a GUI não esteja sendo constantemente atualizada, os botões não funcionam
        sleep(0.01)

main()
