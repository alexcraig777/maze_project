import pygame

white = [255, 255, 255]
black = [0, 0, 0]

class Maze:
    def __init__(self, height, width, grid):
        self.height = height
        self.width = width
        self.grid = grid

        self.cell_size = 20

        ### You may want to add more attributes (or not)
        ### YOUR CODE HERE

    def draw(self, window):
        for value_y in range(self.height):
            for value_x in range(self.width):
                if self.grid[value_y][value_x] == 0:
                    draw_color = white
                else:
                    draw_color = black
                pygame.draw.rect(window, draw_color, (value_x * self.cell_size,
                                                      value_y * self.cell_size,
                                                      self.cell_size, self.cell_size))