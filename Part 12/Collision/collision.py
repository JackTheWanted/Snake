import pygame, sys, time, random
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 500
WHITE = (255,255,255)

pygame.init()
mainClock = pygame.time.Clock()
applauseSound = pygame.mixer.Sound('Munch.wav')  #set up applause Sound

# set up the window
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Simple Collision Example--ESC to Quit')

# set up the block data structure
tobey_rect = pygame.Rect(50, 50, 100, 60)
tobey_image = pygame.image.load('tobey.png')
tobey_stretched_image = pygame.transform.scale(tobey_image, (90, 60))
pizza_rect= pygame.Rect(300, 250, 65, 50)
pizza_image = pygame.image.load('pizza.png')
pizza_stretched_image = pygame.transform.scale(pizza_image, (70, 60))

pygame.mouse.set_pos(tobey_rect.centerx, tobey_rect.centery)  # place mouse at Stampie's location

# play the game
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        # move Stampie to follow the mouse cursor
        if event.type == MOUSEMOTION:      
                tobey_rect.move_ip(event.pos[0]-tobey_rect.centerx, event.pos[1]-tobey_rect.centery)
    pygame.mouse.set_visible(False)
    windowSurface.fill(WHITE)
 
    windowSurface.blit(pizza_stretched_image, pizza_rect)
    windowSurface.blit(tobey_stretched_image, tobey_rect)
    
    if tobey_rect.colliderect(pizza_rect):  #Stampie collides with Ram
        applauseSound.play()
        pizza_rect.top = random.randint(0, WINDOWHEIGHT - pizza_rect.height)
        pizza_rect.left = random.randint(0, WINDOWWIDTH - pizza_rect.width)
      
                                   
    pygame.display.update()
    mainClock.tick(40)
