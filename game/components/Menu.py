import sys
import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
class GameOverScreen:
    def __init__(self, screen, score, new_hs, highest_score):
        self.screen = screen
        self.score = score
        self.new_hs = new_hs
        self.highest_score = highest_score

    def show(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        score_text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(score_text, score_rect)
        continue_text = font.render("Press Enter to continue", True, (255, 255, 255))
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
        Gameover = True
        while Gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                       Gameover = False