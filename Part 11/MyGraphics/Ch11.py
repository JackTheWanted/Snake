import pygame

PI = 3.1415926535897
# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (6, 253, 0)
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
angle = 0
rotate_speed = 0
x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 10
width = 300
height = 225
wide_speed = 0
height_speed = 0
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
background_image = pygame.image.load("Spidermanstreet.jpeg").convert()
foreground_image = pygame.image.load("tobey.png").convert()
foreground_image.set_colorkey(WHITE)
pygame.mixer.music.load('Pizza Song.ogg')
click_sound = pygame.mixer.Sound("Pizza_Time.wav")
pygame.mixer.music.play(0, 0.0)
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
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
            elif event.key == pygame.K_s:
                wide_speed = -5
                height_speed = -5
            elif event.key == pygame.K_g:
                wide_speed = 5
                height_speed = 5
            elif event.key == pygame.K_a:
                rotate_speed = 1
            elif event.key == pygame.K_d:
                rotate_speed = -1
            elif event.key == pygame.K_SPACE:
                background_image = pygame.image.load("Pizza Background.jpg").convert()

        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
            elif event.key == pygame.K_s:
                wide_speed = 0
                height_speed = 0
            elif event.key == pygame.K_g:
                wide_speed = 0
                height_speed = 0
            elif event.key == pygame.K_a:
                rotate_speed = 0
            elif event.key == pygame.K_d:
                rotate_speed = 0
            elif event.key == pygame.K_SPACE:
                background_image = pygame.image.load("Spidermanstreet.jpeg").convert()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()

    width += wide_speed
    height += height_speed
    if width < 3:
        wide_speed = 0
    if height < 2.25:
        height_speed = 0
    angle += rotate_speed
    x_coord += x_speed
    y_coord += y_speed

    pygame.mouse.set_visible(False)
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    # --- Game logic should go here

    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.
    screen.fill(WHITE)

    # --- Drawing code should go here
    screen.blit(background_image, [0, 0])
    player_image = pygame.transform.scale(foreground_image, (width, height))
    player_image2 = pygame.transform.rotate(player_image, angle)
    screen.blit(player_image2, [x_coord, y_coord])
    if x_coord >= 725:
        x_coord = -300
    elif x_coord <= -300:
        x_coord = 725
    if y_coord >= 550:
        y_coord = -250
    elif y_coord <= -250:
        y_coord = 550
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
