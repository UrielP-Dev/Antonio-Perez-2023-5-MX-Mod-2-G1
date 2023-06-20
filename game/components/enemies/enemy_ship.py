import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1

class EnemyShip(Enemy):
    WIDTH = 40
    HEIGHT = 60


    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
