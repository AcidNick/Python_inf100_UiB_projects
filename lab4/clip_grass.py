def clip_grass(heights, max_height):
  for i in range(len(heights)):
    if heights[i] > max_height:
      heights[i] = max_height
