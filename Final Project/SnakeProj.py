import pygame, random



pygame.init()
r = 0
g = 0
b = 0

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
score = 0
done = False
screen = pygame.display.set_mode([700, 500])

class Food():
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = pygame.Rect(x, y, width, height)
        self.colour = WHITE
        self.rect.x = random.randint(30, 670)
        self.rect.y = random.randint(30, 470)

    def draw(self):
        pygame.draw.rect(screen, self.colour, self.rect)

    def reset_pos(self):
        self.rect.x = random.randrange(30, 670)
        self.rect.y = random.randrange(30, 470)



class Snake():
    def __init__(self, x, y, width, height, food):
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(x, y, width, height)
        self.colour = GREEN
        self.food = food
        self.x_speed = 0
        self.y_speed = 0
        self.score = 0
        self.multiplier = 1
        self.body = []
        self.body.append(self.rect)

    def draw(self):
     for self.segment in self.body:
        pygame.draw.rect(screen, self.colour, self.segment)

    def move(self):
        done = False
        if len(self.body) > 1:
            segment = self.body.pop(len(self.body) - 1)
            self.body.insert(0, segment)
            self.body[0] = self.body[1].move(self.body[1].width, self.body)

        else:
            self.body[0].move_ip(self.x_speed, self.y_speed)

        if self.body[0].x > 680 or self.body[0].x < 0:
            done = lose()
            self.x_speed = 0
        elif self.body[0].y > 480 or self.body[0].y < 0:
            done = lose()
            self.y_speed = 0

        if pygame.Rect(self.body[0]).colliderect(food.rect):
            self.score += 1
            self.grow()
            food.reset_pos()

        return done

    def restart(self):
        if len(self.body) > 1:
            for self.segment in self.body:
                self.body.pop(0)
        self.score = 0
        self.colour = GREEN
        self.multiplier = 1
        self.body[0].x = 30
        self.body[0].y = 30


    def grow(self):
        if self.x_speed > 0:
            self.body.insert(0, pygame.Rect(self.body[0].x, self.body[0].y, self.body[0].width, self.body[0].height))
        if self.x_



def wait():
    done = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # pressing escape quits
                    return True
                return False

def draw_text(text, font, surface, x, y, clr):
    textobj = font.render(text, 1, clr)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def lose():
    draw_text('You lost!', font, screen, 270, 170, BLUE)
    draw_text('Press any key to start again.', font, screen, 150, 270, BLUE)
    pygame.display.update()
    done = wait()
    food.reset_pos()
    snake.restart()
    snake.draw()

    return done

# Set the title of the window
pygame.display.set_caption('Snake')


food = Food(10, 10, 20, 20)
snake = Snake(30, 30, 20, 20, food)


draw_text('It\'s snake time!', font, screen, 250, 170, BLUE)
draw_text('Press any key to start.', font, screen, 210, 270, BLUE)
pygame.display.update()
done = wait()

clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    if r > 0 and b == 0:
        r -= 2.55
        g += 2.55
        RGB = (r, g, b)
    elif g > 0 and r == 0:
        g -= 2.55
        b += 2.55
        RGB = (r, g, b)
    elif b > 0 and g == 0:
        r += 2.55
        b -= 2.55
        RGB = (r, g, b)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.x_speed = -30*snake.multiplier
                snake.y_speed = 0
            elif event.key == pygame.K_RIGHT:
                snake.x_speed = 30*snake.multiplier
                snake.y_speed = 0
            elif event.key == pygame.K_UP:
                snake.y_speed = -30*snake.multiplier
                snake.x_speed = 0
            elif event.key == pygame.K_DOWN:
                snake.y_speed = 30*snake.multiplier
                snake.x_speed = 0
            elif event.key == pygame.K_f:
                snake.colour = RED

    # Clear the screen
    screen.fill(BLACK)
    draw_text(str(snake.score), font, screen, 10, 10, snake.colour)

    if snake.score >= 5:
        snake.multiplier = 1
        snake.colour = BLUE
    if snake.score >= 10:
        snake.multiplier = 1
        snake.colour = ORANGE
    if snake.score >= 15:
        snake.multiplier = 1
        snake.colour = YELLOW
    if snake.score >= 20:
        snake.multiplier = 1
        snake.colour = RED

    # Check the list of collisions.

        #moving right

        #moving left

        #moving up

        #moving down

    # Draw all the spites
    snake.draw()
    done = snake.move()
    food.draw()

    # Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(10)


pygame.quit()