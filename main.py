import pygame
import sys
from snake import Snake
from food import Food
from game import show_game_over
from config import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, BLACK, WHITE, GAME_SPEED


def main():
    # 初始化Pygame
    pygame.init()
    
    # 设置游戏窗口
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    
    # 初始化字体
    font = pygame.font.SysFont(None, 36)
    
    snake = Snake()
    food = Food()
    score = 0
    
    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # 控制蛇的移动方向
                if event.key == pygame.K_UP:
                    if snake.direction.y != 1: # 防止反向移动
                        snake.direction = pygame.math.Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if snake.direction.y != -1:
                        snake.direction = pygame.math.Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if snake.direction.x != -1:
                        snake.direction = pygame.math.Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if snake.direction.x != 1:
                        snake.direction = pygame.math.Vector2(-1, 0)
        
        # 移动蛇
        snake.move_snake()
        
        # 检查碰撞
        if snake.check_collision():
            show_game_over(screen, score, font)
            # 重置游戏状态
            snake = Snake()
            food = Food()
            score = 0
            
        # 检查是否吃到食物
        if snake.body[0] == food.pos:
            food.randomize()
            snake.add_block()
            score += 10
            
        # 绘制游戏画面
        screen.fill(BLACK)
        snake.draw_snake(screen)
        food.draw_food(screen)
        
        # 显示分数
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(GAME_SPEED) # 控制游戏速度


if __name__ == "__main__":
    main()