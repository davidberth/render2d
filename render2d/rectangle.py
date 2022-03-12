from render2d.renderable import Renderable
import numpy as np

class Rectangle(Renderable):
    def __init__(self, y, x, height, width, edge_width, color, edge_color):
        self.y_min = y
        self.x_min = x
        self.y_max = y + height
        self.x_max = x + width
        self.edge_width = edge_width
        self.color = color
        self.edge_color = edge_color

    def intersect(self, coords):
        # TODO find a cleaner way to do this, some numpy function
        bool_array = coords[:,:,0] > -1.0

        min_distance = np.absolute(coords[:,:,0] - self.y_min)
        max_distance = np.absolute(coords[:,:,0] - self.y_max)
        y_distance = np.minimum(min_distance, max_distance)
        min_distance = np.absolute(coords[:,:,1] - self.x_min)
        max_distance = np.absolute(coords[:,:,1] - self.x_max)
        x_distance = np.minimum(min_distance, max_distance)
        edge_distance = np.minimum(y_distance, x_distance)

        return bool_array, edge_distance
