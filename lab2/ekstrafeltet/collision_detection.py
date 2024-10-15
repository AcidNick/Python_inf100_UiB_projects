def rectangles_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
  x_left_1 = min(x1, x2)
  x_right_1 = max(x1, x2)
  y_top_1 = min(y1, y2)
  y_bottom_1 = max(y1, y2)

  x_left_2 = min(x3, x4)
  x_right_2 = max(x3, x4)
  y_top_2 = min(y3, y4)
  y_bottom_2 = max(y3, y4)

  if x_right_1 < x_left_2 or x_right_2 < x_left_1 or y_top_2 > y_bottom_1 or y_top_1 > y_bottom_2:
    return False
  else:
    return True
  
print("Tester rectangles_overlap... ", end="")
assert rectangles_overlap(0, 0, 5, 5, 2, 2, 6, 6) is True # Delvis overlapp
assert rectangles_overlap(0, 5, 5, 0, 1, 1, 4, 4) is True # Fullstendig overlapp
assert rectangles_overlap(0, 1, 7, 2, 1, 0, 2, 7) is True # Kryssende rektangler
assert rectangles_overlap(0, 5, 5, 0, 5, 5, 7, 7) is True # Deler et hjørne
assert rectangles_overlap(0, 0, 5, 5, 3, 6, 5, 8) is False # Utenfor
print("OK")

from point_in_rectangle import point_in_rectangle
from distance import distance

def circle_overlaps_rectangle(x1, y1, x2, y2, xc, yc, rc):
  x_left = min(x1, x2)
  x_right = max(x1, x2)
  y_top = min(y1, y2)
  y_bottom = max(y1, y2)

  ut_x1 = x_left-rc
  ut_y1 = y_top-rc
  ut_x2 = x_right+rc
  ut_y2 = y_bottom+rc

  if point_in_rectangle(x1, y1, x2, y2, xc, yc):
    return True
  elif not point_in_rectangle(ut_x1, ut_y1, ut_x2, ut_y2, xc, yc):
    return False
  elif x1 < xc < x2:
    return True
  elif y1 < yc < y2:
    return True
  elif distance(x1, y1, xc, yc) < rc:
    return True
  elif distance(x1, y2, xc, yc) < rc:
    return True
  elif distance(x2, y1, xc, yc) < rc:
    return True
  elif distance(x2, y2, xc, yc) < rc:
    return True
  else:
    return False
  
print("Tester circle_overlaps_rectangle... ", end="")
assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 2.5, 2) is True # på midten
assert circle_overlaps_rectangle(0, 5, 5, 0, 8, 3, 2) is False # langt utenfor
assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 7, 2.01) is True # på kanten
assert circle_overlaps_rectangle(0, 5, 5, 0, 5.1, 5.1, 1) is True # på hjørnet
assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 8.99, 5) is True # på hjørnet
assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 9.01, 5) is False # bare nesten

# assert circle_overlaps_rectangle(2, 2, 5, 5, 1, 1, 2) is True
print("OK")