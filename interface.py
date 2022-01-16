import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, location, scale):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, scale)

        self.rect = self.image.get_rect()
        self.rect.center = location