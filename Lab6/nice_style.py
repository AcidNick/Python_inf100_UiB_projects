def good_style(source_code: str) -> bool:
    lines = source_code.splitlines()
    return all([len(line) <= 79 for line in lines])

def good_style_from_file(filename: str) -> bool:
    file = Path(filename).read_text(encoding='utf-8')
    return good_style(file)


# All([]) returnerer True hvis alle elementene i listen er True,
# eller hvis listen er tom, ellers False.
# https://www.geeksforgeeks.org/python-all-function/


def test_good_style():
    print('Tester good_style... ', end='')
    assert good_style('''\
def distance(x0, y0, x1, y1):
    return ((x0 - x1)**2 + (y0 - y1)**2)**0.5
''') is True
    assert good_style((('x' * 79) + '\n') * 20) is True
    assert good_style('x' * 80) is False
    assert good_style(
          (('x' * 79) + '\n') * 5
        + (('x' * 80) + '\n')
        + (('x' * 79) + '\n') * 5
    ) is False
    print('OK')

def test_good_style_from_file():
    print('Tester good_style_from_file... ', end='')
    assert good_style_from_file('test_file1.py') is True
    assert good_style_from_file('test_file2.py') is False
    assert good_style_from_file('test_file3.py') is False
    assert good_style_from_file('nice_style.py') is True
    print('OK')


if __name__ == '__main__':
    from pathlib import Path
    test_good_style()
    test_good_style_from_file()
