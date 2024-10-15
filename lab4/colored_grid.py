def draw_grid(canvas, x1, y1, x2, y2, color_grid):
  rows = len(color_grid)
  cols = len(color_grid[0])
  cell_width = (x2-x1)/cols
  cell_height = (y2-y1)/rows
  for row in range(rows):
    for col in range(cols):
      cell_x1 = x1 + cell_width*col
      cell_x2 = cell_x1 + cell_width
      cell_y1 = y1 + cell_height*row
      cell_y2 = cell_y1 + cell_height
      color = color_grid[row][col]
      canvas.create_rectangle(cell_x1, cell_y1, cell_x2, cell_y2, fill=color)