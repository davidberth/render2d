from render2d.renderable import Renderable
import numpy as np

class Polygon(Renderable):
    def __init__(self, coordinates, edge_width, color, edge_color):
        self.coordinates = np.array(coordinates)
        self.num_coordinates = len(coordinates)
        self.edge_width = edge_width
        self.color = color
        self.edge_color = edge_color
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
        min_edge_distance = np.ones( (coords.shape[0], coords.shape[1]), dtype=np.float32)

        for i in range(self.num_coordinates):
            coord1 = self.coordinates[i, :]
            coord2 = self.coordinates[(i+1) % self.num_coordinates, :]
            vector = (coord2[0] - coord1[0], coord2[1] - coord1[1])
            vector_length = np.sqrt(vector[0]**2 + vector[1]**2)
            rel_coords = coords - coord1

            outside = vector[0] * rel_coords[:, :, 1] - vector[1] * rel_coords[:, :, 0]
            edge_distance = np.absolute(outside) / vector_length
            min_edge_distance = np.minimum(edge_distance, min_edge_distance)
            mask[outside > 0.0] = False

        return mask, min_edge_distance

