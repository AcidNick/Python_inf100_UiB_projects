def filter_dangerous(plants, dangerous_plants):
  safe_plants = plants.copy()
  for e in dangerous_plants:
    if e in safe_plants:
      safe_plants.remove(e)
  return safe_plants

