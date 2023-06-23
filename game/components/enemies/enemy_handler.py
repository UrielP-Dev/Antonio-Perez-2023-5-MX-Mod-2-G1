import random
import time
import pygame
from game.components.enemies.enemy_ship import EnemyShip
from game.components.bullet import Bullet
from game.components.powerup import Powerup
from game.utils.constants import SCREEN_HEIGHT, SHIELD, HEART,SPACESHIP_SHIELD

class EnemyHandler:
    MAX_ENEMIES = 2
    POWERUP_PROBABILITY = 0.50
    
    def __init__(self, player):
        self.enemies = []
        self.enemies.append(EnemyShip())
        self.player = player
        self.score = 0
        self.powerups = []
        self.active_powerups = []
        self.powerup_image = random.choice([SHIELD, HEART])
        self.shield = False
        self.falg2 = False

        
        
        

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            
            if not enemy.is_alive:
                self.remove_enemy(enemy)
                if random.random() < self.POWERUP_PROBABILITY:
                    self.powerup_image = random.choice([SHIELD, HEART])
                    powerup = Powerup(enemy.rect.center, self.powerup_image)
                    self.powerups.append(powerup)
                
                
                
            if self.player.bullet is not None:   #si la bala existe 
                if self.player.bullet.collides_with_enemy(enemy):
                    enemy.is_alive = False
                    ##print("Colision")
                    self.player.bullet = None
                    self.score += 100
                    print("Puntuacion", self.score)
                    
                    
                    
                    
            if enemy.enemy_bullet is not None:
                enemy.enemy_bullet.update_enemy()
                if enemy.enemy_bullet.rect.colliderect(self.player.rect):
                    
                    if not self.shield:
                        print("Life lose")
                        self.player.num_collisions += 1
                        print("Lifes: ", 3-self.player.num_collisions)
                        enemy.enemy_bullet = None
                    else:
                        print("No damage")
                        self.shield = False   
                        
                          
                            
                            
            
        for powerup in self.powerups:
            powerup.update()
            if powerup.rect.colliderect(self.player.rect):
                # Handle power-up collision with the player
                self.handle_powerup_collision(powerup)
                self.powerups.remove(powerup)


        # Add active power-ups and remove expired power-ups
        for powerup in self.active_powerups:
            powerup.update()
            

        self.powerups = [powerup for powerup in self.powerups if powerup.rect.bottom < SCREEN_HEIGHT]
           
                    
         

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
            if enemy.enemy_bullet is not None:
                enemy.enemy_bullet.draw(screen)
        for powerup in self.powerups:
            powerup.draw(screen)               
              


    def add_enemy(self):
        if len(self.enemies) < self.MAX_ENEMIES:
            self.enemies.append(EnemyShip())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        
    def lose_game(self):
        if self.player.num_collisions >= 3:
            return False
        else:
            return True  
        
    def handle_powerup_collision(self, powerup):
        if powerup.colision_with_spaceship(self.player):
            if self.shield == False:
                self.player.shield_off()
            if self.powerup_image == SHIELD:
                self.player.shield()
                self.shield = True
                self.powerup_image = SPACESHIP_SHIELD  # Activar sprite de escudo
            elif self.powerup_image == HEART:
                powerup.activate(self.player)
            self.active_powerups.append(powerup)
        else:
            self.powerups.remove(powerup)
            print("no entro")
            
    

         

