import pygame
import images
from towers import *

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(images.mouse_image_path)
        self.image = pygame.transform.scale(self.image, images.mouse_scale)

        self.rect = self.image.get_rect()
        self.state = "hover"
        self.rect.center = pygame.mouse.get_pos()
    
    def click(self, tower_button_group, wave_button_group, tower_group, wave_manager):
        # hover is the default mouse state
        if self.state == "hover":
            tower_button_collisions = pygame.sprite.spritecollide(self, tower_button_group, False)
            wave_button_collision = pygame.sprite.spritecollide(self, wave_button_group, False)
            # check if we pressed the tower button (we will being placing a tower)
            if len(tower_button_collisions) > 0:
                self.state = "placing"
                self.image = pygame.image.load(images.tower_image_path)
                self.image = pygame.transform.scale(self.image, images.tower_scale)
            
            # check if we pressed the start wave button (the next wave will start)
            elif len(wave_button_collision) > 0:
                print("start wave")
                wave_manager.start_wave()
        
        # we are placing a tower
        elif self.state == "placing":
            # set the mouse state back to default hover
            self.state = "hover"
            self.image = pygame.image.load(images.mouse_image_path)
            self.image = pygame.transform.scale(self.image, images.mouse_scale)

            # places tower with some hard coded values
            tower = Tower(images.tower_image_path, images.projectile_image_path, 
                          list(self.rect.center), 0, 3, 2000, 10)
            tower_group.add(tower)
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()