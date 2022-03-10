# render2d
# A library to render high-quality 2D algorithmic art scenes

# David Berthiaume

import numpy as np
from PIL import Image

class Canvas:
    # this class defines our canvas which contain multiple layers in a dictionary
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.layers = dict()
        self.output = None

    def add_layer(self, label):
        # add a layer to the canvas with a label
        self.layers[label] = Layer(label, self.height, self.width)

    def get_layers(self):
        # get a list of all the layers in the canvas
        return self.layers.keys()

    def remove_layer(self, label):
        # remove a layer
        del self.layers[label]

    def get_number_of_layers(self):
        # get the number of layers in the canvas
        return len(self.layers)

    def render(self):
        # render the canvas by applying post processing effects to each layer and then combining them
        for key, item in self.layers.items():
            print (f'rendering layer {key}')
        self.output = np.zeros((self.height, self.width, 3), dtype=np.uint8)

    def save(self, file_name):
        if self.output is None:
            print ('Please render the canvas before saving it to a file')

        img = Image.fromarray(self.output, 'RGB')
        img.save(file_name)
        img.show()



class Layer:
    # this class defines a single layer within a canvas
    def __init__(self, label, height, width):
        self.height = height
        self.width = width
        self.label = label

        self.buffer = np.zeros((self.height, self.width, 4), dtype=np.float32)


