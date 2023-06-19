import pygame
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1 ,SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy(Sprite):
    def __init__(self,):
        self.image_width =  40
        self.image_heigth = 50
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image,(self.image_width, self.image_heigth))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
         

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))    

    def update(self):
        print(self.rect.x)
        flagR = True
        flagL = False
        if flagR and self.rect.x < SCREEN_WIDTH :
            self.rect.x += 5
        elif self.rect.x > SCREEN_WIDTH:
            flagR = False
            self.rect.x -= 5

        
            