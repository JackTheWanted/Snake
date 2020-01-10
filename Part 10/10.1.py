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
# Speed in pixels per frame
x_speed = 0
y_speed = 0
# Current position
x_coord = 10
y_coord = 10
def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35+x, y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [x, 65+y, 100, 100])
def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, WHITE, [1+x, y, 10, 10], 0)
    # Legs
    pygame.draw.line(screen, WHITE, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, WHITE, [5+x, 17+y], [x, 27+y], 2)
    # Body
    pygame.draw.line(screen, RED, [5+x, 17+y], [5+x, 7+y], 2)
    # Arms
    pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 2)

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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

    x_coord += x_speed
    y_coord += y_speed
    # --- Game logic should go here
    # pygame.mouse.set_visible(False)
    # pos = pygame.mouse.get_pos()
    # x = pos[0]
    # y = pos[1]
    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.

    screen.fill(BLACK)

    # --- Drawing code should go here
    draw_stick_figure(screen, 10, 40)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
