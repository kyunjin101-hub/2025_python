#화면 크게

import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 700   # 화면 확대
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - Bigger Screen")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("dukbird.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.center = (WIDTH // 2, HEIGHT // 2)
    self.speed = 4              # 큰 화면에 맞춰 속도 살짝 증가

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: self.rect.x -= self.speed
    if keys[pygame.K_RIGHT]: self.rect.x += self.speed
    if keys[pygame.K_UP]: self.rect.y -= self.speed
    if keys[pygame.K_DOWN]: self.rect.y += self.speed
    self.rect.clamp_ip(screen.get_rect())

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  all_sprites.update()

  screen.fill((150, 180, 255))
  all_sprites.draw(screen)

  pygame.display.flip()
  clock.tick(60)
pygame.quit()
