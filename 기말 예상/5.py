import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 - Sound Example")

clock = pygame.time.Clock()

# ---------------------- 사운드 로드 ----------------------
# 배경음악 (무한 반복)
pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.play(-1)

# 걷기 효과음
walk_sound = pygame.mixer.Sound("walk.wav")
walk_sound.set_volume(0.4)   # 음량 조절

# ---------------------------------------------------------


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 3
        self.is_walking = False

    def update(self):
        keys = pygame.key.get_pressed()
        moving_now = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            moving_now = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            moving_now = True
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            moving_now = True
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            moving_now = True

        # 사운드 처리 ---------------------------------------
        if moving_now and not self.is_walking:
            walk_sound.play()
            self.is_walking = True
        elif not moving_now:
            self.is_walking = False
        # ----------------------------------------------------

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
