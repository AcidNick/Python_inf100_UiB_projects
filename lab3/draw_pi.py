from uib_inf100_graphics.simple import canvas, display
import random

def draw_dot(canvas, x, y, color):
    canvas.create_oval(x-5, y-5, x+5, y+5, fill=color)

def distance(x1, y1, x2, y2):
  return ((x2-x1)**2 + (y2-y1)**2)**0.5

# Draw a circle in the window
canvas.create_oval(0, 0, 400, 400)
n = 1000
antall = 0
for i in range(n + 1):
  color = 'orange'
  # Highlight a random point on 400x400 canvas
  x = random.random() * 400
  y = random.random() * 400
  if distance(x, y, 200, 200) > 200:
     color = 'gray'
  else:
    antall += 1
  draw_dot(canvas, x, y, color)

beregnet_pi = (antall/n)*4
message = f'{antall}/{n} prikker traff sirkelen\nBeregnet pi: {beregnet_pi}'
canvas.create_rectangle(100, 180, 300, 220, fill='white')
canvas.create_text(200, 200, text=message, fill='black', font=('TkDefaultFont', 10), justify='center')

display(canvas)

