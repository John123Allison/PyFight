import pygame
import pygame.locals
from .player import Player

# Constants
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60


def main():
    # Setup stuff
    # Reference: https://coderslegacy.com/python/pygame-platformer-game-development/
    pygame.init()
    vec = pygame.math.Vector2  # 2 for two dimensional
    FramePerSec = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyFight")

    # Instantiate platform and player
    platform_one = Platform()
    player = Player()


class Platform(pygame.sprite.Sprite):
    """
    Class for a basic platform.
    TODO Refactor this to its own file
    """

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT - 10))


if __name__ == '__main__':
    main()
