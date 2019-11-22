import pygame, sys, time, random
from pygame.locals import *

pygame.init()

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
font = pygame.font.Font('freesansbold.ttf', 30)
x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 10
score = 0
done = False
screen = pygame.display.set_mode([700, 500])



class Food(pygame.sprite.Sprite):
    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.x = random.randrange(10, 690)
        self.rect.y = random.randrange(10, 490)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y


    def restart(self):
        self.rect.x = 10
        self.rect.y = 10


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # pressing escape quits
                    pygame.quit()
                return

def drawText(text, font, surface, x, y, clr):
    textobj = font.render(text, 1, clr)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Set the title of the window
pygame.display.set_caption('Snake')

# List to hold all the sprites
all_sprites_list = pygame.sprite.Group()

segment_list = []
wall_list = pygame.sprite.Group()
food_list = pygame.sprite.Group()

snake = Snake(x_coord, y_coord, 10, 10)
snake.rect.x = x_coord + x_speed
snake.rect.y = y_coord + y_speed
segment_list.append(snake)
all_sprites_list.add(snake)


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


drawText('It\'s snake time!', font, screen, 250, 170, BLUE)
drawText('Press any key to start.', font, screen, 210, 270, BLUE)
pygame.display.update()
waitForPlayerToPressKey()

clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -2
                y_speed = 0
            elif event.key == pygame.K_RIGHT:
                x_speed = 2
                y_speed = 0
            elif event.key == pygame.K_UP:
                y_speed = -2
                x_speed = 0
            elif event.key == pygame.K_DOWN:
                y_speed = 2
                x_speed = 0

    snake.rect.x += x_speed
    snake.rect.y += y_speed
    # Clear the screen
    screen.fill(BLACK)
    drawText(str(score), font, screen, 10, 10, BLUE)
    # Check the list of collisions.
    if pygame.sprite.spritecollide(snake, wall_list, False):
        drawText('You lost!', font, screen, 270, 170, BLUE)
        drawText('Press any key to start again.', font, screen, 150, 270, BLUE)
        pygame.display.update()
        waitForPlayerToPressKey()
        score = 0
        x_speed = 0
        y_speed = 0
        snake.restart()

    food_hit_list = pygame.sprite.spritecollide(snake, food_list, False)
    for food in food_hit_list:
        score += 1
        food.reset_pos()

        #moving right
        if x_speed > 0:
            segment_list.append(snake)
        #moving left
        if x_speed < 0:
            segment_list.append(snake)
        #moving up
        if y_speed < 0:
            segment_list.append(snake)
        #moving down
        if y_speed > 0:
            segment_list.append(snake)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)


pygame.quit()