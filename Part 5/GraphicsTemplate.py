import pygame

PI = 3.1415926535897
# Define some colors, you may want to add more
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
r = 255
g = 0
b = 0
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
        # --- Main event loop
        if r > 0 and b == 0:
                r -= 25.5
                g += 25.5
                RGB = (r, g, b)
        elif g > 0 and r == 0:
                g -= 25.5
                b += 25.5
                RGB = (r, g, b)
        elif b > 0 and g == 0:
                r += 25.5
                b -= 25.5
                RGB = (r, g, b)
        # --- All events are detected here
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
        # --- Game logic should go here

        # --- Screen-clearing code goes here
         #  Here, we clear the screen to white. 
        screen.fill(WHITE)

        
        # --- Drawing code should go here



        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        
# Close the window and quit.
pygame.quit()
