import pygame

pygame.init()
window = pygame.display.set_mode([100, 100])

while True:
    ### Continuously, process all 'events' that pygame has detected.
    for event in pygame.event.get():
        ### If the event is a key press:
        if event.type == pygame.KEYDOWN:
            ### If the key was the 'down' arrow key:
            if event.key == pygame.K_LEFT:
                ### What should we do?
            else:
                pass
