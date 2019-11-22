import pygame

PI = 3.1415926535897
# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (165, 42, 42)
CYAN = (127, 255, 255)
GRAY = (105, 105, 105)
YELLOW = (255, 255, 153)
ORANGE = (255, 165, 0)
DARK_GREEN = (0, 100, 0)
r = 255
g = 0
b = 0

def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150+x, 170+y], [75+x, 20+y], [x, 170+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x, 120+y], [75+x, y], [10+x, 120+y]])
    pygame.init()

def volume_sphere(radius):
    pi = 3.141592653589
    volume = (4 / 3) * pi * radius ** 3
    print("The volume is", volume)

def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    print("The volume is", volume)
    return volume

def sum_two_numbers(a, b):
    result = a + b
    return result
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
    draw_tree(screen, 150, 200)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
