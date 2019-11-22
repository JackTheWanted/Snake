import pygame

PI = 3.1415926535897
# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
r = 255
g = 0
b = 0
rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 2
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if r > 0 and b == 0:
        r -= 1
        g += 1
        RGB = (r, g, b)
    elif g > 0 and r == 0:
        g -= 1
        b += 1
        RGB = (r, g, b)
    elif b > 0 and g == 0:
        r += 1
        b -= 1
        RGB = (r, g, b)
    # --- Game logic should go here

    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.
    screen.fill(BLACK)

    # --- Drawing code should go here
    if rect_x > 650 or rect_x < 0:
        rect_change_x *= -1
    if rect_y > 450 or rect_y < 0:
        rect_change_y *=  -1
    pygame.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RGB, [rect_x + 10, rect_y + 10, 30, 30])
    pygame.draw.rect(screen, RED, [rect_x + 20, rect_y + 20, 10, 10])
    rect_x += rect_change_x
    rect_y += rect_change_y
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
