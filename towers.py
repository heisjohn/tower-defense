import pygame
import images
from projectile import *

class Tower(pygame.sprite.Sprite):
    def __init__(self, image_path, projectile_image_path, location, range, damage, fire_rate, projectile_speed):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, images.tower_scale)

        self.projectile_image_path = projectile_image_path
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.range = range
        self.projectile_speed = projectile_speed
        self.damage = damage
        # milliseconds in between firing
        self.fire_rate = fire_rate
        # tick in which tower last fired
        self.last_fired = 0

    def shoot(self, time, units, projectile_group):
        if time - self.last_fired > self.fire_rate:
            if units:
                self.last_fired = time
                projectile = Projectile(self.projectile_image_path, self, units[0], self.projectile_speed)
                projectile_group.add(projectile)