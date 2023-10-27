import random
import pygame
from pygame.locals import QUIT
from object import GameObject

def make_objects(num_objects, HEIGHT, WIDTH):
    objects = []
    for _ in range(num_objects):
        obj = GameObject()
        obj.x = random.randint(0, WIDTH - obj.width)
        obj.y = random.randint(0, HEIGHT - obj.height)
        objects.append(obj)
    return objects

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player_size = (20, 20)
player = pygame.Surface(player_size)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_speed = [1, 1]

playing = True

objects = make_objects(10, HEIGHT, WIDTH)

pass

while playing:

    FPS.tick(660)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    for obj in objects:
        obj_rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
        pygame.draw.rect(main_display, obj.color, obj_rect)

        if player_rect.colliderect(obj_rect):
            # Определите, с какой стороны произошло столкновение
            if player_rect.right >= obj_rect.left and player_speed[0] > 0:
                player_speed[0] = -player_speed[0]  # Столкновение справа
            elif player_rect.left <= obj_rect.right and player_speed[0] < 0:
                player_speed[0] = -player_speed[0]  # Столкновение слева
            elif player_rect.bottom >= obj_rect.top and player_speed[1] > 0:
                player_speed[1] = -player_speed[1]  # Столкновение снизу
            elif player_rect.top <= obj_rect.bottom and player_speed[1] < 0:
                player_speed[1] = -player_speed[1]  # Столкновение сверху

    player_rect = player_rect.move(player_speed)

    if player_rect.bottom >= HEIGHT or player_rect.top <= 0:
        player_speed[1] = -player_speed[1]

    if player_rect.right >= WIDTH or player_rect.left <= 0:
        player_speed[0] = -player_speed[0]

    main_display.blit(player, player_rect)

    pygame.display.flip()

pygame.quit()