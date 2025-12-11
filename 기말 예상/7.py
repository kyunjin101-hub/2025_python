import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9")

clock = pygame.time.Clock()

# ---------------------- Player ----------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]:    self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:  self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())


# ---------------------- Apple (좌우로 움직임) ----------------------
class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.choice([2, 3, 4])
        self.dir = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed * self.dir
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dir *= -1


# ---------------------- Poop (위아래로 움직임) ----------------------
class Poop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("poop.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.choice([2, 3, 4])
        self.dir = random.choice([-1, 1])

    def update(self):
        self.rect.y += self.speed * self.dir
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dir *= -1


# ---------------------- 그룹 ----------------------
all_sprites = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
poop_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# 사과 여러 개
for i in range(5):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 100)
    apple = Apple(x, y)
    all_sprites.add(apple)
    apple_group.add(apple)

# 똥 여러 개
for i in range(5):
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 100)
    poop = Poop(x, y)
    all_sprites.add(poop)
    poop_group.add(poop)


# ---------------------- 게임 루프 ----------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((170, 200, 255))

    # ★★★ 네가 넣은 화면 밑 초록색 바닥 ★★★
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
