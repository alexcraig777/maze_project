import sys

import pygame

import maze_generation
from maze import Maze
from person import Person

height = 20
width = 20

grid = maze_generation.gen_grid(height, width)
maze = Maze(height, width, grid)
person = Person(0, 0, maze)

### pygame initialization stuff.
pygame.init()
window = pygame.display.set_mode([width * maze.cell_size,
                                  height * maze.cell_size])
clock = pygame.time.Clock()

while True:
    ### Limit the loop to going 10 times per second.
    clock.tick(10)

    maze.draw(window)
    person.draw(window)

    ### Process all 'events' that pygame has detected since last loop.
    for event in pygame.event.get():
        ### If the event is a key press:
        if event.type == pygame.KEYDOWN:
            ### If the key was the 'down' arrow key:
            if event.key == pygame.K_LEFT:
                person.move("left")
            elif event.key == pygame.K_RIGHT:
                person.move("right")
            elif event.key == pygame.K_UP:
                person.move("up")
            elif event.key == pygame.K_DOWN:
                person.move("down")

        ### Try to exit as nicely as possible.
        if event.type == pygame.QUIT:
            sys.exit()

    ### Check if we've caught the goal.
    ### YOUR CODE HERE

    ### We should probably redraw everything.
    ### YOUR CODE HERE

    ### Update the pygame display.
    pygame.display.flip()
