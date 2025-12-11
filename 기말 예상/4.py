#아래 위

import pygame
import math

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - 8 Direction Move")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("dukbird.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
    self.speed = 3

  def update(self):
    keys = pygame.key.get_pressed()
    dx = dy = 0

    if keys[pygame.K_LEFT]:  dx -= 1
    if keys[pygame.K_RIGHT]: dx += 1
    if keys[pygame.K_UP]:    dy -= 1
    if keys[pygame.K_DOWN]:  dy += 1

    # 대각선 이동 부드럽게 처리
    if dx != 0 or dy != 0:
      length = math.sqrt(dx*dx + dy*dy)
      dx = (dx / length) * self.speed
      dy = (dy / length) * self.speed

    self.rect.x += dx
    self.rect.y += dy

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

  screen.fill((170, 200, 255))
  all_sprites.draw(screen)

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
