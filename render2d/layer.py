import numpy as np
from render2d import circle
from render2d import rectangle
from render2d import polygon

class Layer:
    # this class defines a single layer within a canvas
    def __init__(self, label, depth):
        self.label = label
        self.depth = depth
        self.objects = []

    def add_object(self, object):
        self.objects.append(object)

    def render(self, height, width):
        buffer = np.zeros((height, width, 4), dtype=np.float32)
        y_coords, x_coords = np.meshgrid( np.linspace(0.0, 1.0, buffer.shape[0]),
                                          np.linspace(0.0, 1.0, buffer.shape[1]),
                                          indexing='ij')
        coords = np.dstack((y_coords, x_coords))

        for object in self.objects:
            y_min_index = max(0, int(object.y_min * height))
            y_max_index = min(height-1, int(object.y_max * height))

            x_min_index = max(0, int(object.x_min * width))
            x_max_index = min(width-1, int(object.x_max * width))
            coords_within_bounds = coords[y_min_index:y_max_index, x_min_index:x_max_index]

            bool_array = object.intersect(coords_within_bounds)
            object.render(bool_array, buffer, y_min_index, x_min_index)
        return buffer

    def add_circle(self, y, x, radius, color):
        self.objects.append(circle.Circle(y, x, radius, color))

    def add_rectangle(self, y, x, height, width, color):
        self.objects.append(rectangle.Rectangle(y, x, height, width, color))

    def add_polygon(self, coordinates, color):
        self.objects.append(polygon.Polygon(coordinates, color))

