from math import sqrt

def distance(x1, y1 ,x2, y2):
  return sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)

from math import isclose
print("Tester distance... ", end="")
assert isclose(3, distance(103, 42, 100, 42))
assert isclose(4, distance(2, 100, 2, 104))
assert isclose(5, distance(0, 3, 4, 0))
assert isclose(1.414213562373, distance(0, 0, 1, 1))
assert isclose(1.414213562373, distance(3, 4, 2, 3))
print("OK")