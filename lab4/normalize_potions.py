def normalize_potions(levels):
  if levels == []:
      return []
  x_min = min(levels)
  x_max = max(levels)
  x_delta = x_max - x_min
  if x_delta == 0:
      return [x/x_min for x in levels]
  return [round((x-x_min)/x_delta, 2) for x in levels]


def lists_almost_equal(list_a, list_b):
    if len(list_a) != len(list_b):
        return False
    for i, a in enumerate(list_a):
        if abs(a - list_b[i]) > 0.00000001:
            return False
    return True

def test_normalize_potions():
    def do_test(arg, expected):
        print('.', end='')
        arg_copy = arg.copy()
        actual = normalize_potions(arg)

        assert arg_copy == arg, (
            'Argument was unexpectedly mutated. '
            f'Was first {arg_copy} but is now {arg}.'
        )
        assert lists_almost_equal(expected, actual), (
            f'On input {arg} we expected {expected} '
            f'but got {actual}.'
        )
    
    print('Testing normalize_potions', end='')
    do_test(arg=[1, 2, 3, 4, 5], expected=[0, 0.25, 0.5, 0.75, 1])
    do_test(arg=[3, 2, 1, 0, -1], expected=[1, 0.75, 0.5, 0.25, 0])
    do_test(arg=[0.02, 0.01, 0.05, 0.03], expected=[0.25, 0.0, 1.0, 0.5])
    do_test(arg=[3, 3, 3], expected=[1, 1, 1])
    do_test(arg=[9], expected=[1])
    do_test(arg=[], expected=[])
    print(' OK')

if __name__ == '__main__':
    test_normalize_potions()
