def draw_multicolored_flag(canvas, x1, y1, x2, y2, colors):
  for i in range(len(colors)):
    bredde = (x2-x1)/len(colors)
    x_start = x1+bredde*i
    canvas.create_rectangle(x_start, y1, x_start+bredde, y2, fill=colors[i], outline="")