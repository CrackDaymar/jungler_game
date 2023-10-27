import random
import pygame



class GameObject:
    def __init__(self):
        self.size = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = 0  # Инициализируйте x координату объекта
        self.y = 0  # Инициализируйте y координату объекта
        self.width = self.size  # Добавьте ширину объекта
        self.height = self.size  # Добавьте высоту объекта

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)