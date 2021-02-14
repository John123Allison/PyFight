from constants import FPS, HEIGHT, WIDTH
import pygame
from pygame.constants import KEYDOWN, K_SPACE, QUIT
from pygame.font import SysFont
import pygame.locals
from player import Player


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT - 10))


# Setup stuff
# Reference: https://coderslegacy.com/python/pygame-platformer-game-development/
pygame.init()

FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyFight")

# instantiate player and platform
player_obj = Player()
platform_test = Platform()

# Create sprite groups
# TODO make this not global lol
all_sprites = pygame.sprite.Group()
all_sprites.add(player_obj)
all_sprites.add(platform_test)

player_group = pygame.sprite.Group()
player_group.add(player_obj)

platform_group = pygame.sprite.Group()
platform_group.add(platform_test)

### MAIN GAME LOOP ###
while True:
    for event in pygame.event.get():
        # Handle quitting the game
        if event.type == QUIT:
            pygame.quit()
            SysFont.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # check if in collision with platform
                if player_obj.check_collision(platform_group):
                    player_obj.jump()

    # Handle player movement
    player_obj.move()
    player_obj.check_collision(platform_group)

    displaysurface.fill((0, 0, 0))

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
