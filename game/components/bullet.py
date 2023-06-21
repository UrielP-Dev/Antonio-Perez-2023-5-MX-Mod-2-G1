import pygame
from pygame.sprite import Sprite




class Bullet(Sprite):
    def __init__(self, location, sprite):
        self.image = pygame.transform.scale(sprite, (30, 40))
        self.rect = self.image.get_rect()
        self.speed = 35
        self.rect.center = location
        

    def update(self):
        self.rect.y -= self.speed
       

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def collides_with_enemy(self, enemy):
        return self.rect.colliderect(enemy.rect)   