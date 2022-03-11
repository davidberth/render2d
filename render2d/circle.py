from render2d.renderable import Renderable
import numpy as np

class Circle(Renderable):
    def __init__(self, center_y, center_x, radius, color):
        self.center_y = center_y
        self.center_x = center_x
        self.radius = radius
        self.color = color

        self.radius_squared = radius * radius
        self.get_bounds()

    def get_bounds(self):
        # compute the axis-aligned bounding box used for rendering
        self.y_min = self.center_y - self.radius
        self.x_min = self.center_x - self.radius
        self.y_max = self.center_y + self.radius
        self.x_max = self.center_x + self.radius

    def intersect(self, coords):
        bool_array = (coords[:,:,0] - self.center_y)**2 + (coords[:,:,1] - self.center_x)**2 < self.radius_squared
        return bool_array


