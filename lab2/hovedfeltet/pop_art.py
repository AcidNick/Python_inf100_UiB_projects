from uib_inf100_graphics.simple import canvas, display

def drawPopArt(canvas, x1, y1, scale):
  scale = scale*0.25
  points_cheese = [((10)*scale+x1, (33)*scale+y1), ((120)*scale+x1, (363)*scale+y1), ((280)*scale+x1 ,(33)*scale+y1)]
  canvas.create_polygon(points_cheese, fill='gold2')

  points_crust = [((10)*scale+x1, (33)*scale+y1), ((135)*scale+x1, (-7)*scale+y1,), ((280)*scale+x1, (33)*scale+y1)]
  canvas.create_line(points_crust, fill='orangeRed3', width=40*scale, smooth=True)

  canvas.create_oval((100)*scale+x1, (43)*scale+y1, (150)*scale+x1, (93)*scale+y1, fill='red3')
  canvas.create_oval((120)*scale+x1, (143)*scale+y1, (170)*scale+x1, (193)*scale+y1, fill='red3')
  canvas.create_oval((110)*scale+x1, (223)*scale+y1, (160)*scale+x1, (273)*scale+y1, fill='red3')
  canvas.create_oval((50)*scale+x1, (103)*scale+y1, (100)*scale+x1, (153)*scale+y1, fill='red3')
  canvas.create_oval((180)*scale+x1, (73)*scale+y1, (230)*scale+x1, (123)*scale+y1, fill='red3')
  return None

drawPopArt(canvas, 10, 10, 1)
drawPopArt(canvas, 250, 10, 2)
drawPopArt(canvas, 10, 250, 1.5)
drawPopArt(canvas, 250, 200, 2)
drawPopArt(canvas, 75, 75, 2.5)
display(canvas)