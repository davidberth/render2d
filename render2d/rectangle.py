from render2d.renderable import Renderable
import numpy as np

class Rectangle(Renderable):
    def __init__(self, y, x, height, width, color):
        self.y_min = y
        self.x_min = x
        self.y_max = y + height
        self.x_max = x + width

        self.color = color

    def intersect(self, coords):
        # TODO find a cleaner way to do this, some numpy function
        bool_array = coords[:,:,0] > -1.0
        return bool_array
