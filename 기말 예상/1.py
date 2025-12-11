#객체 생성

import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - Add Enemy")

clock = pygame.time.Clock()

# Player Sprite
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("dukbird.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH // 2, HEIGHT // 2)
    self.speed = 3

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]: self.rect.x += self.speed
    if keys[pygame.K_UP]: self.rect.y -= self.speed
    if keys[pygame.K_DOWN]: self.rect.y += self.speed
    self.rect.clamp_ip(screen.get_rect())

# Enemy Sprite 추가
class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((40, 40))
    self.image.fill((255, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
enemy1 = Enemy(100, 100)
enemy2 = Enemy(500, 300)

all_sprites.add(player, enemy1, enemy2)
enemies.add(enemy1, enemy2)

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  all_sprites.update()

  screen.fill((170, 200, 255))
  all_sprites.draw(screen)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
