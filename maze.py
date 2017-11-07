from interface import *

class Mouse:
    def __init__(self, x = 0, y = 0, direction = 4):
        self.x = x
        self.y = y
        self.d = direction

    def move(self, direction = 0):
        if direction != 0:
            self.d = direction

        if self.d == 1:
            self.y -= 1
        elif self.d == 2:
            self.x += 1
        elif self.d == 4:
            self.y += 1
        elif self.d == 8:
            self.x -= 1

class Maze:
    def __init__(self, maze = 0, M = Mouse(), target = [[7,7],[7,8],[8,7],[8,8]]):
        self.mouse = M
        self.targets = target
        if maze == 0: # Labirinto Vazio
            maze = [[9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [12,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6]]
        elif maze == 1:
            maze = [[9,3,9,5,5,1,7,9,3,9,3,9,5,5,5,3], [10,12,6,9,3,10,9,6,12,6,10,10,9,5,5,6], [10,9,5,6,12,6,12,3,9,2,10,10,10,13,1,3], [10,10,9,5,5,5,5,6,14,8,4,6,10,11,10,10],
                    [10,10,8,3,9,3,9,3,9,2,9,3,8,2,10,10], [10,8,6,12,6,12,6,8,6,12,6,12,6,12,6,10], [10,10,9,3,9,5,3,12,7,11,11,11,11,9,5,2], [10,10,10,10,10,9,6,9,1,0,0,0,0,0,7,10],
                    [10,10,10,10,10,8,3,12,6,14,14,14,14,12,1,6], [10,10,10,10,10,14,12,5,5,5,5,5,5,5,4,3], [10,10,10,12,6,9,3,9,3,9,3,9,3,9,3,10], [10,10,12,5,1,6,12,6,12,6,12,6,12,6,12,6],
                    [10,8,5,1,6,11,9,5,5,5,5,5,5,3,13,3], [10,12,3,12,5,4,6,9,5,1,5,1,5,6,9,2], [8,3,12,5,5,5,5,6,11,12,5,4,5,5,6,10], [14,12,5,5,5,5,5,5,4,5,5,5,5,5,5,6]]
        self.maze = maze
        self.inter = Interface(self)

    def __str__(self):
        draw = [['+',' ','+', ' ',' ',' ', '+',' ','+'], ['+','_','+', ' ',' ',' ', '+',' ','+'],
                ['+',' ','+', ' ',' ','|', '+',' ','+'], ['+','_','+', ' ',' ','|', '+',' ','+'],
                ['+',' ','+', ' ',' ',' ', '+','_','+'], ['+','_','+', ' ',' ',' ', '+','_','+'],
                ['+',' ','+', ' ',' ','|', '+','_','+'], ['+','_','+', ' ',' ','|', '+','_','+'],
                ['+',' ','+', '|',' ',' ', '+',' ','+'], ['+','_','+', '|',' ',' ', '+',' ','+'],
                ['+',' ','+', '|',' ','|', '+',' ','+'], ['+','_','+', '|',' ','|', '+',' ','+'],
                ['+',' ','+', '|',' ',' ', '+','_','+'], ['+','_','+', '|',' ',' ', '+','_','+'],
                ['+',' ','+', '|',' ','|', '+','_','+'], ['x','x','x', 'x','x','x', 'x','x','x']]


        '''
                Sendo a existência de uma parede = 1 e a não existência = 0,
                "Número" do bloco = 1*(cima) + 2*(direita) + 4*(baixo) + 8*(esquerda)

                0 = + . +    1 = + _ +    2 = + . +   3 = + _ +
                    . . .        . . .        . . |       . . |
                    + . +        + . +        + . +       + . +

                4 = + . +    5 = + _ +    6 = + . +    7 = + _ +
                    . . .        . . .        . . |        . . |
                    + _ +        + _ +        + _ +        + _ +

                8 = + . +    9 = + _ +   10 = + . +   11 = + _ +
                    | . .        | . .        | . |        | . |
                    + . +        + . +        + . +        + . +

                12= + . +   13 = + _ +   14 = + . +   15 = + _ +
                    | . .        | . .        | . |        | . |
                    + _ +        + _ +        + _ +        + _ +
        '''

        string = '\n'

        for line in range(16): # Percorre todas as linhas
            line_part = 0
            while line_part < 3: # Cada linha é dividida em 3 partes individuais
                for row in range(16): # Percorre todas as colunas
                    row_part = 0
                    while row_part < 3: #Cada coluna é dividida em 3 partes
                        if((line == 0 and line_part == 0) or (row_part == 0 and row == 0) or (row == 15 and row_part == 2) or (line == 15 and line_part == 2)): #Trata dos casos de borda

                            if(row_part == 0 and line == 0 and line_part == 0):
                                row_part = 1
                            elif(row_part == 2 and line == 0 and line_part == 0 and row == 15):
                                string += "# "

                            if(row_part == 0 and line == 15 and line_part == 2):
                                row_part = 1
                            elif(row_part == 2 and line == 15 and line_part == 2 and row == 15):
                                string += "# "

                            string += "# "

                        else:
                            if(row_part == 0): # Se chegou aqui, não está na borda, então ignoramos a primeira parte da linha e coluna, para evitar repetições
                                row_part = 1
                            if(line_part == 0):
                                line_part = 1
                            m = False
                            t = False
                            if self.mouse.x == row and self.mouse.y == line:
                                if row_part == 1 and line_part == 1:
                                    string += 'M '
                                    m = True
                            else:
                                for target in self.targets:
                                    if target[0] == line and target[1] == row:
                                        if row_part == 1 and line_part == 1:
                                            string += 'T '
                                            t = True
                            if not t and not m:
                                string = string + draw[self.maze[line][row]][row_part + (line_part*3)] + " "
                        row_part += 1
                line_part += 1

                string += '\n'

        return string

    def addWall(self, position = [0,0], direction = 0):
        if (self.maze[position[1]][position[0]] & direction) == 0:
            self.maze[position[1]][position[0]] += direction
            if direction == 1 and position[1] > 0:
                self.maze[position[1] - 1][position[0]] += 4
            if direction == 2 and position[0] < 15:
                self.maze[position[1]][position[0] + 1] += 8
            if direction == 4 and position[1] < 15:
                self.maze[position[1] + 1][position[0]] += 1
            if direction == 8 and position[0] > 0:
                self.maze[position[1]][position[0] - 1] += 2
            self.inter.update_wall(position, direction)



    def moveMouse(self, direction = 0):
        cell = "white"
        mouse_color = "yellow"

        if direction == 0:
            return False

        if (self.maze[self.mouse.y][self.mouse.x] & direction) == 0:
            print (self.maze[self.mouse.y][self.mouse.x], direction)
            i_1 = self.mouse.x
            j_1 = self.mouse.y
            self.mouse.move(direction)
            i_2 = self.mouse.x
            j_2 = self.mouse.y

            self.inter.update_cells([[i_1,j_1], [i_2,j_2]])

        else:

            return False


