import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP,SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    def __init__(self,screen_width, screen_height):
        self.image_width =  40
        self.image_heigth = 50
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.image_width, self.image_heigth))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.centery = screen_height // 2
        self.speed = 15
        
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        
          
    def update(self, keyboard_events):    
        
        if keyboard_events[pygame.K_LEFT] and  self.rect.x > 5 :
            self.rect.x -= self.speed
        elif keyboard_events[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.image_width: 
            self.rect.x += self.speed
        elif keyboard_events[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keyboard_events[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.image_heigth:
            self.rect.y += self.speed
