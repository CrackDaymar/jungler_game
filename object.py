import pygame
from setting import  WIDTH, HEIGHT
import random


class Player:
    def __init__(self, color):
        self.speed = 5
        self.movement = [0, 0]
        self.size = (20, 20)
        self.player = pygame.image.load('image/player.png')
        self.rect = pygame.Rect((WIDTH/2)-10, (HEIGHT/2)-10, *self.size)
        self.score = 1

    def move_down(self):
        self.movement = [0, self.speed]

    def move_up(self):
        self.movement = [0, -self.speed]

    def move_left(self):
        self.movement = [-self.speed, 0]

    def move_right(self):
        self.movement = [self.speed, 0]

    def add_score(self):
        self.score += 1

    def minus_score(self):
        self.score -= 1


class Enemies:
    def __init__(self, width, height, color):
        self.size = (random.randint(10, 30), random.randint(10, 30))
        self.color = random.choice(color)
        self.enemy = pygame.transform.scale(pygame.image.load('image/enemy.png'), (50, 20))
        self.rect = pygame.Rect(width, random.randint(20, height-20), *self.size)
        self.move = [-(random.randint(4, 9)), 0]

    def move_enemies(self):
        self.rect = self.rect.move(self.move)


class Bonus:
    def __init__(self, width, height):
        self.size = (random.randint(10, 30), random.randint(10, 30))
        self.color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
        self.bonus = pygame.transform.scale(pygame.image.load('image/bonus.png'), (40, 100))
        self.rect = pygame.Rect(random.randint(40, width), 100, *self.size)
        self.move = [0, (random.randint(4, 9))]

    def move_bonuses(self):
        self.rect = self.rect.move(self.move)