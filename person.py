import sys

import pygame

class Person:
    def __init__(self, x_value, y_value, maze):
        self.x_value = x_value
        self.y_value = y_value
        self.maze = maze

    def move(self, direction):
        if direction == "right":
            if self.x_value < self.maze.width - 1:
                if self.maze.grid[self.y_value][self.x_value + 1] == 0:
                    self.x_value += 1
            elif self.x_value == self.maze.width - 1:
                if self.y_value == self.maze.height - 1:
                    self.x_value += 1
                    sys.exit()

        if direction == "left":
            if self.x_value != 0:
                if self.maze.grid[self.y_value][self.x_value - 1] == 0:
                    self.x_value -= 1
            else:
                pass

        if direction == "up":
            if self.y_value > 0:
                if self.maze.grid[self.y_value - 1][self.x_value] == 0:
                    self.y_value -= 1
            else:
                pass

        if direction == "down":
            if self.y_value < self.maze.height - 1:
                if self.maze.grid[self.y_value + 1][self.x_value] == 0:
                    self.y_value += 1
            elif self.x_value == self.maze.width - 1:
                if self.y_value == self.maze.height - 1:
                    self.y_value += 1
                    sys.exit()
            else:
                pass

    def draw(self, window):
        x_center = (self.x_value * self.maze.cell_size) + (self.maze.cell_size / 2)
        y_center = (self.y_value * self.maze.cell_size) + (self. maze.cell_size / 2)
        pygame.draw.circle(window, (50, 255, 255), (x_center, y_center), self.maze.cell_size / 2)
