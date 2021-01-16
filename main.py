import sys

import pygame

import maze_generation
from maze import Maze

height = 50
width = 50

grid = maze_generation.gen_grid(height, width)
maze = Maze(height, width, grid)

### pygame initialization stuff.
pygame.init()
window = pygame.display.set_mode([width * maze.cell_size,
                                  height * maze.cell_size])
clock = pygame.time.Clock()

### Draw stuff for quick gratification:
maze.draw(window)
pygame.display.flip()

while True:
    ### Limit the loop to going 10 times per second.
    clock.tick(10)
    
    ### Process all 'events' that pygame has detected since last loop.
    for event in pygame.event.get():
        ### If the event is a key press:
        if event.type == pygame.KEYDOWN:
            ### If the key was the 'down' arrow key:
            if event.key == pygame.K_LEFT:
                ### What should we do?
                ### YOUR CODE HERE
                pass
            ### Finish the rest of the arrow key options.
            ### YOUR CODE HERE

        ### Try to exit as nicely as possible.
        if event.type == pygame.QUIT:
            sys.exit()

    ### Check if we've caught the goal.
    ### YOUR CODE HERE

    ### We should probably redraw everything.
    ### YOUR CODE HERE

    ### Update the pygame display.
    pygame.display.flip()
