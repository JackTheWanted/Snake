import pygame
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
done = False
size = (700, 500)
while not done:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Professor Craven's Cool Game")
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True
    screen.fill(GREEN)
