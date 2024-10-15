from math import sqrt

def circles_overlap(x1, y1, r1, x2, y2, r2):
  sum_r = r1 + r2
  avstand = sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
  overlapp = False
  if avstand <= sum_r:
    overlapp = True
  return overlapp


# Sirkel1 med sentrum (0, 0) og radius 1
# Sirkel2 med sentrum (1, 1) og radius 1
# Overlapper
print(circles_overlap(0, 0, 1, 1, 1, 1)) # Skal skrive ut True

# Sirkel1 med sentrum (0, 0) og radius 2
# Sirkel2 med sentrum (4, 1) og radius 2
# Overlapper ikke
print(circles_overlap(0, 0, 2, 4, 1, 2)) # Skal skrive ut False

# Sirkel1 med sentrum (0, 0) og radius 3
# Sirkel2 med sentrum (5, 0) og radius 2
# De overlapper hverandre i et enkelt punkt
print(circles_overlap(0, 0, 3, 5, 0, 2)) # Skal skrive ut True