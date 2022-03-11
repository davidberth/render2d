from render2d.renderable import Renderable
import numpy as np

class Polygon(Renderable):
    def __init__(self, coordinates, color):
        self.coordinates = np.array(coordinates)
        self.num_coordinates = len(coordinates)
        self.color = color
        self.get_bounds()

    def get_bounds(self):
        self.y_min = np.min(self.coordinates[:,0])
        self.y_max = np.max(self.coordinates[:,0])
        self.x_min = np.min(self.coordinates[:,1])
        self.x_max = np.max(self.coordinates[:,1])


    def intersect(self, coords):

        # we traverse the edge segments and determine which side the point
        # is on

        mask = np.ones( (coords.shape[0], coords.shape[1]), dtype=np.bool)

        for i in range(self.num_coordinates):
            coord1 = self.coordinates[i, :]
            coord2 = self.coordinates[(i+1) % self.num_coordinates, :]
            vector = (coord2[0] - coord1[0], coord2[1] - coord1[1])
            rel_coords = coords - coord1

            outside = vector[0] * rel_coords[:, :, 1] - vector[1] * rel_coords[:, :, 0]
            mask[outside > 0.0] = False

        # This will not work
        return mask

