from render2d import render2d

height, width = 100, 100
canvas = render2d.Canvas(height, width)
canvas.add_layer('front')
canvas.add_layer('back')
canvas.render()
canvas.save('output/test1.png')