white = [255, 255, 255]
black = [0, 0, 0]

class Maze:
    def __init__(self, height, width, grid):
        self.height = height
        self.width = width
        self.grid = grid

        ### You may want to add more attributes (or not)
        ### YOUR CODE HERE

    def draw(self, window):
        for value_y in range(self.height):
            for value_x in range(self.width):
                if self.grid[value_y][value_x] == 0:
                    draw_color = white
                else:
                    draw_color = black

                ### YOUR CODE HERE
                ### Hint: you can do it in one line . . .
                ### Hint: to draw a rectangle, the command is:
                ### pygame.draw.rect(window, color, (left, right, width, height))
