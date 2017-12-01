from maze import Maze, Mouse
from time import sleep
import random


starting_x, starting_y = 0,0
full = Maze(1, Mouse(starting_x, starting_y))
empty = Maze(0, Mouse(starting_x, starting_y))
stack = []
sleep(1)

while(empty.cellValue[empty.mouse.y][empty.mouse.x]!=0):
    sleep(0.1)
    minCell = empty.minimumCell()
    full.moveMouse(minCell)
    empty.moveMouse(minCell)

    mouse_x, mouse_y = empty.mousePosition()
    previous_walls = empty.maze[mouse_y][mouse_x]
    new_walls = full.maze[mouse_y][mouse_x]
    updated = (new_walls^previous_walls)

    updated_walls = [wall for wall in [1,2,4,8] if wall & updated != 0]

    for wall in updated_walls:
        empty.addWall([mouse_x, mouse_y], wall)

    if stack:
        stack = []
    if updated_walls:
        updated_cells = []
        for wall in updated_walls:
            if wall&1 != 0 and mouse_y>0:
                stack.append([mouse_x, mouse_y-1])
            if wall&2 != 0 and mouse_x<15:
                stack.append([mouse_x+1, mouse_y])
            if wall&4 != 0 and mouse_y<15:
                stack.append([mouse_x, mouse_y+1])
            if wall&8 != 0 and mouse_x>0:
                stack.append([mouse_x-1, mouse_y])
        stack.append([mouse_x, mouse_y])
        while stack:
            x_atual, y_atual = stack.pop()
            min_value = 300
            viz_abertos = []
            if empty.maze[y_atual][x_atual]&1 == 0:
                viz_abertos.append([x_atual, y_atual-1])
            if empty.maze[y_atual][x_atual]&2 == 0:
                viz_abertos.append([x_atual+1, y_atual])
            if empty.maze[y_atual][x_atual]&4 == 0:
                viz_abertos.append([x_atual, y_atual+1])
            if empty.maze[y_atual][x_atual]&8 == 0:
                viz_abertos.append([x_atual-1, y_atual])
            for vizinho in viz_abertos:
                value = empty.cellValue[vizinho[1]][vizinho[0]]
                if value < min_value:
                    min_value = value
            if empty.cellValue[y_atual][x_atual] != min_value + 1 and empty.cellValue[y_atual][x_atual] != 0:
                empty.updateCellValue([x_atual,y_atual], min_value+1)
                for vizinho in viz_abertos:
                    stack.append(vizinho)
    empty.update()
    full.update() # Caso a GUI não esteja sendo constantemente atualizada, os botões não funcionam


print("Chegou")
while(1):
    empty.update()
    full.update() # Caso a GUI não esteja sendo constantemente atualizada, os botões não funcionam
    sleep(1)
