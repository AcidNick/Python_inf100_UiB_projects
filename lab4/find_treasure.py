def find_treasure(grid, target_sum):
  coords = []
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if i + j + grid[i][j] == target_sum:
        coords.append([i, j])
  return coords
