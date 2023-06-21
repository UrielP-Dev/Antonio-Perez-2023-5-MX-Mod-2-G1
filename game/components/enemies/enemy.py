import random

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET
from game.components.bullet import Bullet

class Enemy:
    X_POS_LIST = [100, 150, 200, 250, 300, 350, 400, 450]
    Y_POS = 20
    SPEED_X = 6
    SPEED_Y = 2
    LEFT = 'left'
    RIGHT = 'right'
    MOV_X = [LEFT, RIGHT]
    INTERVAL = 100


    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.mov_x = random.choice(self.MOV_X)
        self.index = 0 
        self.is_alive = True
        self.shoot_interval = 0
        self.enemy_bullet = None


    def update(self):
        if self.rect.y >= SCREEN_HEIGHT:
            self.is_alive = False
        self.move()
        self.shoot()
        if self.enemy_bullet is not None:
            self.enemy_bullet.update_enemy()
            if self.enemy_bullet.rect.bottom >= SCREEN_HEIGHT:
                self.enemy_bullet = None

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y += self.SPEED_Y
        if self.mov_x == self.LEFT:
            self.rect.x -= self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x <= 0:
                self.mov_x = self.RIGHT
                self.index = 0
        else:
            self.rect.x += self.SPEED_X
            if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                self.mov_x = self.LEFT
                self.index = 0
        
        self.index += 1
        
    def shoot(self):
        if self.shoot_interval <= 0:
            self.enemy_bullet = Bullet(self.rect.center, BULLET)
            self.shoot_interval = random.randint(10, 50 )  # Intervalo de tiempo aleatorio entre disparos
        else:
            self.shoot_interval -= 1    
