def rotate(grid, clockwise):
  n = len(grid[0]) # Kolonner
  m = len(grid) # Rader
  rotated = [[None] * m for i in range(n)]
  for row in range(m):
    for col in range(n):
      rotated[col][row] = grid[-1-row][col] if clockwise else grid[row][-1-col]
  return rotated