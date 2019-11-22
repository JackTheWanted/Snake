# Jack C
import pygame
import random
import time
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
LIGHT_ORANGE = (245, 185, 66)
DARK_ORANGE = (245, 161, 66)
night = False
r = 255
g = 0
b = 0
x2 = 0
width = 5
timer = 0
smoke_list = []
colour = []
sun_colour = YELLOW
sky_colour = CYAN
colour_list = [YELLOW, ORANGE, RED, WHITE]
colour_list2 = [CYAN, LIGHT_ORANGE, DARK_ORANGE, BLACK]
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [70+x, 350+y, 65, 150])
    pygame.draw.polygon(screen, DARK_GREEN, [[40+x, 350+y], [102.5+x, 200+y], [165+x, 350+y]])
    pygame.draw.polygon(screen, DARK_GREEN, [[40+x, 400+y], [102.5+x, 250+y], [165+x, 400+y]])
    pygame.draw.polygon(screen, DARK_GREEN, [[40+x, 450+y], [102.5+x, 300+y], [165+x, 450+y]])
def draw_door(screen, x, y):
    pygame.draw.rect(screen, BROWN, [320+x, 375+y, 75, 125])
    pygame.draw.ellipse(screen, BLACK, [375+x, 435+y, 10, 10])
for i in range(100):
    x = random.randrange(450, 480)
    y = random.randrange(150)
    width = random.randrange(5, 10)
    colour.append(colour_list[random.randint(0, 3)])
    smoke_list.append([x, y, width])


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

    # --- Drawing code should go here
    timer += 1

    if timer == 100:
        timer = 0

        if len(colour_list) == 0:
            colour_list = [YELLOW, ORANGE, RED, WHITE]
            colour_list2 = [CYAN, LIGHT_ORANGE, DARK_ORANGE, BLACK]

        sun_colour = colour_list[0]
        if colour_list[0] == WHITE:
            night = True
        elif colour_list[0] != WHITE:
            night = False
        colour_list.remove(colour_list[0])
        sky_colour = colour_list2[0]
        colour_list2.remove(colour_list2[0])



    screen.fill(sky_colour)
    pygame.draw.circle(screen, sun_colour, (0, 0), 100)

    # Ground
    pygame.draw.rect(screen, GREEN, [0, 350, 700, 150])

    # Cloud
    if not night:
        for i in range(1):
            pygame.draw.circle(screen, WHITE, (x2, 100), 50)
            pygame.draw.circle(screen, WHITE, (x2 + 50, 100), 50)
            pygame.draw.circle(screen, WHITE, (x2 + 100, 100), 50)
            x2 += 2
            if x2 > 750:
                x2 = -80

    # House base
    pygame.draw.rect(screen, RED, [200, 250, 300, 250])

    # Chimney
    if not night:
        for i in range(len(smoke_list)):
            pygame.draw.circle(screen, GRAY, (smoke_list[i][0], smoke_list[i][1]), 5)
            smoke_list[i][1] -= 1
            if smoke_list[i][1] < 0:
                y = random.randrange(180)
                smoke_list[i][1] = y
                x = random.randrange(455, 475)
                smoke_list[i][0] = x

    pygame.draw.rect(screen, GRAY, [450, 150, 30, 70])

    # House roof
    pygame.draw.polygon(screen, GRAY, [[180, 250], [350, 125], [520, 250]])

    # Window
    if not night:
        pygame.draw.rect(screen, CYAN, [235, 385, 60, 60])
        pygame.draw.rect(screen, CYAN, [415, 385, 60, 60])
        pygame.draw.ellipse(screen, CYAN, [310, 265, 90, 90])
    if night:
        pygame.draw.rect(screen, LIGHT_ORANGE, [235, 385, 60, 60])
        pygame.draw.rect(screen, LIGHT_ORANGE, [415, 385, 60, 60])
        pygame.draw.ellipse(screen, LIGHT_ORANGE, [310, 265, 90, 90])
    # House door
    draw_door(screen, 0, 0)

    # Trees
    draw_tree(screen, 0, 0)
    draw_tree(screen, 500, 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
