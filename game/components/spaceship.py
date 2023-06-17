import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP

class Spaceship(Sprite):
    def __init__(self):
        self.image_width =  40
        self.image_heigth = 50
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.image_width, self.image_heigth))
        self.rect = self.image.get_rect()
        
    
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
        
          
    def update(self, keyboard_events):    
        speed = 5  # Velocidad de movimiento de la nave

        # Verificar las teclas presionadas y actualizar la posición de la nave
        if keyboard_events[pygame.K_LEFT]:
            self.rect.x -= speed
        elif keyboard_events[pygame.K_RIGHT]:
            self.rect.x += speed
        elif keyboard_events[pygame.K_UP]:
            self.rect.y -= speed
        elif keyboard_events[pygame.K_DOWN]:
            self.rect.y += speed
