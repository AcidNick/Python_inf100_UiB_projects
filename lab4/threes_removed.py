def threes_removed(a):
  list = a.copy()
  for e in a:
    if e == 3:
      list.remove(e)
  return list
