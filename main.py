import pygame

import maze_generation
from maze import Maze

height = 50
width = 50

pygame.init()
window = pygame.display.set_mode([width*20, height*20])
clock = pygame.time.Clock()

grid = maze_generation.gen_grid(height, width)
maze = Maze(height, width, grid)

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

    ### Check if we've caught the goal.
    ### YOUR CODE HERE

    ### We should probably redraw everything.
    ### YOUR CODE HERE

    ### Update the pygame display.
    pygame.display.flip()
