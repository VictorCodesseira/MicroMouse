def stack_Iter(init_stack, empty):
    if not init_stack:
        return
    stack = []
    for x in init_stack:
        stack.append(x)
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
    stack = []
    for x in init_stack:
        stack.append(x)
    while stack:
        x_atual, y_atual = stack.pop()
        ret_min_value = 300
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
            ret_value = empty.returnCellValue[vizinho[1]][vizinho[0]]
            if ret_value < ret_min_value:
                ret_min_value = ret_value
        if empty.returnCellValue[y_atual][x_atual] != ret_min_value + 1 and empty.returnCellValue[y_atual][x_atual] != 0:
            empty.returnCellValue[y_atual][x_atual] = ret_min_value+1
            for vizinho in viz_abertos:
                stack.append(vizinho)

def registerWalls(maze, previous_walls, new_walls, mouse_x, mouse_y):

    updated = (new_walls^previous_walls)

    updated_walls = [wall for wall in [1,2,4,8] if wall & updated != 0]

    for wall in updated_walls:
        maze.addWall([mouse_x, mouse_y], wall)

    stack = []
    if updated_walls:
        updated_cells = []
        for wall in updated_walls:
            if wall&1 != 0:
                stack.append([mouse_x, mouse_y-1])
            if wall&2 != 0:
                stack.append([mouse_x+1, mouse_y])
            if wall&4 != 0:
                stack.append([mouse_x, mouse_y+1])
            if wall&8 != 0:
                stack.append([mouse_x-1, mouse_y])
        stack.append([mouse_x, mouse_y])
    return stack

def floodFill(memory, real):
    changed = 1
    real.moveMouse(1)
    memory.moveMouse(1)
    while(changed):
        changed = 0
        while(memory.cellValue[memory.mouse.y][memory.mouse.x]!=0):

            minCell = memory.minimumCell()
            real.moveMouse(minCell)
            memory.moveMouse(minCell)

            mouse_x, mouse_y = memory.mousePosition()
            previous_walls = memory.maze[mouse_y][mouse_x]
            new_walls = real.maze[mouse_y][mouse_x]

            init_stack = registerWalls(memory, previous_walls, new_walls, mouse_x, mouse_y)
            if init_stack:
                changed = 1
            stack_Iter(init_stack, memory)

            memory.update()
            real.update() # Caso a GUI não esteja sendo constantemente atualizada, os botões não funcionam
        if not changed:
            break

        while(memory.mousePosition()!=(0,15)):
            minCell = memory.minimumReturnCell()
            real.moveMouse(minCell)
            memory.moveMouse(minCell)

            mouse_x, mouse_y = memory.mousePosition()
            previous_walls = memory.maze[mouse_y][mouse_x]
            new_walls = real.maze[mouse_y][mouse_x]

            init_stack = registerWalls(memory, previous_walls, new_walls, mouse_x, mouse_y)
            if init_stack:
                changed = 1
            stack_Iter(init_stack, memory)

            memory.update()
            real.update()


def fastRun(maze):
    while(maze.cellValue[maze.mouse.y][maze.mouse.x]!=0):
        minCell = maze.minimumCell()
        maze.moveMouse(minCell)

        maze.update()
