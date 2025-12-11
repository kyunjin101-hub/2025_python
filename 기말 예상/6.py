import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9")

clock = pygame.time.Clock()  # FPS 제어 준비

# ---------------------- Player Sprite ----------------------
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
        if keys[pygame.K_LEFT]:  self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]:    self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:  self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())


# ---------------------- Apple Sprite ----------------------
class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


# ---------------------- Poop Sprite ----------------------
class Poop(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("poop.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



# ---------------------- Sprite 그룹 ----------------------
all_sprites = pygame.sprite.Group()
apple_group = pygame.sprite.Group()
poop_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)


# ---------------------- 사과 여러 개 생성 ----------------------
for i in range(5):   # 사과 5개
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
    apple = Apple(x, y)
    all_sprites.add(apple)
    apple_group.add(apple)

# ---------------------- 똥 여러 개 생성 ----------------------
for i in range(5):   # 똥 5개
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
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
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))
    pygame.draw.rect(screen, (255, 80, 80), (50, 280, 40, 40))
    pygame.draw.circle(screen, (0, 255, 0), (450, 150), 20)
    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
