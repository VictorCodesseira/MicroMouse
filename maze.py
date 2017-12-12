from interface import *
from time import sleep

class Mouse: # Classe do mouse(só pra facilitar um pouco)
    def __init__(self, x = 0, y = 15, direction = 1):
        self.x = x
        self.y = y
        self.d = direction

    def move(self, direction = 0):
        if self.d != direction:
            self.d = direction


        if self.d == 1:
            self.y -= 1
        elif self.d == 2:
            self.x += 1
        elif self.d == 4:
            self.y += 1
        elif self.d == 8:
            self.x -= 1

    def turn(self,right = 1):
        dire = [1,2,4,8,1,8]
        for i in range(len(dire)):
            if self.d == dire[i]:
                if right == 1:
                    self.d = dire[i+1]
                else:
                    self.d = dire[i-1]
                return



class Maze: # Classe do labirinto em si
    def __init__(self, maze = 0, inter = 0, M = 0, target = [[7,7],[7,8],[8,7],[8,8]]):
        if M == 0:
            self.mouse = Mouse()
        else:
            self.mouse = M
        self.targets = target # Lista de "alvos" do labirinto
        if maze == 0: # Labirinto Vazio
            maze = [[9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
                    [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2], [14,12,4,4,4,4,4,4,4,4,4,4,4,4,4,6]]
        elif maze == 1: # Labirinto 2016
            maze = [[9,3,9,5,5,1,7,9,3,9,3,9,5,5,5,3], [10,12,6,9,3,10,9,6,12,6,10,10,9,5,5,6], [10,9,5,6,12,6,12,3,9,3,10,10,10,13,1,3], [10,10,9,5,5,5,5,6,14,8,4,6,10,11,10,10],
                    [10,10,8,3,9,3,9,3,9,2,9,3,8,2,10,10], [10,8,6,12,6,12,6,8,6,12,6,12,6,12,6,10], [10,10,9,3,9,5,3,12,7,11,11,11,11,9,5,2], [10,10,10,10,10,9,6,9,1,0,0,0,0,0,7,10],
                    [10,10,10,10,10,8,3,12,6,14,14,14,14,12,1,6], [10,10,10,10,10,14,12,5,5,5,5,5,5,5,4,3], [10,10,10,12,6,9,3,9,3,9,3,9,3,9,3,10], [10,10,12,5,1,6,12,6,12,6,12,6,12,6,12,6],
                    [10,8,5,1,6,11,9,5,5,5,5,5,5,3,13,3], [10,12,3,12,5,4,6,9,5,1,5,1,5,6,9,2], [8,3,12,5,5,5,5,6,11,12,5,4,5,5,6,10], [14,12,5,5,5,5,5,5,4,5,5,5,5,5,5,6]]
        self.maze = maze
        self.cellValue = []
        for i in range(16):
            linha = []
            for j in range(16):
                linha.append(self.initialCellValue([i,j]))
            self.cellValue.append(linha)
        self.returnCellValue = []
        for i in range(16):
            linha = []
            for j in range(16):
                dist_y = abs(15 - i)
                dist_x = abs(0 - j)
                linha.append(dist_y + dist_x)
            self.returnCellValue.append(linha)

        if inter == 1:
            self.inter = Interface(self)
        else:
            self.inter = 0

    def __str__(self): # Função que cuida de imprimir o labirinto no console(só usar print())
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


    def addWall(self, position = [0,0], direction = 0): # Adiciona uma parede em uma posição [x,y], numa direção
        if (self.maze[position[1]][position[0]] & direction) == 0:
            self.maze[position[1]][position[0]] += direction
            if direction == 1:
                self.maze[position[1] - 1][position[0]] += 4
            if direction == 2:
                self.maze[position[1]][position[0] + 1] += 8
            if direction == 4:
                self.maze[position[1] + 1][position[0]] += 1
            if direction == 8:
                self.maze[position[1]][position[0] - 1] += 2
            if self.inter != 0:
                self.inter.update_wall(position, direction, 1)

    def toggleWall(self, position = [0,0], direction = 0): # O mesmo que acima, mas se a parede já existir, remove ela
        if (self.maze[position[1]][position[0]] & direction) == 0:
            self.maze[position[1]][position[0]] += direction
            if direction == 1:
                self.maze[position[1] - 1][position[0]] += 4
            if direction == 2:
                self.maze[position[1]][position[0] + 1] += 8
            if direction == 4:
                self.maze[position[1] + 1][position[0]] += 1
            if direction == 8:
                self.maze[position[1]][position[0] - 1] += 2
            if self.inter != 0:
                self.inter.update_wall(position, direction, 1)
        else:
            self.maze[position[1]][position[0]] -= direction
            if direction == 1:
                self.maze[position[1] - 1][position[0]] -= 4
            if direction == 2:
                self.maze[position[1]][position[0] + 1] -= 8
            if direction == 4:
                self.maze[position[1] + 1][position[0]] -= 1
            if direction == 8:
                self.maze[position[1]][position[0] - 1] -= 2
            if self.inter != 0:
                self.inter.update_wall(position, direction, 0)

    def moveMouse(self, direction = 0): # Move o mouse e atualiza a interface
        TURNDELAY = 0.05
        MOVEDELAY = 0.05
        if direction == 0:
            return False
        if (self.maze[self.mouse.y][self.mouse.x] & direction) == 0:
            i_1 = self.mouse.x
            j_1 = self.mouse.y
            if self.mouse.d != direction:
                if self.mouse.d/direction == 4 or self.mouse.d/direction == 1/4:
                    self.mouse.turn(1)
                    if self.inter != 0:
                        self.inter.update_cells([[i_1,j_1]])
                    sleep(TURNDELAY)
                    self.mouse.turn(1)
                    if self.inter != 0:
                        self.inter.update_cells([[i_1,j_1]])
                    sleep(TURNDELAY)
                else:
                    dire = [1,2,4,8,1,8]
                    for i in range(len(dire)):
                        if self.mouse.d == dire[i]:
                            if direction == dire[i+1]:
                                self.mouse.turn(1)
                            else:
                                self.mouse.turn(0)
                            break
                    if self.inter != 0:
                        self.inter.update_cells([[i_1,j_1]])
                    sleep(TURNDELAY)


            self.mouse.move(direction)
            i_2 = self.mouse.x
            j_2 = self.mouse.y

            if self.inter != 0:
                self.inter.update_cells([[i_1,j_1], [i_2,j_2]])
            sleep(MOVEDELAY)
        else:
            return False

    def mouseValue(self): # Retorna o valor de paredes da célula na qual o mouse está
        return self.maze[self.mouse.y][self.mouse.x]

    def mousePosition(self): # Retorna uma lista [x,y] com a posição do mouse
        return self.mouse.x, self.mouse.y

    def update(self): # Atualiza a interface
        if self.inter != 0:
            self.inter.update()

    def setMouse(self, position = [0,0], direction = 1):
        i, j = self.mousePosition()

        self.mouse.x = position[0]
        self.mouse.y = position[1]
        self.mouse.d = direction
        if self.inter != 0:
            self.inter.update_cells([[i,j], [position[0],position[1]]])

    def initialCellValue(self, position = [0,0]):
        x, y = position
        menor_x = 16
        menor_y = 16
        for target in self.targets:
            dist_x = abs(target[1] - x)
            dist_y = abs(target[0] - y)
            if dist_x < menor_x:
                menor_x = dist_x
            if dist_y < menor_y:
                menor_y = dist_y
        return menor_x + menor_y

    def minimumCell(self):
        x, y = self.mousePosition()
        minDir = [16]
        minValue = 300
        if (self.maze[y][x] & 1) == 0 and self.cellValue[y-1][x] <= minValue:
            if self.cellValue[y-1][x] == minValue:
                minDir.append(1)
            else:
                minValue = self.cellValue[y-1][x]
                minDir = [1]
        if (self.maze[y][x] & 2) == 0 and self.cellValue[y][x+1] <= minValue:
            if self.cellValue[y][x+1] == minValue:
                minDir.append(2)
            else:
                minValue = self.cellValue[y][x+1]
                minDir = [2]
        if (self.maze[y][x] & 4) == 0 and self.cellValue[y+1][x] <= minValue:
            if self.cellValue[y+1][x] == minValue:
                minDir.append(4)
            else:
                minValue = self.cellValue[y+1][x]
                minDir = [4]
        if (self.maze[y][x] & 8) == 0 and self.cellValue[y][x-1] <= minValue:
            if self.cellValue[y][x-1] == minValue:
                minDir.append(8)
            else:
                minValue = self.cellValue[y][x-1]
                minDir = [8]
        for dire in minDir:
            relativo = dire/self.mouse.d
            if relativo == 1:
                return dire
        for dire in minDir:
            relativo = dire/self.mouse.d
            if relativo != 1/4 and relativo != 4:
                return dire
        return minDir[0]

    def minimumReturnCell(self):
        x, y = self.mousePosition()
        minDir = [16]
        minValue = 300
        if (self.maze[y][x] & 1) == 0 and self.returnCellValue[y-1][x] <= minValue:
            if self.returnCellValue[y-1][x] == minValue:
                minDir.append(1)
            else:
                minValue = self.returnCellValue[y-1][x]
                minDir = [1]
        if (self.maze[y][x] & 2) == 0 and self.returnCellValue[y][x+1] <= minValue:
            if self.returnCellValue[y][x+1] == minValue:
                minDir.append(2)
            else:
                minValue = self.returnCellValue[y][x+1]
                minDir = [2]
        if (self.maze[y][x] & 4) == 0 and self.returnCellValue[y+1][x] <= minValue:
            if self.returnCellValue[y+1][x] == minValue:
                minDir.append(4)
            else:
                minValue = self.returnCellValue[y+1][x]
                minDir = [4]
        if (self.maze[y][x] & 8) == 0 and self.returnCellValue[y][x-1] <= minValue:
            if self.returnCellValue[y][x-1] == minValue:
                minDir.append(8)
            else:
                minValue = self.returnCellValue[y][x-1]
                minDir = [8]
        for dire in minDir:
            relativo = dire/self.mouse.d
            if relativo == 1:
                return dire
        for dire in minDir:
            relativo = dire/self.mouse.d
            if relativo != 1/4 and relativo != 4:
                return dire
        return minDir[0]

    def updateCellValue(self, position, newValue):
        self.cellValue[position[1]][position[0]] = newValue
        if self.inter != 0:
            self.inter.update_cells([position])
