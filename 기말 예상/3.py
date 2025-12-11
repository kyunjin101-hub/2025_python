#충돌 발생 

import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - Collision")

clock = pygame.time.Clock()

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

class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((50, 50))
    self.image.fill((255, 0, 0))
    self.rect = self.image.get_rect(center=(x, y))

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
enemy = Enemy(300, 200)

all_sprites.add(player, enemy)
enemies.add(enemy)

running = True
font = pygame.font.SysFont(None, 40)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  all_sprites.update()

  screen.fill((170, 200, 255))
  all_sprites.draw(screen)

  # 충돌 검사
  if pygame.sprite.spritecollide(player, enemies, False):
    text = font.render("HIT!", True, (255, 0, 0))
    screen.blit(text, (20, 20))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
