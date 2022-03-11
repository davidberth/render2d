from render2d import canvas, rectangle
import numpy as np

height, width = 1000, 1000
canvas = canvas.Canvas()
front = canvas.add_layer('front', 1.0)
for y in np.linspace(0.0, 1.0, 40):
    for x in np.linspace(0.0, 1.0, 40):
        front.add_circle(y, x, 0.01, (1.0, np.random.uniform(0.0, 1.0), 0.0, 1.0))
        front.add_rectangle(y, x, 0.02, 0.02, (0.0, np.random.uniform(0.0, 1.0), 1.0, 1.0))

front.add_polygon(((0.3, 0.5), (0.5, 0.7), (0.5, 0.3), (0.4, 0.2)), (0.0, 1.0, 0.0, 1.0))
canvas.render(height, width)
canvas.save('output/test1.png')

