import pygame

### What other modules do we need access to?
### YOUR CODE HERE

### Initialize pygame stuff (don't worry too much about this).
pygame.init()
window = pygame.display.set_mode([100, 100])
clock = pygame.clock.Clock()

### Initialize the maze, the person, and the goal objects.
### YOUR CODE HERE

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
