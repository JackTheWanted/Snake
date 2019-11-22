import pygame, sys, time, random
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
CYAN = (127, 255, 255)
GRAY = (105, 105, 105)
YELLOW = (255, 255, 153)
ORANGE = (255, 165, 0)
DARK_GREEN = (0, 100, 0)
done = False
font = pygame.font.Font('freesansbold.ttf', 30)

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    sys.exit()
                return

def drawText(text, font, surface, x, y, clr):
    textobj = font.render(text, 1, clr)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


screen = pygame.display.set_mode([700, 500])


drawText('It\'s snake time!', font, screen, 250, 170, BLUE)
drawText('Press any key to start.', font, screen, 210, 270, BLUE)
pygame.display.update()
waitForPlayerToPressKey()

# Set the title of the window
pygame.display.set_caption('Walls')

# List to hold all the sprites
all_sprites_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)


clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(BLACK)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()


    # See if the player block has collided with anything.


    # Check the list of collisions.


    # Draw all the spites


    # Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)


pygame.quit()