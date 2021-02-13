import pygame


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
