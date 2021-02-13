import pygame
from pygame.constants import QUIT
from pygame.font import SysFont
import pygame.locals
from player import Player

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT - 10))


def main():
    # Setup stuff
    # Reference: https://coderslegacy.com/python/pygame-platformer-game-development/
    pygame.init()
    vec = pygame.math.Vector2  # 2 for two dimensional

    FramePerSec = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyFight")

    # instantiate player and platform
    player = Player()
    platform_test = Platform()

    # Create sprite groups
    # TODO make this not global lol
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(platform_test)

    ### MAIN GAME LOOP ###
    while True:
        for event in pygame.event.get():
            # Handle quitting the game
            if event.type == QUIT:
                pygame.quit()
                SysFont.exit()

        displaysurface.fill((0, 0, 0))

        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)

        pygame.display.update()
        FramePerSec.tick(FPS)


if __name__ == '__main__':
    main()
