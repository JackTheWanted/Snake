import pygame, sys, time, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()
catches = 0
timer = 0
# set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('PCI Football')

# set up the colors
WHITE = (255,255,255)
BLACK = (0, 0, 0)
# set up the block data structure
player = pygame.Rect(20, 20, 40, 60)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 60))
ball= pygame.Rect(300, 30, 25, 20)
ballImage = pygame.image.load('football.png')
ballStretchedImage = pygame.transform.scale(ballImage, (25, 20))

fontObj = pygame.font.Font('freesansbold.ttf', 16)
textSurfaceObj = fontObj.render(str(catches), True, BLACK, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (50, 20)

# set up keyboard variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# set up music
applauseSound = pygame.mixer.Sound('Munch.wav')
pygame.mixer.music.load('Pizza Song.ogg')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True
start_time = time.time()
# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying
        
    # draw the black background onto the surface
    windowSurface.fill(WHITE)
    time_passed = time.time() - start_time
    # move the player

    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED


    # draw the block onto the surface
    windowSurface.blit(playerStretchedImage, player)
    windowSurface.blit(ballStretchedImage, ball)
    print("time elapsed: {:.2f}s".format(time.time() - start_time))
    # check if the block has intersected with any food squares.
    if time_passed >= 20:
        pygame.quit()
        sys.exit()
    if player.colliderect(ball):
        catches += 1
        if catches >= 6:
            pygame.mixer.music.stop()
            pygame.mixer.music.play(-1, 0.0)
        if musicPlaying:
            applauseSound.play()
            ball.top=random.randint(0, WINDOWHEIGHT - ball.height)
            ball.left=random.randint(0, WINDOWWIDTH - ball.width)
    textSurfaceObj = fontObj.render(str(catches), True, BLACK, WHITE)
    windowSurface.blit(textSurfaceObj, textRectObj)
    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
