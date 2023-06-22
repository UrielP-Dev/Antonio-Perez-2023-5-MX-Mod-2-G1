import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_handler import EnemyHandler

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10 # el numero de pixeles que el "objeto / imagen" se mueve en patalla
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_handler = EnemyHandler(self.player)
        self.score = 0
        self.highest_score = 0 
        self.new_hs = False

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing and self.enemy_handler.lose_game():
            self.handle_events()
            self.update()
            self.draw()
            if not self.enemy_handler.lose_game():
                self.show_game_over_screen()
                self.player.num_collisions = 0
                self.score = self.enemy_handler.score
                if self.score > self.highest_score:
                    self.new_hs = True
                    self.highest_score = self.score


                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                waiting = False
                                self.enemy_handler = EnemyHandler(self.player)  # Reiniciar los enemigos
                                self.playing = True
        pygame.display.quit()
        pygame.quit()                    
                              
        
                        

    def handle_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.playing = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pass
                
    def update(self):
        
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_handler.update()

    def draw(self):
        self.draw_background()
        self.clock.tick(FPS) # configuro cuantos frames per second voy a dibujar
        self.player.draw(self.screen)
        self.enemy_handler.draw(self.screen)
        # self.screen.fill((255, 255, 255)) # lleno el screen de color BLANCO???? 255, 255, 255 es el codigo RGB
        pygame.display.update() # esto hace que el dibujo se actualice en el display de pygame
        pygame.display.flip()  # hace el cambio

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()# alto de la imagen
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) # blit "dibuja"
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_game_over_screen(self):
        self.screen.fill((0, 0, 0))  
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        score_text = font.render("Score: " + str(self.enemy_handler.score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(score_text, score_rect)
        continue_text = font.render("Press Enter to Restar", True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        self.screen.blit(continue_text, continue_rect)
        continue_text = font.render("Highest Score: " + str(self.highest_score), True, (255, 255, 255))
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200))
        self.screen.blit(continue_text, continue_rect)
        if self.new_hs:
            continue_text = font.render("NEW Highest Score!!!!" , True, (255, 255, 255))
            continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250))
            self.screen.blit(continue_text, continue_rect)
        pygame.display.flip()  
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting = False