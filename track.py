from array import array
from engine import *

class Track:
    def __init__(self, points, WIDTH, HEIGHT):
        # argument points is an array of coordinates that represents the track, adjacent points represent a line segment
        # x and y values are passed in as values from 0 to 100 and then converted based on width and height (so that pixel values aren't hard coded)
        self.points = [[arr[0] / 100 * WIDTH, arr[1] / 100 * HEIGHT] for arr in points]

class Location:
    def __init__(self, track):
        # starts at the beginning of the track at the 1st segment
        self.track = track
        self.center = track.points[0]
        self.segment = 1