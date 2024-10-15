def alternate_sign_sum(nums):
  sum = 0
  for i in range(len(nums)):
    sum += (-1)**(i+2) * nums[i]
  return sum

def test_alternate_sign_sum():
    print('Tester alternate_sign_sum... ', end='')
    assert 3 == alternate_sign_sum([1, 2, 3, 4, 5])
    assert 30 == alternate_sign_sum([10, 20, 30, 40, 50])

    a = [-10, 20, -30, 40, -50]
    assert -150 == alternate_sign_sum([-10, 20, -30, 40, -50])
    assert [-10, 20, -30, 40, -50] == a # Sjekk at funksjon ikke er destruktiv
    print('OK')

if __name__ == '__main__':
  test_alternate_sign_sum()