
#Jack C
import pygame
import random
import time
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
x_speed = 0
y_speed = 0
lvl_timer = 0
level = 0

control = True
screen = pygame.display.set_mode([1000, 800])

score = 0

shoot_sound = pygame.mixer.Sound('shoot_sound.ogg')
player_explosion_sound = pygame.mixer.Sound('player_explosion.ogg')
enemy_explosion_sound = pygame.mixer.Sound('enemy_explosion.ogg')


level_one = pygame.image.load('level_one.png').convert()
level_two = pygame.image.load('level_two.png').convert()
level_three = pygame.image.load('level_three.png').convert()

title_screen = pygame.image.load('title_screen.png').convert()
title_screen.set_colorkey(MAGENTA)
story = pygame.image.load('story.png')

shooter_one = pygame.image.load('shooter1.png').convert()
shooter_one.set_colorkey(MAGENTA)
shooter_two = pygame.image.load('shooter2.png').convert()
shooter_two.set_colorkey(MAGENTA)
shooter_three = pygame.image.load('shooter3.png').convert()
shooter_three.set_colorkey(MAGENTA)

enemy_one = pygame.image.load('enemy1.png').convert()
enemy_one.set_colorkey(MAGENTA)
enemy_two = pygame.image.load('enemy2.png').convert()
enemy_two.set_colorkey(MAGENTA)
enemy_three = pygame.image.load('enemy3.png').convert()
enemy_three.set_colorkey(MAGENTA)

done = False


level_list = [level_one, level_two, level_three]
level_music_list = [('level1_music.wav'), ('level2_music.wav'), ('level3_music.wav')]
shooter_list = [shooter_one, shooter_two, shooter_three]
enemy_list = [enemy_one, enemy_two, enemy_three]

class Bullet:
    def __init__(self, screen, x, y, bullet_speed):
        self.image = pygame.Surface([8, 8])
        self.rect = pygame.Rect(x, y, 8, 8)
        self.bullet_speed = bullet_speed
        self.screen = screen
        self.player_bullet = pygame.image.load('ship_bullet.png').convert()
        self.player_bullet.set_colorkey(MAGENTA)
        self.enemy_bullet = pygame.image.load('enemy_bullet.png').convert()
        self.enemy_bullet.set_colorkey(MAGENTA)


    def move(self):
        self.rect.y += self.bullet_speed

    def draw(self):
        screen.blit(self.player_bullet, (self.rect.x, self.rect.y))

    def draw2(self):
        screen.blit(self.enemy_bullet, (self.rect.x, self.rect.y))


class Enemy:
    def __init__(self, screen, x, y, width, height):
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(450, -50, width, height)
        self.screen = screen
        self.x_speed = 0
        self.y_speed = 0
        self.bullets = []
        self.health = 20
        self.timer = 0
        self.dead = 0
        self.bullet_timer = 0
        self.cooldown = 30
        self.speed_multiplier = 1

    def move(self):
        if player.health > 0:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            if self.rect.y >= 100:
                if player.rect.x > self.rect.x:
                    self.x_speed = 2*self.speed_multiplier
                elif player.rect.x < self.rect.x:
                    self.x_speed = -2*self.speed_multiplier
                else:
                    self.x_speed = 0

        if self.rect.y < 100:
            self.y_speed = 5
        elif self.rect.y >= 100:
            self.y_speed = 0

            if self.health > 0 and player.health > 0:
                for i in range(player.rect.x, player.rect.x + 100):
                    if self.rect.x + self.rect.width / 2 == i:
                        self.shoot()

        #moving bullets and bullets colliding
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.y > 800:
                self.bullets.remove(bullet)
            elif bullet.rect.colliderect(player.rect):
                player.health -= 3 + self.dead
                self.bullets.remove(bullet)
            elif bullet.rect.collidelistall(player.bullets):
                self.bullets.remove(bullet)

    def draw(self):
        if self.health > 0:
            screen.blit(enemy_list[level], self.rect)

        if self.health <= 0:
            self.timer += 1
            self.x_speed = 0
            if 0 <= self.timer <= 15:
                enemy_explosion_sound.play()
                enemy_image = pygame.image.load('explosion1.png').convert()
                enemy_image.set_colorkey(MAGENTA)
                screen.blit(enemy_image, self.rect)
            elif 13 <= self.timer <= 30:
                enemy_image =  pygame.image.load('explosion2.png').convert()
                enemy_image.set_colorkey(MAGENTA)
                screen.blit(enemy_image, self.rect)
            elif 30 <= self.timer  <= 45:
                enemy_image = pygame.image.load('explosion3.png').convert()
                enemy_image.set_colorkey(MAGENTA)
                screen.blit(enemy_image, self.rect)
            elif 45 <= self.timer <= 60:
                enemy_image = pygame.image.load('explosion4.png').convert()
                enemy_image.set_colorkey(MAGENTA)
                screen.blit(enemy_image, self.rect)
            elif 60 <= self.timer <= 75:
                enemy_image = pygame.image.load('explosion5.png').convert()
                enemy_image.set_colorkey(MAGENTA)
                screen.blit(enemy_image, self.rect)
            elif self.timer > 200:
                self.respawn()

        for bullet in self.bullets:
            bullet.draw2()

    def respawn(self):
        if player.health > 0:
            self.timer = 0
            self.dead += 1
            self.speed_multiplier += .2
            self.health = 20
            self.cooldown = 30 - self.dead *5
            if self.cooldown <= 10:
                self.cooldown = 10
            if self.speed_multiplier > 1.8:
                self.speed_multiplier = 1.8
            self.rect.x = random.randrange(100, 900)
            self.rect.y = -50
            screen.blit(enemy_list[level], self.rect)

    def shoot(self):
        self.bullet_timer += 1
        if self.bullet_timer > self.cooldown:
            shoot_sound.play()
            self.bullets.append(Bullet(self.screen, self.rect.x + self.rect.width/2 - 4, self.rect.y + 70, 10))
            self.bullet_timer = 0


class Shooter(Enemy):
    def __init__(self, screen, width, height):
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(450, -30, width, height)
        self.screen = screen
        self.x_speed = 3
        self.y_speed = 0
        self.bullets = []
        self.health = 10
        self.timer = 0
        self.dead = 0
        self.cooldown = 0
        self.shoot_timer = 0
        self.speed_multiplier = 1

    def move(self):
        if player.health > 0 and enemy.dead > 0:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            if self.rect.x >= 950 or self.rect.x <= 0:
                self.x_speed *= -1

            if self.rect.y < 30:
                self.y_speed = 5
            elif self.rect.y >= 30:
                self.y_speed = 0

        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.y > 800:
                self.bullets.remove(bullet)
            elif bullet.rect.colliderect(player.rect):
                player.health -= 8 + self.dead*2
                self.bullets.remove(bullet)
            elif bullet.rect.collidelistall(player.bullets):
                self.bullets.remove(bullet)

    def draw(self):
        if enemy.dead > 0:
            if self.health > 0:
                screen.blit(shooter_list[level], self.rect)

        #explosion
        if self.health <= 0:
            self.timer += 1
            self.x_speed = 0
            if 0 <= self.timer <= 15:
                enemy_explosion_sound.play()
                shooter_image = pygame.image.load('explosion1.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif 15 <= self.timer <= 30:
                shooter_image =  pygame.image.load('explosion2.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif 30 <= self.timer  <= 45:
                shooter_image = pygame.image.load('explosion3.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif 45 <= self.timer <= 60:
                shooter_image = pygame.image.load('explosion4.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif 60 <= self.timer <= 75:
                shooter_image = pygame.image.load('explosion5.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif self.timer > 200:
                self.respawn()

        for bullet in self.bullets:
            bullet.draw2()

    def shoot(self):
        self.shoot_timer += 1
        self.cooldown = random.randrange(0, 2000 - self.dead * 400)
        if self.health >= 0 and enemy.dead > 0 and player.health > 0:
            if self.shoot_timer > self.cooldown:
                shoot_sound.play()
                self.bullets.append(Bullet(self.screen, self.rect.x + self.rect.width / 2 - 4, self.rect.y + 70, 2))
                self.shoot_timer = 0

    def respawn(self):
        if player.health > 0:
            self.timer = 0
            self.dead += 1
            self.speed_multiplier += .2
            self.health = 10 + self.dead*5
            self.x_speed = 3
            self.rect.x = random.randrange(100, 900)
            self.rect.y = -30
            screen.blit(shooter_list[level], self.rect)


class Bomber(Enemy):
    def __init__(self, screen, width, height):
        self.image = pygame.Surface([width, height])
        self.rect = pygame.Rect(450, 500, width, height)
        self.screen = screen
        self.x_speed = 3
        self.y_speed = 3
        self.health = 10
        self.timer = 0
        self.invtimer = 0

    def move(self):
        if player.health > 0 and self.health > 0:
            self.rect.x += self.x_speed
            self.rect.y += self.y_speed
            if self.rect.x >= 980:
                self.x_speed = random.randrange(1, 10)
                self.x_speed *= -1
            elif self.rect.x <= 0:
                self.x_speed = random.randrange(1, 10)
            elif self.rect.y >= 780:
                self.y_speed = random.randrange(1, 10)
                self.y_speed *= -1
            elif self.rect.y <= 0:
                self.y_speed = random.randrange(1, 10)

        if self.rect.colliderect(player.rect):
            if enemy.dead > 2 or shooter.dead > 1:
                if self.invtimer > 50:
                    self.health = 0
                    player.health = 0

    def draw(self):
        if enemy.dead > 2 or shooter.dead > 1:
            self.invtimer += 1
            if self.health > 0:
                bomber_image = pygame.image.load('bomber.png').convert()
                bomber_image.set_colorkey(MAGENTA)
                screen.blit(bomber_image, self.rect)

        #explosion
        if self.health <= 0:
            self.timer += 1
            self.x_speed = 0
            enemy_explosion_sound.play()
            if 0 <= self.timer <= 15:
                shooter_image = pygame.image.load('explosion1a.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif 15 <= self.timer <= 30:
                shooter_image =  pygame.image.load('explosion2a.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif 30 <= self.timer  <= 45:
                shooter_image = pygame.image.load('explosion3a.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif 45 <= self.timer <= 60:
                shooter_image = pygame.image.load('explosion4a.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)
            elif 60 <= self.timer <= 75:
                shooter_image = pygame.image.load('explosion5a.png').convert()
                shooter_image.set_colorkey(MAGENTA)
                screen.blit(shooter_image, self.rect)


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
        self.health = 100
        self.timer = 0
        self.score = 0


    def move(self):
        if player.health > 0:
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
            elif bullet.rect.colliderect(shooter.rect) and shooter.rect.y >= 30:
                shooter.health -= 1
                if shooter.health > 0:
                    self.bullets.remove(bullet)
                elif shooter.health == 0:
                    self.score += 1

            elif bullet.rect.colliderect(enemy.rect):
                enemy.health -= 1
                if enemy.health > 0:
                    self.bullets.remove(bullet)

        if enemy.health < 0 and enemy.timer == 100:
            self.score += 1
        elif shooter.health < 0 and shooter.timer == 100:
            self.score += 1

        #collision
        if self.rect.colliderect(enemy.rect):
            self.health -= 5

    def draw(self):
        if self.health > 0:
            player_image = self.player_stopped
            if self.x_speed != 0 or self.y_speed != 0:
                player_image = self.player_moving
            screen.blit(player_image, self.rect)

            pygame.draw.rect(screen, RED, (5, 5, 100, 20))
            pygame.draw.rect(screen, GREEN, (5, 5, self.health, 20))
        #draw bullets
            for bullet in self.bullets:
                bullet.draw()


        if self.health <= 0:
            self.timer += 1
            self.x_speed = 0
            if self.timer >= 10 and self.timer < 20:
                player_explosion_sound.play()
                player_image = pygame.image.load('explosion1.png').convert()
                player_image.set_colorkey(MAGENTA)
                screen.blit(player_image, self.rect)
            elif self.timer >= 20 and self.timer <= 30:
                player_image = pygame.image.load('explosion2.png').convert()
                player_image.set_colorkey(MAGENTA)
                screen.blit(player_image, self.rect)
            elif self.timer >= 30 and self.timer <= 40:
                player_image = pygame.image.load('explosion3.png').convert()
                player_image.set_colorkey(MAGENTA)
                screen.blit(player_image, self.rect)
            elif self.timer >= 40 and self.timer <= 50:
                player_image = pygame.image.load('explosion4.png').convert()
                player_image.set_colorkey(MAGENTA)
                screen.blit(player_image, self.rect)
            elif self.timer >= 50 and self.timer <= 60:
                player_image = pygame.image.load('explosion5.png').convert()
                player_image.set_colorkey(MAGENTA)
                screen.blit(player_image, self.rect)
            elif self.timer >= 100:
                screen.fill(BLACK)
                end_image = pygame.image.load('end_screen.png').convert()
                end_image.set_colorkey(MAGENTA)
                screen.blit(end_image, (0, -50))


    def shoot(self):
        if self.health > 0:
            shoot_sound.play()
            self.bullets.append(Bullet(self.screen, self.rect.x - 4, self.rect.y + 50, -10 ))
            self.bullets.append(Bullet(self.screen, self.rect.x + self.rect.width - 4, self.rect.y + 50, -10))


bullet = Bullet(8, 8, 8, -3)
enemy = Enemy(screen, 500, 150, 90, 78)
shooter = Shooter(score, 90, 78)
player = Player(screen, 410, 700, 90, 103)
bomber = Bomber(screen, 25, 25)


def level_up(screen, player, enemy, shooter, bomber, level):
    if player.score == 5 and level == 0 or player.score == 10 and level == 1:
        done = False
        clock = pygame.time.Clock()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.blit(level_list[level], [0, 0])
            player_image = player.player_stopped
            if player.x_speed != 0 or player.y_speed != 0:
                player_image = player.player_moving
            screen.blit(player_image, player.rect)

            pygame.draw.rect(screen, RED, (5, 5, 100, 20))
            pygame.draw.rect(screen, GREEN, (5, 5, player.health, 20))

            player.x_speed = 0
            player.rect.move_ip((0, player.y_speed))
            player.y_speed = -10
            clock.tick(60)
            if player.rect.y < -30:
                done = True

            pygame.display.update()

        player.y_speed = 0
        player.rect.y = 750
        player.health = 100
        enemy.health = 0
        shooter.health = 0
        bomber.invtimer = 0
        return level + 1

    return level


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


screen.fill(BLACK)
screen.blit(title_screen, (100, 0))
pygame.display.update()
wait()
screen.blit(story, (0, 0))
pygame.display.update()
wait()



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
                player.score = 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.y_speed = 0


    screen.blit(level_list[level], [0, 0])



    enemy.draw()
    enemy.move()

    shooter.draw()
    shooter.move()
    shooter.shoot()

    if enemy.dead > 0:
        bomber.draw()
        bomber.move()

    player.draw()
    player.move()

    old_level = level
    level = level_up(screen, player, enemy, shooter, bomber, level)
    if old_level != level:
        pygame.mixer.music.load(level_music_list[level])
        pygame.mixer.music.play(-1, 0)
    pygame.display.flip()


    clock.tick(60)

pygame.quit()