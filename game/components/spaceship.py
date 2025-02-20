import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, BULLET, SPACESHIP_SHIELD
from game.components.bullet import Bullet

class Spaceship:
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPACESHIP_SPEED = 20

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True
        self.bullet = None
        self.num_collisions = 0
        self.shield_start_time = None

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        
        if user_input[pygame.K_UP]:
            self.move_up()
        
        if user_input[pygame.K_DOWN]:
            self.move_down()
            
        if self.bullet is not None:
            self.bullet.update() 
            
          

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.bullet is not None:
            self.bullet.draw(screen) 

    def move_left(self):
        self.rect.x -= self.SPACESHIP_SPEED
        if self.rect.left < 0 - self.SPACESHIP_WIDTH:
            self.rect.x = SCREEN_WIDTH
            
    def move_right(self):
        self.rect.x += self.SPACESHIP_SPEED
        if self.rect.right > SCREEN_WIDTH + self.SPACESHIP_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > 0:
            self.rect.y -= self.SPACESHIP_SPEED
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SPACESHIP_SPEED

    def shoot(self):
        self.bullet = Bullet(self.rect.center, BULLET)
        
    def shield(self):
        self.image = SPACESHIP_SHIELD
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        
    
    def shield_off(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT)) 
    
        
            
        
    