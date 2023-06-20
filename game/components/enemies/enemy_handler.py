from game.components.enemies.enemy_ship import EnemyShip
from game.components.bullet import Bullet

class EnemyHandler:
    MAX_ENEMIES = 4

    def __init__(self):
        self.enemies = []
        self.enemies.append(EnemyShip())

    def update(self):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update()
            if not enemy.is_alive:
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < self.MAX_ENEMIES:
            self.enemies.append(EnemyShip())

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

