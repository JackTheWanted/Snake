import pygame
import random
size = (700, 500)
screen = pygame.display.set_mode(size)
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Rectangle():
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.change_x = 0
        self.change_y = 0
        self.r = 0
        self.g = 0
        self.b = 0
        self.colour = [self.r, self.g, self.b]
        self.screen = screen
    def draw(self):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])
    def move(self):
        self.x += self.change_x
        self.y += self.change_y


class Ellipse(Rectangle):
    def __init__(self, screen):
        super().__init__(screen)

    def draw(self):
        pygame.draw.ellipse(screen, self.colour, [self.x, self.y, self.width, self.height])


my_list = []
for i in range(2000):
    if random.randint(0,1):
        my_object = Ellipse(screen)
    else:
        my_object = Rectangle(screen)

    my_object.x = random.randint(0, 701)
    my_object.y = random.randint(0, 501)
    my_object.width = random.randint(20, 70)
    my_object.height = random.randint(20, 70)
    my_object.change_x = random.randint(-3, 3)
    my_object.change_y = random.randint(-3, 3)
    my_object.r = random.randrange(0, 255)
    my_object.g = random.randrange(0, 255)
    my_object.b = random.randrange(0, 255)
    my_object.colour = [my_object.r, my_object.g, my_object.b]
    my_list.append(my_object)



pygame.init()

# Set the width and height of the screen [width, height]


pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    for my_object in my_list:
        my_object.draw()
        my_object.move()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()