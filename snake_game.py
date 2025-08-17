import pygame
import random
import sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        if new_head in self.positions:
            return False
        
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            return False
        
        self.positions.insert(0, new_head)
        
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False
        
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def grow_snake(self):
        self.grow = True

    def draw(self, surface):
        for position in self.positions:
            rect = pygame.Rect(position[0] * GRID_SIZE, position[1] * GRID_SIZE, 
                             GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GREEN, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)

class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        return (random.randint(0, GRID_WIDTH - 1), 
                random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, 
                         GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)

class Game:
    def __init__(self):
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("贪吃蛇游戏")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((1, 0))
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True

    def update(self):
        if not self.snake.move():
            return False
        
        if self.snake.positions[0] == self.food.position:
            self.snake.grow_snake()
            self.score += 10
            while self.food.position in self.snake.positions:
                self.food.position = self.food.generate_position()
        
        return True

    def draw(self):
        self.surface.fill(BLACK)
        self.snake.draw(self.surface)
        self.food.draw(self.surface)
        
        score_text = self.font.render(f"分数: {self.score}", True, WHITE)
        self.surface.blit(score_text, (10, 10))
        
        pygame.display.flip()

    def game_over_screen(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.surface.blit(overlay, (0, 0))
        
        game_over_text = self.font.render("游戏结束!", True, WHITE)
        score_text = self.font.render(f"最终分数: {self.score}", True, WHITE)
        restart_text = self.font.render("按 R 重新开始，ESC 退出", True, WHITE)
        
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        
        self.surface.blit(game_over_text, game_over_rect)
        self.surface.blit(score_text, score_rect)
        self.surface.blit(restart_text, restart_rect)
        
        pygame.display.flip()

    def run(self):
        running = True
        game_active = True
        
        while running:
            if game_active:
                running = self.handle_events()
                if running:
                    game_active = self.update()
                    self.draw()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.__init__()
                            game_active = True
                        elif event.key == pygame.K_ESCAPE:
                            running = False
                
                self.game_over_screen()
            
            self.clock.tick(10)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()