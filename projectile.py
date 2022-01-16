import pygame
import copy
import images
from engine import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, image_path, tower, unit, speed):
        # tower is the source, unit is the target
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, images.projectile_scale)

        self.rect = self.image.get_rect()
        self.rect.center = tower.rect.center
        self.tower = tower
        self.unit = unit
        self.speed = speed

    def copy(self):
        return copy.deepcopy(self)

    def update(self):
        destination, _ = GameEngine.move(self.rect.center, self.unit.rect.center, self.speed)
        # if the destination after moving is equal to the location of the unit
        if destination[0] == self.unit.rect.center[0] and destination[1] == self.unit.rect.center[1]:
            # damage the unit and remove the projectile from the game
            self.unit.damage(self.tower.damage)
            self.kill()
            return
        # otherwise set the center to the new destination
        self.rect.center = destination
