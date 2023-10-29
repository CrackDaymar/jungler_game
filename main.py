import random
import os
import pygame
from pygame.locals import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from setting import HEIGHT, WIDTH, COLOR_WHITE, COLOR_BLACK, COLOR_BLUE, COLOR_GREEN, IMAGE_PATH
from object import Player, Enemies, Bonus

PLAYER_IMAGES = os.listdir(IMAGE_PATH)

bg = pygame.transform.scale(pygame.image.load('image/background.png'), (WIDTH, HEIGHT))
bg_x1 = 0
bg_x2 = bg.get_width()
bg_move = 3

pygame.init()

FPS = pygame.time.Clock()

FONT = pygame.font.SysFont('Verdana', 20)


main_display = pygame.display.set_mode((WIDTH, HEIGHT))

playing = True

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 2000)
CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

image_index = 0

enemies = [Enemies(WIDTH, HEIGHT, COLOR_WHITE)]
bonuses = [Bonus(WIDTH, HEIGHT)]
player = Player(COLOR_BLACK)


while playing:

    FPS.tick(660)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            warrior = Enemies(WIDTH, HEIGHT, COLOR_WHITE)
            enemies.append(warrior)
        if event.type == CREATE_BONUS:
            bonus = Bonus(WIDTH, HEIGHT)
            bonuses.append(bonus)
        if event.type == CHANGE_IMAGE:
            player.player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    bg_x1 -= bg_move
    bg_x2 -= bg_move

    if bg_x1 < -bg.get_width():
        bg_x1 = bg.get_width()

    if bg_x2 < -bg.get_width():
        bg_x2 = bg.get_width()

    main_display.blit(bg, (bg_x1, 0))
    main_display.blit(bg, (bg_x2, 0))

    for bonus_point in bonuses:
        bonus_point.move_bonuses()
        main_display.blit(bonus_point.bonus, bonus_point.rect)

        if player.rect.colliderect(bonus_point.rect):
            player.add_score()
            bonuses.pop(bonuses.index(bonus_point))

    for points in enemies:
        points.move_enemies()
        main_display.blit(points.enemy, points.rect)

        if player.rect.colliderect(points.rect):
            player.minus_score()
            enemies.pop(enemies.index(points))

    player.rect = player.rect.move(player.movement)

    player.movement = [0, 0]

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player.rect.bottom < HEIGHT:
        player.move_down()
    elif keys[K_UP] and player.rect.top > 0:
        player.move_up()
    elif keys[K_RIGHT] and player.rect.right < WIDTH:
        player.move_right()
    elif keys[K_LEFT] and player.rect.left > 0:
        player.move_left()

    main_display.blit(FONT.render(str(player.score), True, COLOR_BLACK), (WIDTH-50, 20))
    main_display.blit(player.player, player.rect)

    pygame.display.flip()

    if player.score == 0:
        playing = False

    for points in enemies:
        if points.rect.left < 0:
            enemies.pop(enemies.index(points))

    for point in bonuses:
        if point.rect.bottom > HEIGHT:
            bonuses.pop(bonuses.index(point))

pygame.quit()