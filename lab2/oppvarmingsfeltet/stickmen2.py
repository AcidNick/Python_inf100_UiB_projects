from uib_inf100_graphics.simple import canvas, display

def draw_stickman(canvas, x, y):
  canvas.create_oval(60+x, 80+y, 140+x, 160+y)   # Head
  canvas.create_line(100+x, 160+y, 100+x, 280+y) # Body
  canvas.create_line(50+x, 180+y, 150+x, 180+y)  # Arms
  canvas.create_line(100+x, 280+y, 50+x, 330+y)  # Left leg
  canvas.create_line(100+x, 280+y, 150+x, 330+y) # Right leg

draw_stickman(canvas, 0, 0)
draw_stickman(canvas, 200, 0)
draw_stickman(canvas, 210, 10)

display(canvas)