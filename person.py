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
            else:
                pass

        if direction == "left":
            if self.x_value != 0:
                if self.maze.grid[self.y_value][self.x_value + 1] == 0:
                    self.x_value -= 1
            else:
                pass

        if direction == "":
            if self.x_value <= self.maze.width - 1:
                if self.maze.grid[self.y_value][self.x_value + 1] == 0:
                    self.x_value += 1
            else:
                pass
        ### What action do we need to do based on the direction?
        ### YOUR CODE HERE
        pass

    def draw(self, window):
        ### How are we going to draw the person?
        ### YOUR CODE HERE
        pass
