def color_train_A(canvas, x, y, colors):
  for i in range(len(colors)):
    canvas.create_rectangle(x+15*i, y, x+15*i+15, y+10, fill = colors[i])

def color_train_B(canvas, x, y, width, height, colors):
  bredde = width / len(colors)
  for i in range(len(colors)):
    canvas.create_rectangle(x+bredde*i, y, x+bredde*i+bredde, y+height, fill = colors[i])

def color_train_C(canvas, x1, y1, x2, y2, colors):
  width = x2-x1
  height = y2-y1
  bredde = width / len(colors)
  for i in range(len(colors)):
    canvas.create_rectangle(x1+bredde*i, y1, x1+bredde*i+bredde, y1+height, fill = colors[i])

