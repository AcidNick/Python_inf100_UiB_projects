def parity(x):
    if x % 2 == 0:
      return 'Partall'
    else:
      return 'Oddetall'

print("Tester parity... ", end="")
assert "Partall" == parity(0)
assert "Oddetall" == parity(1) 
assert "Partall" == parity(42)
assert "Oddetall" == parity(99)
print("OK")