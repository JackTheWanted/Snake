import pygame
import random
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
screen = pygame.display.set_mode([700, 500])
class Food(pygame.sprite.Sprite):
    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(10, 690)
        self.rect.x = random.randrange(10, 490)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


# Set the title of the window
pygame.display.set_caption('Walls')

# List to hold all the sprites
all_sprites_list = pygame.sprite.Group()

# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
food_list = pygame.sprite.Group()

food = Food(WHITE, 10, 10)
food.rect.x = random.randint(10, 690)
food.rect.y = random.randint(10, 490)
food_list.add(food)
all_sprites_list.add(food)


wall = Wall(0, 0, 0, 500)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(0, 0, 700, 0)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(0, 500, 700, 500)
wall_list.add(wall)
all_sprites_list.add(wall)

wall = Wall(700, 10, 700, 490)
wall_list.add(wall)
all_sprites_list.add(wall)

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
    food_hit_list = pygame.sprite.spritecollide(wall, food_list, True)
    for food in food_hit_list:
         food.reset_pos()

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)


pygame.quit()