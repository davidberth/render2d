import numpy as np
from render2d import circle
from render2d import rectangle
from render2d import polygon
from render2d import blur
from render2d import tint

class Layer:
    # this class defines a single layer within a canvas
    def __init__(self, label, depth):
        self.label = label
        self.depth = depth
        self.objects = []
        self.effects = []

    def add_object(self, object):
        self.objects.append(object)

    def render(self, height, width):
        # create the buffer for rendering
        buffer = np.zeros((height, width, 4), dtype=np.float32)
        y_coords, x_coords = np.meshgrid( np.linspace(0.0, 1.0, buffer.shape[0]),
                                          np.linspace(0.0, 1.0, buffer.shape[1]),
                                          indexing='ij')
        coords = np.dstack((y_coords, x_coords))

        # render the objects in the layer
        for object in self.objects:
            y_min_index = max(0, int(object.y_min * height))
            y_max_index = min(height-1, int(object.y_max * height) + 1)

            x_min_index = max(0, int(object.x_min * width))
            x_max_index = min(width-1, int(object.x_max * width) + 1)
            coords_within_bounds = coords[y_min_index:y_max_index, x_min_index:x_max_index]

            bool_array, edge_distance_array = object.intersect(coords_within_bounds)
            object.render(bool_array, edge_distance_array, buffer, y_min_index, x_min_index)

        # now apply any effects
        for effect in self.effects:
            buffer = effect.apply(buffer)
        return buffer

    def add_circle(self, y, x, radius, edge_width, color, edge_color):
        self.objects.append(circle.Circle(y, x, radius, edge_width, color, edge_color))

    def add_rectangle(self, y, x, height, width, edge_width, color, edge_color):
        self.objects.append(rectangle.Rectangle(y, x, height, width, edge_width, color, edge_color))

    def add_polygon(self, coordinates, edge_width, color, edge_color):
        self.objects.append(polygon.Polygon(coordinates, edge_width, color, edge_color))

    def add_blur(self, standard_deviation):
        self.effects.append(blur.Blur(standard_deviation))

    def add_tint(self, tint_color, tint_strength):
        self.effects.append(tint.Tint(tint_color, tint_strength))
