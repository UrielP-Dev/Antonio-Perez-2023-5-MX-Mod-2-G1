import random
from typing import Any
from pygame.sprite import Sprite
import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET, SHIELD, HEART

class Powerup(Sprite):
    
    def __init__(self, location, Image):
        self.image = Image
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.speed = 2
        
    def update(self):
        self.rect.y += self.speed
    
    def colision_with_spaceship(self, player):
        return self.rect.colliderect(player.rect)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def activate(self, player):
        player.num_collisions -= 1
        print("Lifes: ", -1*(-3 +player.num_collisions))
            

    def shield(self, player, sprite):
        if sprite:
            player.shield()
            print("Escudo")
        else: 
            player.shield_off()   
        
    
    
        
                 
        
    