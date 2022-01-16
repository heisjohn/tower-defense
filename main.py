import pygame
import sys
import images
from interface import *
from towers import *
from units import *
from track import *
from mouse import *
from waves import *

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60

background = pygame.image.load(images.track_image_path)

tower_group = pygame.sprite.Group()
unit_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()
wave_button_group = pygame.sprite.Group()
tower_button_group = pygame.sprite.Group()
mouse_group = pygame.sprite.Group()

track_points = [[0, 70], [25, 70], [25, 30], [50, 30], [50, 70], [75, 70], [75, 30], [100, 30]]
track = Track(track_points, WIDTH, HEIGHT)

mouse = Mouse()
mouse_group.add(mouse)

tower_button = Button(images.tower_image_path, [WIDTH / 2, HEIGHT - images.tower_scale[1] / 2], images.tower_scale)
tower_button_group.add(tower_button)

wave_button = Button(images.play_image_path, [WIDTH / 2, images.play_scale[1] / 2], images.play_scale)
wave_button_group.add(wave_button)

wave_manager = Waves(unit_group)

pygame.mouse.set_visible(False)

def update_game(time):
    unit_group.update()
    projectile_group.update()
    mouse.update()
    wave_manager.send_unit(time, track)
    for tower in tower_group:
        tower.shoot(time, unit_group.sprites(), projectile_group)

def handle_drawing():
    unit_group.draw(WIN)
    projectile_group.draw(WIN)
    tower_group.draw(WIN)
    wave_button_group.draw(WIN)
    tower_button_group.draw(WIN)
    mouse_group.draw(WIN)

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse.click(tower_button_group, wave_button_group, tower_group, wave_manager)
        
        pygame.display.flip()
        WIN.blit(background, (0, 0))
        update_game(time)
        handle_drawing()

        clock.tick(FPS)
        

if __name__ == "__main__":
    main()