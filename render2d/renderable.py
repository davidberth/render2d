import numpy as np

class Renderable:
    def __init__(self):
        self.get_bounds()
        self.x_min = None
        self.x_max = None
        self.y_min = None
        self.y_max = None

    def get_bounds(self):
        pass

    def intersect(self, coords):
        return np.array((0,0))

    def render(self, bool_array, buffer, y_min_index, x_min_index):
        indices_y, indices_x = np.where(bool_array)
        buffer[indices_y + y_min_index, indices_x + x_min_index, :] = self.color

