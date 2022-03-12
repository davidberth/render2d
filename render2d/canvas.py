import numpy as np
from PIL import Image

from render2d.layer import Layer

class Canvas:
    # this class defines our canvas which contain multiple layers in a dictionary
    def __init__(self):
        self.layers = dict()
        self.output = None

    def add_layer(self, label, depth):
        # add a layer to the canvas with a label
        self.layers[label] = Layer(label, depth)
        return self.layers[label]

    def get_layers(self):
        # get a list of all the layers in the canvas
        return self.layers.keys()

    def remove_layer(self, label):
        # remove a layer
        del self.layers[label]

    def get_number_of_layers(self):
        # get the number of layers in the canvas
        return len(self.layers)

    def render(self, height, width):
        # render the canvas by applying post-processing effects to each layer and then combining them
        self.output = np.zeros((height, width, 4), dtype=np.float32)
        for key, item in self.layers.items():
            print (f'rendering layer {key}')
            self.output += item.render(height, width)
        self.output*=255.0
        print (np.max(self.output))

    def save(self, file_name):
        if self.output is None:
            print ('Please render the canvas before saving it to a file')
        print (f'Canvas size is {self.output.shape}')
        img = Image.fromarray(self.output[:,:,:3].astype(np.uint8), 'RGB')
        img.save(file_name)
        img.show()