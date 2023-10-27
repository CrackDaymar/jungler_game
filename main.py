import random
import pygame
from pygame.locals import QUIT
from object import GameObject

def make_objects(num_objects, HEIGHT, WIDTH):
    objects = []
    for _ in range(num_objects):
        obj = GameObject()
        obj.x = random.randint(0, WIDTH - obj.width)  # Генерируйте случайное значение x в пределах ширины поля
        obj.y = random.randint(0, HEIGHT - obj.height)  # Генерируйте случайное значение y в пределах высоты поля
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

while playing:

    FPS.tick(660)  # Устанавливаем FPS на уровне 60 кадров в секунду

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False

    main_display.fill(COLOR_BLACK)

    for obj in objects:
        pygame.draw.circle(main_display, obj.color, (obj.x, obj.y), obj.size)

    player_rect = player_rect.move(player_speed)

    if player_rect.bottom >= HEIGHT or player_rect.top <= 0:
        player_speed[1] = -player_speed[1]

    if player_rect.right >= WIDTH or player_rect.left <= 0:
        player_speed[0] = -player_speed[0]

    main_display.blit(player, player_rect)

    pygame.display.flip()

pygame.quit()