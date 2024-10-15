from pathlib import Path

def total_income(path):
    sales = Path(path).read_text(encoding='utf-8').splitlines()
    sales_table = [sale.split(',') for sale in sales]
    data = sales_table[1:]
    revenue = 0
    for product in data:
        revenue += (int(product[2])-int(product[1]))*int(product[3])
    return revenue

def test_total_income():
    print('Tester total_income... ', end='')
    expected = (
        (50 - 10) * 100
        + (100 - 20) * 50
        + (500 - 50) * 10
        + (1000 - 100) * 5
        + (10000 - 500) * 2
    )
    actual = total_income('sales.csv')
    assert expected == actual, f'{expected=}, {actual=}'
    print('OK')

if __name__ == '__main__':
    test_total_income()