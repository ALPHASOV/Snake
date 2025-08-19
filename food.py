import pygame
import random
from config import CELL_SIZE, CELL_NUMBER_X, CELL_NUMBER_Y, RED


class Food:
    def __init__(self):
        self.randomize()
        
    def draw_food(self, screen):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, food_rect)
        
    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER_X - 1)
        self.y = random.randint(0, CELL_NUMBER_Y - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)