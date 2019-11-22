#Jack C
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
DARK_GREEN = (0,100,0)
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
                r -= 5
                g += 5
                RGB = (r, g, b)
        elif g > 0 and r == 0:
                g -= 5
                b += 5
                RGB = (r, g, b)
        elif b > 0 and g == 0:
                r += 5
                b -= 5
                RGB = (r, g, b)
        # --- All events are detected here
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
        # --- Game logic should go here

        # --- Screen-clearing code goes here

         #  Here, we clear the screen to white. 
        screen.fill(CYAN)

        
        # --- Drawing code should go here

        #Ground
        pygame.draw.rect(screen, GREEN, [0, 350, 700, 150])

        #Cloud
        for i in range(0,150,50):
                pygame.draw.ellipse(screen, WHITE, [i+50, 50, 100, 100])


        # Cloud
        for i in range(0,150,50):
                pygame.draw.ellipse(screen, WHITE, [i+475, 50, 100, 100])


        #House base
        pygame.draw.rect(screen, RED, [200, 250, 300, 250 ])

        #Chimney
        for i in range(0,80,20):
                pygame.draw.ellipse(screen, RGB, [450, 70+i, 30, 30])


        pygame.draw.rect(screen, BLACK, [450, 150, 30, 70])

        #House roof
        pygame.draw.polygon(screen, BLACK, [[180, 250], [350, 125], [520, 250]])

        #Window
        pygame.draw.rect(screen, CYAN, [235, 385, 60, 60])
        pygame.draw.rect(screen, CYAN, [415, 385, 60, 60])

        #House door
        pygame.draw.rect(screen, BROWN, [320, 375, 75, 125])
        pygame.draw.ellipse(screen, BLACK, [375, 435, 10, 10])

        #Top window
        pygame.draw.ellipse(screen, CYAN, [310, 265, 90, 90])

        #Tree trunk
        pygame.draw.rect(screen, BROWN, [70, 350, 65, 150])

        #Tree Leaves
        pygame.draw.polygon(screen, DARK_GREEN, [[40, 350], [102.5, 200], [165, 350]])
        pygame.draw.polygon(screen, DARK_GREEN, [[40, 400], [102.5, 250], [165, 400]])
        pygame.draw.polygon(screen, DARK_GREEN, [[40, 450], [102.5, 300], [165, 450]])
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        # --- Limit to 60 frames per second
        clock.tick(60)
        
# Close the window and quit.
pygame.quit()
