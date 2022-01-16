from units import *
import images

# temporary constants
COOLDOWN = 2000
UNITS_IN_WAVE = 10

class Waves:
    def __init__(self, unit_group):
        self.wave = 0
        self.unit_group = unit_group
        self.last_unit_time = 0
        self.units_sent = 0
        self.wave_finished = True
    
    def start_wave(self):
        if self.wave_finished:
            self.wave += 1
            self.wave_finished = False
            self.units_sent = 0
    
    def send_unit(self, time, track):
        if self.units_sent >= UNITS_IN_WAVE:
            self.wave_finished = True
        elif not self.wave_finished and time - self.last_unit_time >= COOLDOWN:
            print("send unit")
            # sends unit with some hard coded values
            unit = Unit(images.unit_image_path, 10, 1, track)
            self.unit_group.add(unit)
            self.units_sent += 1
            self.last_unit_time = time
