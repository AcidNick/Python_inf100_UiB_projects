def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def collect_collatz(a: int, b: int) -> dict:
    sequence = {}
    for i in range(a, b):
        sequence[i] = collatz_sequence(i)
    return sequence

def test_collect_collatz():
    print('Tester collect_collatz... ', end='')

    # Test 1
    expected = {
        1: [1],
        2: [2, 1],
        3: [3, 10, 5, 16, 8, 4, 2, 1],
    }
    actual = collect_collatz(1, 4)
    assert expected == actual

    # Test 2
    expected = {
        3: [3, 10, 5, 16, 8, 4, 2, 1],
        4: [4, 2, 1],
        5: [5, 16, 8, 4, 2, 1],
    }
    actual = collect_collatz(3, 6)
    assert expected == actual
    print('OK')

if __name__ == '__main__':
    test_collect_collatz()
