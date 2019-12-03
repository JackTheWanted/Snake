import pygame, random



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
        self.body = []
        self.body.append(self.rect)
        self.RGB = [255, 0, 0]
        self.is_RGB = False

    def draw(self):
        if self.is_RGB:
            if self.RGB[0] > 0 and self.RGB[2] == 0:
                self.RGB[0] -= 25.5
                self.RGB[1] += 25.5
            elif self.RGB[1] > 0 and self.RGB[0] == 0:
                self.RGB[1] -= 25.5
                self.RGB[2] += 25.5
            elif self.RGB[2] > 0 and self.RGB[1] == 0:
                self.RGB[0] += 25.5
                self.RGB[2] -= 25.5
            self.colour = self.RGB

        for self.segment in self.body:
            pygame.draw.rect(screen, self.colour, self.segment)

    def move(self):
        done = False
        if len(self.body) > 1:
            segment = self.body.pop(len(self.body) - 1)
            self.body.insert(0, segment)
            self.body[0] = self.body[1].move(self.x_speed, self.y_speed)


            if self.body[0].collidelist(self.body[1:]) != -1:
                done = lose()
                self.x_speed = 0
                self.y_speed = 0

        else:
            self.body[0].move_ip(self.x_speed, self.y_speed)

        if self.body[0].x > 700 or self.body[0].x < -10:
            done = lose()
            self.x_speed = 0
        elif self.body[0].y > 500 or self.body[0].y < -10:
            done = lose()
            self.y_speed = 0

        if pygame.Rect(self.body[0]).colliderect(food.rect):
            self.score += 1

            self.grow()
            food.reset_pos()

        return done

    def restart(self):
        for i in range(snake.score):
            self.body.pop(0)
        self.score = 0
        snake.is_RGB = False
        self.colour = GREEN
        self.body[0].x = 30
        self.body[0].y = 30


    def grow(self):
        self.draw()
        self.body.insert(0, pygame.Rect(self.body[0].x, self.body[0].y, self.body[0].width, self.body[0].height))



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
    draw_text('You lost!', font, screen, 270, 170, snake.colour)
    draw_text('Press any key to start again.', font, screen, 150, 270, snake.colour)
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snake.x_speed != 20:
                    snake.x_speed = -20
                    snake.y_speed = 0
            elif event.key == pygame.K_RIGHT:
                if snake.x_speed != -20:
                    snake.x_speed = 20
                    snake.y_speed = 0
            elif event.key == pygame.K_UP:
                if snake.y_speed != 20:
                    snake.y_speed = -20
                    snake.x_speed = 0
            elif event.key == pygame.K_DOWN:
                if snake.y_speed != -20:
                    snake.y_speed = 20
                    snake.x_speed = 0
            elif event.key == pygame.K_f:
                snake.is_RGB = True
    # Clear the screen
    screen.fill(BLACK)
    draw_text(str(snake.score), font, screen, 10, 10, snake.colour)

    if snake.score >= 10:
        snake.colour = BLUE
    if snake.score >= 20:
        snake.colour = ORANGE
    if snake.score >= 30:
        snake.colour = RED
    if snake.score >= 40:
        snake.is_RGB = True


    # Draw all the spites
    snake.draw()
    done = snake.move()
    food.draw()

    # Go ahead and update the screen with what we've drawn.

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(10)


pygame.quit()