import pygame
from model.player import Player

pygame.init()

size = width, height = 800, 600
speed = 2
black = 0, 0, 0

screen = pygame.display.set_mode(size)

bob = pygame.image.load("resources/bob.png")
bob_rect = bob.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                bob_rect = bob_rect.move(10, 0)
            if event.key == pygame.K_q:
                bob_rect = bob_rect.move(-10, 0)
            if event.key == pygame.K_z:
                bob_rect = bob_rect.move(0, -10)
            if event.key == pygame.K_s:
                bob_rect = bob_rect.move(0, 10)

    screen.fill(black)
    screen.blit(bob, bob_rect)
    pygame.display.flip()