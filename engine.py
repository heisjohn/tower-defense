import math

class GameEngine:
    def move(start, end, speed):
        # returns end point and a remainder if there is one
        distance = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        if speed > distance:
            return list(end), speed - distance
        x = (end[0] - start[0]) * speed / distance + start[0]
        y = (end[1] - start[1]) * speed / distance + start[1]
        return [x, y], 0