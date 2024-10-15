def cross_sum(x):
  sum = 0
  for n in str(x):
    sum += int(n)
  return sum

def nth_cross_sum(n, x):
  i = 0
  tall = 0
  while i < n:
    tall += 1
    if cross_sum(tall) == x:
      i += 1
  return tall

print(nth_cross_sum(3, 7))
