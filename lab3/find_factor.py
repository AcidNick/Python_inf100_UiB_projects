def largest_factor_of(x):
  faktor = 0
  for i in range(1, x):
    if x % i == 0:
      faktor = i
  return faktor

def test_largest_factor_of():
    print('Testing largest_factor_of... ', end='')
    assert 3 == largest_factor_of(6)
    assert 1 == largest_factor_of(7)
    assert 4 == largest_factor_of(8)
    print('OK')

if __name__ == '__main__':
    test_largest_factor_of()
