from tkinter import *

class Interface: # Classe que cria a interface gráfica do programa

    def __init__(self, maze):
        # Funções dos botões
        def move_up():
            self.maze.moveMouse(1)
        def move_right():
            self.maze.moveMouse(2)
        def move_down():
            self.maze.moveMouse(4)
        def move_left():
            self.maze.moveMouse(8)

        def toggle_wall_up():
            self.maze.toggleWall([self.maze.mouse.x, self.maze.mouse.y], 1)
        def toggle_wall_right():
            self.maze.toggleWall([self.maze.mouse.x, self.maze.mouse.y], 2)
        def toggle_wall_down():
            self.maze.toggleWall([self.maze.mouse.x, self.maze.mouse.y], 4)
        def toggle_wall_left():
            self.maze.toggleWall([self.maze.mouse.x, self.maze.mouse.y], 8)

        # Declaração da estrutura
        self.master = Tk()
        self.master.wm_state('zoomed')
        self.maze = maze
        self.outer_frame = Frame(self.master)
        self.outer_frame.pack()
        self.canvas_frame = Frame(self.outer_frame)

        # Labirinto em si
        self.w = Canvas(self.canvas_frame, width = 660, height = 660)
        self.canvas_frame.grid(row = 0, column = 0, rowspan = 2)
        self.draw()

        # Separadores para organização
        self.separator_frame = Frame(self.outer_frame)
        self.outer_frame.grid_columnconfigure(1, minsize = 50)
        self.outer_frame.grid_columnconfigure(3, minsize = 50)
        self.separator_frame.grid(row = 0, column = 1)
        self.separator_frame.grid(row = 0, column = 3)

        # Botões de setinhas
        # self.arrows_frame = Frame(self.outer_frame)

        # up = Button(self.arrows_frame, text = "Up", command = move_up)
        # up.grid(row = 0, column = 1)
        # up.config(height = 5, width = 10)

        # right = Button(self.arrows_frame, text = "Right", command = move_right)
        # right.grid(row = 1, column = 2)
        # right.config(height = 5, width = 10)

        # down = Button(self.arrows_frame, text = "Down", command = move_down)
        # down.grid(row = 2, column = 1)
        # down.config(height = 5, width = 10)

        # left = Button(self.arrows_frame, text = "Left", command = move_left)
        # left.grid(row = 1, column = 0)
        # left.config(height = 5, width = 10)

        # self.arrows_frame.grid(row = 0, column = 2)

        # # Botões de paredes
        # self.walls_frame = Frame(self.outer_frame)

        # up_wall = Button(self.walls_frame, text = "Up Wall", command = toggle_wall_up)
        # up_wall.grid(row = 0, column = 1)
        # up_wall.config(height = 5, width = 10)

        # right_wall = Button(self.walls_frame, text = "Right Wall", command = toggle_wall_right)
        # right_wall.grid(row = 1, column = 2)
        # right_wall.config(height = 5, width = 10)

        # down_wall = Button(self.walls_frame, text = "Down Wall", command = toggle_wall_down)
        # down_wall.grid(row = 2, column = 1)
        # down_wall.config(height = 5, width = 10)

        # left_wall = Button(self.walls_frame, text = "Left Wall", command = toggle_wall_left)
        # left_wall.grid(row = 1, column = 0)
        # left_wall.config(height = 5, width = 10)

        # self.walls_frame.grid(row = 1, column = 2)

        # Necessário para a GUI atualizar
        self.master.update_idletasks()
        self.master.update()


    def draw(self): # Função que (re)desenha todo labirinto(não usar sempre, é lenta)
        wall = "black"
        cell = "white"
        empty_wall = "light gray"
        target_color = "red"
        mouse_color = "yellow"
        mouse_front = "green"
        for j in range(16):
            for i in range(16):
                self.w.create_rectangle(40*i + 5, 40*j + 5, 40*i + 15, 40*j + 15, fill = wall, outline = wall)
                if self.maze.maze[j][i]&1 != 0:
                    self.w.create_rectangle(40*i + 15, 40*j + 5, 40*i + 45, 40*j + 15, fill = wall, outline = wall)
                else:
                    self.w.create_rectangle(40*i + 15, 40*j + 5, 40*i + 45, 40*j + 15, fill = empty_wall, outline = empty_wall)
            self.w.create_rectangle(40*16 + 5, 40*j + 5, 40*16 + 15, 40*j + 15, fill = wall, outline = wall)
            for i in range(16):
                if self.maze.maze[j][i]&8 != 0:
                    self.w.create_rectangle(40*i + 5, 40*j + 15, 40*i + 15, 40*j + 45, fill = wall, outline = wall)
                else:
                    self.w.create_rectangle(40*i + 5, 40*j + 15, 40*i + 15, 40*j + 45, fill = empty_wall, outline = empty_wall)
                alvo = False
                for target in self.maze.targets:
                    if target[0] == j and target[1] == i:
                        alvo = True
                if self.maze.mouse.x == i and self.maze.mouse.y == j:
                    if self.maze.mouse.d == 1:
                        self.w.create_rectangle(40*i + 15, 40*j + 25, 40*i + 45, 40*j + 45, fill = mouse_color, outline = mouse_color)
                        self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 25, fill = mouse_front, outline = mouse_front)
                    elif self.maze.mouse.d == 2:
                        self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 35, 40*j + 45, fill = mouse_color, outline = mouse_color)
                        self.w.create_rectangle(40*i + 35, 40*j + 15, 40*i + 45, 40*j + 45, fill = mouse_front, outline = mouse_front)
                    elif self.maze.mouse.d == 4:
                        self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 35, fill = mouse_color, outline = mouse_color)
                        self.w.create_rectangle(40*i + 15, 40*j + 35, 40*i + 45, 40*j + 45, fill = mouse_front, outline = mouse_front)
                    elif self.maze.mouse.d == 8:
                        self.w.create_rectangle(40*i + 35, 40*j + 15, 40*i + 45, 40*j + 45, fill = mouse_color, outline = mouse_color)
                        self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 35, 40*j + 45, fill = mouse_front, outline = mouse_front)
                    self.w.create_text(40*i + 30, 40*j + 30, text = 'M')
                elif alvo:
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = target_color, outline = target_color)
                else:
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = cell, outline = cell)
                    # self.w.create_text(40*i + 30, 40*j + 30, text = self.maze.cellValue[j][i]) # Mostra o valor das paredes na célula
            self.w.create_rectangle(40*16 + 5, 40*j + 15, 40*16 + 15, 40*j + 45, fill = wall, outline = wall)
        for i in range(16):
            self.w.create_rectangle(40*i + 5, 40*16 + 5, 40*i + 15, 40*16 + 15, fill = wall, outline = wall)
            self.w.create_rectangle(40*i + 15, 40*16 + 5, 40*i + 45, 40*16 + 15, fill = wall, outline = wall)
        self.w.create_rectangle(40*16 + 5, 40*16 + 5, 40*16 + 15, 40*16 + 15, fill = wall, outline = wall)
        self.w.pack()

    def update(self): # Função usada para atualizar a GUI
        self.master.update_idletasks()
        self.master.update()


    def update_cells(self, lista): # Atualiza apenas uma lista de células que foi mudada, bem mais rápido que todo o labirinto
        cell = "white"
        target_color = "red"
        mouse_color = "yellow"
        mouse_front = "green"
        for [i, j] in lista:
            alvo = False
            for target in self.maze.targets:
                    if target[0] == j and target[1] == i:
                        alvo = True
            if self.maze.mouse.x == i and self.maze.mouse.y == j:
                if self.maze.mouse.d == 1:
                    self.w.create_rectangle(40*i + 15, 40*j + 25, 40*i + 45, 40*j + 45, fill = mouse_color, outline = mouse_color)
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 25, fill = mouse_front, outline = mouse_front)
                elif self.maze.mouse.d == 2:
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 35, 40*j + 45, fill = mouse_color, outline = mouse_color)
                    self.w.create_rectangle(40*i + 35, 40*j + 15, 40*i + 45, 40*j + 45, fill = mouse_front, outline = mouse_front)
                elif self.maze.mouse.d == 4:
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 35, fill = mouse_color, outline = mouse_color)
                    self.w.create_rectangle(40*i + 15, 40*j + 35, 40*i + 45, 40*j + 45, fill = mouse_front, outline = mouse_front)
                elif self.maze.mouse.d == 8:
                    self.w.create_rectangle(40*i + 25, 40*j + 15, 40*i + 45, 40*j + 45, fill = mouse_color, outline = mouse_color)
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 25, 40*j + 45, fill = mouse_front, outline = mouse_front)
                self.w.create_text(40*i + 30, 40*j + 30, text = 'M')

            elif alvo:
                self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = target_color, outline = target_color)
            else:
                self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = cell, outline = cell)
                # self.w.create_text(40*i + 30, 40*j + 30, text = self.maze.cellValue[j][i]) # Mostra o valor das paredes na célula

        self.master.update_idletasks()
        self.master.update()

    def update_wall(self, position, parede, add = 1): # Atualiza(adiciona ou remove) a situação de uma parede
        wall = "black"
        empty_wall = "light gray"
        i = position[0]
        j = position[1]
        if add == 1:
            if parede == 1:
                self.w.create_rectangle(40*i + 15, 40*j + 5, 40*i + 45, 40*j + 15, fill = wall, outline = wall)
            elif parede == 2:
                self.w.create_rectangle(40*i + 45, 40*j + 15, 40*i + 55, 40*j + 45, fill = wall, outline = wall)
            elif parede == 4:
                self.w.create_rectangle(40*i + 15, 40*j + 45, 40*i + 45, 40*j + 55, fill = wall, outline = wall)
            else:
                self.w.create_rectangle(40*i + 5, 40*j + 15, 40*i + 15, 40*j + 45, fill = wall, outline = wall)
        else:
            if parede == 1:
                self.w.create_rectangle(40*i + 15, 40*j + 5, 40*i + 45, 40*j + 15, fill = empty_wall, outline = empty_wall)
            elif parede == 2:
                self.w.create_rectangle(40*i + 45, 40*j + 15, 40*i + 55, 40*j + 45, fill = empty_wall, outline = empty_wall)
            elif parede == 4:
                self.w.create_rectangle(40*i + 15, 40*j + 45, 40*i + 45, 40*j + 55, fill = empty_wall, outline = empty_wall)
            else:
                self.w.create_rectangle(40*i + 5, 40*j + 15, 40*i + 15, 40*j + 45, fill = empty_wall, outline = empty_wall)
        self.master.update_idletasks()
        self.master.update()

