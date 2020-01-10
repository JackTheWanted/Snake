import pygame, sys, time, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sound')
done = False
# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
food_eaten = 0
# set up the block data structure
tobey = pygame.Rect(300, 100, 50, 37)
playerImage = pygame.image.load('tobey.png').convert()
playerImage.set_colorkey(WHITE)
playerStretchedImage = pygame.transform.scale(playerImage, (50, 37))
food = pygame.Rect(300, 100, 40, 40)
foodImage = pygame.image.load('pizza.png').convert()
foodImage.set_colorkey(WHITE)
foodStretchedImage = pygame.transform.scale(foodImage, (40, 40))
foods = []
foodCounter = 0
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
fontObj = pygame.font.Font('freesansbold.ttf', 16)
textSurfaceObj = fontObj.render(str(food_eaten), True, WHITE, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (50, 20)
NEWFOOD = 40

# set up keyboard variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# set up music
pickUpSound = pygame.mixer.Sound('Munch.wav')
pygame.mixer.music.load('Pizza Song.ogg')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    sys.exit()
                return


def drawText(text, font, surface, x, y, clr):
    textobj = font.render(text, 1, clr)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

drawText('It\'s pizza time!', fontObj, windowSurface, (WINDOWWIDTH/3)+10, (WINDOWHEIGHT/3), BLUE)
drawText('Press any key to start.', fontObj, windowSurface, (WINDOWWIDTH/3)-20, (WINDOWHEIGHT/3)+ 110, BLUE)
pygame.display.update()
waitForPlayerToPressKey()

# run the game loop
while not done:
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
            if event.key == K_f:
                foods.remove(food)
            if event.key == K_g:
                foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
            if event.key == K_l:
                for i in range(20):
                    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                tobey.top = random.randint(0, WINDOWHEIGHT - tobey.height)
                tobey.left = random.randint(0, WINDOWWIDTH - tobey.width)
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    if moveDown and tobey.bottom < WINDOWHEIGHT:
        tobey.top += MOVESPEED
    if moveUp and tobey.top > 0:
        tobey.top -= MOVESPEED
    if moveLeft and tobey.left > 0:
        tobey.left -= MOVESPEED
    if moveRight and tobey.right < WINDOWWIDTH:
        tobey.right += MOVESPEED


    # draw the block onto the surface
    windowSurface.blit(playerStretchedImage, tobey)

    # check if the block has intersected with any food squares.
    for food in foods[:]:
        if tobey.colliderect(food):
            food_eaten += 1
            foods.remove(food)
            tobey = pygame.Rect(tobey.left, tobey.top, tobey.width + 4, tobey.height + 4)
            playerStretchedImage = pygame.transform.scale(playerImage, (tobey.width, tobey.height))
            if musicPlaying:
                pickUpSound.play()

    if len(foods) == 0 or food_eaten >= 40:
        done = True
        windowSurface.fill(BLACK)
        drawText('You consumed all of the pizza!', fontObj, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3), BLUE)
        drawText('Press any key to end.', fontObj, windowSurface, (WINDOWWIDTH / 3) - 20, (WINDOWHEIGHT / 3) + 110,
                 BLUE)
        pygame.display.update()
        waitForPlayerToPressKey()
        sys.exit()


    textSurfaceObj = fontObj.render(str(food_eaten), True, WHITE, BLACK)
    windowSurface.blit(textSurfaceObj, textRectObj)
    # move the tobey
    for food in foods:
        windowSurface.blit(foodStretchedImage, food)

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
