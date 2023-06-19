import pygame
from pygame.sprite import Sprite
import random

# Gener
from game.utils.constants import ENEMY_1 ,SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_width = 40
        self.image_height = 50
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(50, SCREEN_WIDTH - self.image_width)
        

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.y += 8
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.centerx = random.randint(50, SCREEN_WIDTH - self.image_width)

    def update(self):
        self.move()
        
        

        
            