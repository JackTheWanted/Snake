import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
BROWN = (139, 69, 19)
CYAN = (127, 255, 255)
GRAY = (105, 105, 105)
YELLOW = (255, 255, 153)
ORANGE = (255, 165, 0)
DARK_GREEN = (0, 100, 0)
font = pygame.font.Font('freesansbold.ttf', 30)
shooting = False
x_speed = 0
y_speed = 0
control = True
screen = pygame.display.set_mode([1000, 800])

score = 0
player_image = pygame.image.load('ship_static.png').convert()
player_image.set_colorkey(MAGENTA)

enemy_image = pygame.image.load('enemy1.png').convert()
enemy_image.set_colorkey(MAGENTA)

background_image = pygame.image.load('background.png').convert()

done = False


class Bullet:
    def __init__(self, screen, x, y, bullet_speed):
        self.image = pygame.Surface([8, 8])
        self.rect = pygame.Rect(x, y, 8, 8)
        self.bullet_speed = bullet_speed
        self.screen = screen
        self.player_bullet = pygame.image.load('ship_bullet.png').convert()
        self.player_bullet.set_colorkey(MAGENTA)

    def move(self):
        self.rect.y += self.bullet_speed

    def draw(self):
        screen.blit(self.player_bullet, (self.rect.x, self.rect.y))


class Enemy:
    def __init__(self, screen, x, y, width, height):
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(450, 50, width, height)
        self.screen = screen
        self.x_speed = 0
        self.bullets = []
        self.health = 20

    def move(self):
        self.rect.x += self.x_speed
        if player.rect.x > self.rect.x:
            self.x_speed = 2
        elif player.rect.x < self.rect.x:
            self.x_speed = -2
        else:
            self.x_speed = 0

        if self.health == 0:
            self.respawn()

        for i in range(player.rect.x, player.rect.x + 100):
            if self.rect.x + self.rect.width / 2 == i:
                self.shoot()

        #moving bullets and bullets colliding
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.y > 800:
                self.bullets.remove(bullet)
            elif bullet.rect.colliderect(player.rect):
                player.health -= 1
                self.bullets.remove(bullet)
            elif bullet.rect.collidelistall(player.bullets):
                self.bullets.remove(bullet)

    def draw(self):
        screen.blit(enemy_image, self.rect)
        for bullet in self.bullets:
            bullet.draw()

    def respawn(self):
        self.rect.y = 500

    def shoot(self):
        self.bullets.append(Bullet(self.screen, self.rect.x + self.rect.width/2 - 4, self.rect.y + 70, 2))

class Player:
    def __init__(self, screen, x, y, width, height):
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(450, 700, width, height)
        self.screen = screen
        self.x_speed = 0
        self.y_speed = 0
        self.bullets = []
        self.player_moving = pygame.image.load('ship_mobile.png').convert()
        self.player_moving.set_colorkey(MAGENTA)
        self.player_stopped = pygame.image.load('ship_static.png').convert()
        self.player_stopped.set_colorkey(MAGENTA)
        self.health = 50

    def move(self):
        if self.rect.x + self.x_speed < 0:
            self.rect.x = 0
        elif self.rect.x + self.rect.width + self.x_speed > 1000:
            self.rect.x = 1000 - self.rect.width
        else:
            self.rect.move_ip(self.x_speed, self.y_speed)

        if self.rect.y + self.y_speed < 0:
            self.rect.y = 0
        elif self.rect.y + self.rect.height + self.y_speed > 800:
            self.rect.y = 800 - self.rect.height
        else:
            self.rect.move_ip(self.x_speed, self.y_speed)

        #move bullets
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
            elif bullet.rect.colliderect(enemy.rect):
                enemy.health -= 1
                self.bullets.remove(bullet)
            elif bullet.rect.collidelistall(enemy.bullets):
                self.bullets.remove(bullet)

        #collision
        if self.rect.colliderect(enemy.rect):
            self.health -= 5


        if self.health <= 0:
           print('dead')


    def boost(self):
        if self.x_speed > 0:
            self.rect.x += 30
        elif self.x_speed < 0:
            self.rect.x -= 30
        elif self.y_speed < 0:
            self.rect.y -= 30
        elif self.y_speed > 0:
            self.rect.y += 30

    def draw(self):
        player_image = self.player_stopped
        if self.x_speed != 0 or self.y_speed != 0:
            player_image = self.player_moving
        screen.blit(player_image, self.rect)

        #draw bullets
        for bullet in self.bullets:
            bullet.draw()

    def shoot(self):
        self.bullets.append(Bullet(self.screen, self.rect.x - 4, self.rect.y + 50, -10 ))
        self.bullets.append(Bullet(self.screen, self.rect.x + self.rect.width - 4, self.rect.y + 50, -10))


bullet = Bullet(8, 8, 8, -3)
enemy = Enemy(screen, 500, 150, 90, 78)
player = Player(screen, 410, 700, 90, 103)


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


pygame.display.set_caption('Space_Shooter')


clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_speed = -3
            elif event.key == pygame.K_RIGHT:
                player.x_speed = 3
            elif event.key == pygame.K_UP:
                player.y_speed = -3
            elif event.key == pygame.K_DOWN:
                player.y_speed = 3
            elif event.key == pygame.K_SPACE:
                player.shoot()
            elif event.key == pygame.K_f:
                player.boost()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.y_speed = 0
            elif event.key == pygame.K_SPACE:
                shooting = False

    screen.fill(BLACK)
    screen.blit(background_image, [0, 0])

    enemy.draw()
    enemy.move()


    player.draw()
    player.move()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()