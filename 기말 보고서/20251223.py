import pygame
import random

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("파이썬 과제")

WHITE = (240, 255, 240)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SKYBLUE = (173, 216, 230)

font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 72)
GROUND_Y = 300
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 40, 40 

MARIO_IMG = pygame.image.load('마리오.png')
MARIO_IMG = pygame.transform.scale(MARIO_IMG, (40, 40))

COIN_IMG = pygame.image.load('코인.png')
COIN_IMG = pygame.transform.scale(COIN_IMG, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    
jump_sound = pygame.mixer.Sound("super-mario-coin-sound.mp3") #효과음 추가
jump_sound.set_volume(0.5)

class MARIO:
    def __init__(self):
        self.width = 40
        self.height = 40
        self.image = MARIO_IMG
        self.rect = pygame.Rect(50, GROUND_Y, 40, 40)
        self.velocity_y = 0
        self.jump_count = 0 
    
    def jump(self):
        if self.jump_count < 2: #더블점프
            jump_sound.play()
            self.velocity_y = -10
            self.jump_count += 1
    
    def update(self):
        self.rect.y += self.velocity_y
        self.velocity_y += 0.5

        if self.rect.y >= GROUND_Y:
            self.rect.y = GROUND_Y
            self.velocity_y = 0
            self.jump_count = 0
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle:
    def __init__(self):
        self.image = COIN_IMG
        self.rect = pygame.Rect(WIDTH, GROUND_Y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        self.scored = False 

    def update(self, speed):
        self.rect.x -= speed

    def draw(self, surface):
        surface.blit(self.image, self.rect) 

def reset_game():
    mario = MARIO()
    obstacles = []
    score = 0
    game_speed = 5
    return mario, obstacles, score, game_speed

def main():
    clock = pygame.time.Clock()
    mario, obstacles, score, game_speed = reset_game()
    isrunning = True
    game_over = False

    while isrunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isrunning = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not game_over:
                    mario.jump()
                else:
                    mario, obstacles, score, game_speed = reset_game()
                    game_over = False
                        
        if not game_over:
            screen.fill(SKYBLUE)
            
            if random.randint(1, 100) <= 3: 
                obstacles.append(Obstacle())

            for obs in obstacles[:]:
                obs.update(game_speed)
                if obs.rect.right < mario.rect.left and not obs.scored:
                    score += 1
                    obs.scored = True
                if obs.rect.right < 0:
                    obstacles.remove(obs)
                if mario.rect.colliderect(obs.rect):
                    game_over = True
                    
            mario.update()
            game_speed = 5 + score // 10

            pygame.draw.line(screen, WHITE, (0, GROUND_Y + mario.height), (WIDTH, GROUND_Y + mario.height), 2)
            
            mario.draw(screen)
            for obstacle in obstacles:
                obstacle.draw(screen)
                
            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (WIDTH - 130, 10))

        else: 
            screen.fill(SKYBLUE)
            game_over_surface = game_over_font.render("GAME OVER", True, RED)
            text_rect = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            screen.blit(game_over_surface, text_rect)
            
            final_score_surface = font.render(f"Final Score: {score}", True, BLACK)
            final_score_rect = final_score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
            screen.blit(final_score_surface, final_score_rect)
            
            restart_surface = font.render("Press SPACE to Restart", True, BLACK)
            restart_rect = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
            screen.blit(restart_surface, restart_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()