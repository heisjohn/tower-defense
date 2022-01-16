import pygame
import images
import copy
from engine import *
from track import *

class Unit(pygame.sprite.Sprite):
    def __init__(self, image_path, health, speed, track):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, images.unit_scale)

        self.rect = self.image.get_rect()
        self.health = health
        self.speed = speed
        self.track = track
        self.location = Location(track)
        self.rect.center = self.location.center
    
    def copy(self):
        return copy.deepcopy(self)
    
    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def update(self):
        self.move_helper(self.speed)
    
    def move_helper(self, amount):
        # recursive method to move through line segments represented by track.points

        # if the user has reached the end of the track (segment that it is travelling on is out of bounds)
        if self.location.segment == len(self.track.points):
            # TODO: player takes damage because unit reached the end
            self.kill()
            return
        
        # if the user has not reached the end, we want to go to the end of the line segment we are on
        end = self.track.points[self.location.segment]
        destination, remainder = GameEngine.move(self.location.center, end, amount)

        # update location
        self.location.center = destination
        self.rect.center = self.location.center

        # if we are done traveling, return
        if remainder == 0:
            return
        # otherwise keep going along the next segment
        else:
            self.location.segment += 1
            self.move_helper(remainder)
