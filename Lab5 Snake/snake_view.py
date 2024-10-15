def draw_board(canvas, x1, y1, x2, y2, board, info_mode, fruit_images):
  rows = len(board)
  cols = len(board[0])
  cell_width = (x2-x1)/cols
  cell_height = (y2-y1)/rows
  for row in range(rows):
    for col in range(cols):
      cell_x1 = x1 + cell_width*col
      cell_x2 = cell_x1 + cell_width
      cell_y1 = y1 + cell_height*row
      cell_y2 = cell_y1 + cell_height

      if board[row][col] <= 0:
        if (row % 2 == 0 and col % 2 == 0) or (row % 2 == 1 and col % 2 == 1):
          color = '#aad751'
        else:
          color = '#a2d149'
      else:
        color = 'green'

      canvas.create_rectangle(cell_x1, cell_y1, cell_x2, cell_y2, fill=color, outline='')
      if board[row][col] < 0:
        image_in_box(canvas, cell_x1, cell_y1, cell_x2, cell_y2, fruit_images[board[row][col]])
      if info_mode:
        cell_mid_x = (cell_x1 + cell_x2) / 2
        cell_mid_y = (cell_y1 + cell_y2) / 2
        canvas.create_text(cell_mid_x, cell_mid_y, text=f'{row},{col}\n{board[row][col]}')

from uib_inf100_graphics.helpers import image_in_box