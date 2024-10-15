def count_xs(s):
  x_count = 0
  for char in s:
    if char.lower() == 'x':
      x_count += 1
  return x_count

print(count_xs('xxCoolDragonSlayer99xx')) # 4

# print('Tester count_xs... ', end='')
# assert 0 == count_xs('foo bar hei')
# assert 1 == count_xs('x')
# assert 4 == count_xs('xxCoolDragonSlayer99xx')
# print('OK')
