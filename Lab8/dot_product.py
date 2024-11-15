def dot_product(a: list, b: list):
    # for i in range(len(a)):
    #     a[i] *= b[i] # Destruktiv
    products = [a[i] * b[i] for i in range(len(a))] # Ikke destruktiv
    return sum(products)

def test_dot_product():
    print('Tester dot_product... ', end='')
    assert 36 == dot_product([1, 2, 3, 4], [4, 5, 6, 1])
    assert 12 == dot_product([0, 6, 1], [400, 1, 6])
    assert 651 == dot_product([43, 6], [15, 1])
    print('OK')

if __name__ == '__main__':
    test_dot_product()
