from uib_inf100_graphics.simple import canvas, display

canvas.create_polygon(10, 20, 390, 90, 10, 90)
canvas.create_polygon(10, 110, 390, 190, 10, 190,
                      fill='', outline='red', width=3) # fill='' -> no fill

points = [50, 210, 390, 290, 50, 290, 390, 210]
canvas.create_polygon(points, fill='lightGreen', outline='black', width=1)

points = [(10, 310), (390, 390), (50, 390), (390, 310)]
canvas.create_polygon(points, fill='darkblue', smooth=True)

display(canvas)
