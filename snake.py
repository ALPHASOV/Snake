import pygame
from config import CELL_SIZE, CELL_NUMBER_X, CELL_NUMBER_Y, GREEN


class Snake:
    def __init__(self):
        # Initial position at the center of the screen
        self.body = [pygame.math.Vector2(CELL_NUMBER_X//2, CELL_NUMBER_Y//2),
                     pygame.math.Vector2(CELL_NUMBER_X//2 - 1, CELL_NUMBER_Y//2),
                     pygame.math.Vector2(CELL_NUMBER_X//2 - 2, CELL_NUMBER_Y//2)]
        self.direction = pygame.math.Vector2(1, 0) # Initial movement to the right
        self.new_block = False # Whether to add a new block to the body
        
    def draw_snake(self, screen):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, block_rect)
            
    def move_snake(self):
        if self.new_block:
            # If food is eaten, don't remove the tail, just add a new head
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            # Normal movement, remove tail, add new head
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            
    def add_block(self):
        self.new_block = True
        
    def check_collision(self):
        # Check wall collision
        if not 0 <= self.body[0].x < CELL_NUMBER_X or not 0 <= self.body[0].y < CELL_NUMBER_Y:
            return True
        # Check self collision
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        return False