from constants import ACC, FRIC, GRAV, WIDTH
import pygame
from pygame.constants import K_LEFT, K_RIGHT

vec = pygame.Vector2


class Player(pygame.sprite.Sprite):
    """
    Main class for the player controlled object.
    """

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        # Use a rect for the player for now
        self.rect = self.surf.get_rect(center=(10, 420))

        self.pos = vec((10, 385))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self):
        self.acc = vec(0, GRAV)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos
