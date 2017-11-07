from tkinter import *

class Interface:
    def __init__(self, maze):
        self.master = Tk()
        self.maze = maze
        self.w = Canvas(self.master, width = 660, height = 660)
        self.draw()
        self.master.update_idletasks()
        self.master.update()


    def draw(self):
        wall = "black"
        cell = "white"
        empty_wall = "light gray"
        target_color = "red"
        mouse_color = "yellow"
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
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = mouse_color, outline = mouse_color)
                    self.w.create_text(40*i + 30, 40*j + 30, text = 'M')
                elif alvo:
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = target_color, outline = target_color)
                else:
                    self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = cell, outline = cell)
                    # self.w.create_text(40*i + 30, 40*j + 30, text = self.maze.maze[j][i])
            self.w.create_rectangle(40*16 + 5, 40*j + 15, 40*16 + 15, 40*j + 45, fill = wall, outline = wall)
        for i in range(16):
            self.w.create_rectangle(40*i + 5, 40*16 + 5, 40*i + 15, 40*16 + 15, fill = wall, outline = wall)
            self.w.create_rectangle(40*i + 15, 40*16 + 5, 40*i + 45, 40*16 + 15, fill = wall, outline = wall)
        self.w.create_rectangle(40*16 + 5, 40*16 + 5, 40*16 + 15, 40*16 + 15, fill = wall, outline = wall)
        self.w.pack()

    def update(self):
        self.draw()
        self.master.update_idletasks()
        self.master.update()

    def update_cells(self, lista):
        cell = "white"
        target_color = "red"
        mouse_color = "yellow"
        for [i, j] in lista:
            alvo = False
            for target in self.maze.targets:
                    if target[0] == j and target[1] == i:
                        alvo = True
            if self.maze.mouse.x == i and self.maze.mouse.y == j:
                self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = mouse_color, outline = mouse_color)
                self.w.create_text(40*i + 30, 40*j + 30, text = 'M')
            elif alvo:
                self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = target_color, outline = target_color)
            else:
                self.w.create_rectangle(40*i + 15, 40*j + 15, 40*i + 45, 40*j + 45, fill = cell, outline = cell)
                # self.w.create_text(40*i + 30, 40*j + 30, text = self.maze.maze[j][i])

        self.master.update_idletasks()
        self.master.update()

    def update_wall(self, position, parede):
        wall = "black"
        i = position[0]
        j = position[1]
        if parede == 1:
            self.w.create_rectangle(40*i + 15, 40*j + 5, 40*i + 45, 40*j + 15, fill = wall, outline = wall)
        elif parede == 2:
            self.w.create_rectangle(40*i + 45, 40*j + 15, 40*i + 55, 40*j + 45, fill = wall, outline = wall)
        elif parede == 4:
            self.w.create_rectangle(40*i + 15, 40*j + 45, 40*i + 45, 40*j + 55, fill = wall, outline = wall)
        else:
            self.w.create_rectangle(40*i + 5, 40*j + 15, 40*i + 15, 40*j + 45, fill = wall, outline = wall)

        self.master.update_idletasks()
        self.master.update()
