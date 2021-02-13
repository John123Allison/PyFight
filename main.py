import pygame
import pygame.locals


def main():
    # Setup stuff
    # Reference: https://coderslegacy.com/python/pygame-platformer-game-development/
    pygame.init()
    vec = pygame.math.Vector2  # 2 for two dimensional
    HEIGHT = 450
    WIDTH = 400
    ACC = 0.5
    FRIC = -0.12
    FPS = 60
    FramePerSec = pygame.time.Clock()
    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyFight")


if __name__ == '__main__':
    main()
