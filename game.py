import pygame
import sys
from config import WHITE, WINDOW_WIDTH, WINDOW_HEIGHT


def show_game_over(screen, score, font):
    game_over_text = font.render(f"Game Over! Score: {score}", True, WHITE)
    restart_text = font.render("Press R to Restart, Q to Quit", True, WHITE)
    screen.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, WINDOW_HEIGHT//2 - 50))
    screen.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, WINDOW_HEIGHT//2 + 10))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()