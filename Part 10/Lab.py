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
YELLOW = (255, 255, 0)
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
def draw_bus(screen, x, y):
    pygame.draw.circle(screen, BLACK, (5+x, 30+y), 5)
    pygame.draw.circle(screen, BLACK, (45+x, 30+y), 5)
    pygame.draw.rect(screen, YELLOW, (0+x, 0+y, 50, 30))
    pygame.draw.rect(screen, CYAN, (40+x, 0+y, 10, 10))
    pygame.draw.rect(screen, CYAN, (25+x, 10+y, 8, 8))
    pygame.draw.rect(screen, CYAN, (10+x, 10+y, 8, 8))


def draw_knife(screen, x, y):
    pygame.draw.rect(screen, BROWN, (5+x, 20+y, 10, 20))
    pygame.draw.line(screen, GRAY, (x, 20+y), (20+x, 20+y), 3)
    pygame.draw.rect(screen, GRAY, (5+x, y, 10, 20))
    pygame.draw.polygon(screen, GRAY, ([5+x, y-10], [14+x, y], [5+x, y]))
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
    pygame.mouse.set_visible(False)
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.

    screen.fill(WHITE)

    # --- Drawing code should go here
    draw_knife(screen, x, y)
    draw_bus(screen, x_coord, y_coord)
    if x_coord >= 725:
        x_coord = -50
    elif x_coord <= -50:
        x_coord = 725
    if y_coord >= 500:
        y_coord = -50
    elif y_coord <= -50:
        y_coord = 500


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
