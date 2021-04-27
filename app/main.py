import pygame
from model.player import Player

pygame.init()

size = width, height = 800, 600
speed = 10
black = 0, 0, 0

timer = pygame.time.Clock()

screen = pygame.display.set_mode(size)

bob = pygame.image.load("resources/bob.png")
bob_rect = bob.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_d and bob_rect.right <= width:
        #         bob_rect = bob_rect.move(speed, 0)
        #     if event.key == pygame.K_q and bob_rect.left >= 0:
        #         bob_rect = bob_rect.move(-speed, 0)
        #     if event.key == pygame.K_z and bob_rect.top >= 0:
        #         bob_rect = bob_rect.move(0, -speed)
        #     if event.key == pygame.K_s and bob_rect.bottom <= height:
        #         bob_rect = bob_rect.move(0, speed)

    timer.tick(30)

    keys_pressed = pygame.key.get_pressed()
    x_speed = (keys_pressed[pygame.K_d] - keys_pressed[pygame.K_q]) * speed
    y_speed = (keys_pressed[pygame.K_s] - keys_pressed[pygame.K_z]) * speed
    bob_rect = bob_rect.move(x_speed, y_speed)

    screen.fill(black)
    screen.blit(bob, bob_rect)
    pygame.display.flip()