def sequence_for(n):
  tall = ''
  for num in range(0, n+1):
    tall += f'{num} '
  return tall

def sequence_while(n):
  tall = ''
  i = 0
  while i <= n:
    tall += f'{i} '
    i += 1
  return tall

print("Tester sequence_for... ", end="")
assert "0 1 2 3 4 5 " == sequence_for(5)
assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_for(10)
assert "0 " == sequence_for(0)
print("OK")

print("Tester sequence_while... ", end="")
assert "0 1 2 3 4 5 " == sequence_while(5)
assert "0 1 2 3 4 5 6 7 8 9 10 " == sequence_while(10)
assert "0 " == sequence_while(0)
print("OK")
