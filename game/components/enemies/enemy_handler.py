import pygame
from game.components.enemies.enemy_ship import EnemyShip
from game.components.bullet import Bullet

class EnemyHandler:
    MAX_ENEMIES = 4

    def __init__(self, player):
        self.enemies = []
        self.enemies.append(EnemyShip())
        self.player = player
        self.score = 0
        

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
                self.remove_enemy(enemy)
                
            if self.player.bullet is not None:   #si la bala existe 
                if self.player.bullet.collides_with_enemy(enemy):
                    enemy.is_alive = False
                    print("Colision")
                    self.player.bullet = None
                    self.score += 100
                    print(self.score)
                    
            if enemy.enemy_bullet is not None:
                enemy.enemy_bullet.update_enemy()
                if enemy.enemy_bullet.rect.colliderect(self.player.rect):
                    print("colision2")
                    enemy.enemy_bullet = None         
            
            
                    
                       

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            if enemy.enemy_bullet is not None:
                enemy.enemy_bullet.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < self.MAX_ENEMIES:
            self.enemies.append(EnemyShip())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

