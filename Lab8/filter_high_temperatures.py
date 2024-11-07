def filter_high_temperatures(path_input: str, path_output: str, threshold_temp: float) -> None:
    with open(path_input, "rt", encoding='utf-8') as input_file:
        with open(path_output, "wt", encoding='utf-8') as output_file:
            for line in input_file:
                if float(line.split(" ")[1]) >= threshold_temp:
                    output_file.write(line)

def test_filter_high_temperatures():
    print('Tester filter_high_temperatures... ', end='')
    filter_high_temperatures('temperatures.txt', 'high_temps.txt', 23.5)
    expected = (
        'Monday 23.5\n'
        'Wednesday 24.0\n'
        'Thursday 23.9\n'
        'Sunday 23.9\n'
    )
    with open('high_temps.txt', 'rt', encoding='utf-8') as file:
        actual = file.read()
    assert expected.strip() == actual.strip()
    print('OK')

if __name__ == '__main__':
    test_filter_high_temperatures()
