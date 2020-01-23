import pygame
pygame.init()
shoot_sound = pygame.mixer.Sound('shoot_sound.ogg')
enemy_explosion_sound = pygame.mixer.Sound('level1_music.wav')
enemy_explosion_sound.play()
shoot_sound.play()
while True:
    print("gg")