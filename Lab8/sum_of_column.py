import csv

def sum_of_column(path, col) -> float:
    with open(path, "r", encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        total = 0.0
        for row in csv_reader:
            try:
                float(row[col])
            except (ValueError, IndexError):
                continue
            total += float(row[col])
    return total

def test_sum_of_column():
    print('Tester sum_of_column... ', end='')
    assert(42.0 == sum_of_column('foo.csv', 0))
    assert(95.0 == sum_of_column('foo.csv', 1))
    assert(0.0 == sum_of_column('foo.csv', 2))
    assert(76363.0 == sum_of_column('Statistikk_Tilsyn_ar.csv', 1))
    assert(46007.0 == sum_of_column('Statistikk_Tilsyn_ar.csv', 2))
    assert(5024518.0 == sum_of_column('airport-codes.csv', 3))
    print('OK')

if __name__ == '__main__':
    test_sum_of_column()
