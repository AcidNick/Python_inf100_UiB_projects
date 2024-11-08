def string_to_data(content_string:str) -> list:
    result = []
    for char in content_string:
        bit_list = [int(x) for x in f'{ord(char):08b}']
        result.extend(bit_list)
    return result

def get_core_bit_list(content_string:str) -> list:
    data = string_to_data(content_string)
    my_len = len(content_string)
    length = [int(x) for x in f'{my_len:08b}']
    head = [0, 1, 0, 0]
    term = [0,0,0,0]
    return head + length + data + term

def pad_bit_list(core_bit_list: list, pad_to_bytes: int) -> None:
    pad1 = (1, 1, 1, 0, 1, 1, 0, 0)
    pad2 = (0, 0, 0, 1, 0, 0, 0, 1)
    target_length = pad_to_bytes * 8
    current_length = len(core_bit_list)
    if current_length >= target_length:
        return
    pad_length = target_length - current_length
    pad_list = []
    while len(pad_list) < pad_length:
        pad_list.extend(pad1 if len(pad_list) // len(pad1) % 2 == 0 else pad2)
    pad_list = pad_list[:pad_length]
    core_bit_list.extend(pad_list)

from qr6_error_correction import generate_error_correction

def string_to_bit_list(content_string: str, qr_layout: dict):
    core_bit_list = get_core_bit_list(content_string)

    total_bits = qr_layout['byte_capacity'] * 8
    error_correction_levels = {'L': 80, 'M': 128, 'Q': 176, 'H': 224}

    error_correction_level = None
    for level in ['L', 'M', 'Q', 'H']:
        # error correction bits
        ec_bits = error_correction_levels[level]
        available_bits = total_bits - ec_bits
        if len(core_bit_list) <= available_bits:
            error_correction_level = level
            break
    if error_correction_level is None:
        raise ValueError("Data er for stor til å passe i QR-koden selv med det laveste nivået av feilretting.")

    # Padding
    pad_size_bytes = (available_bits + 7) // 8  # Runder opp til nærmeste byte
    pad_bit_list(core_bit_list, pad_size_bytes)

    final_bit_list = generate_error_correction(core_bit_list, error_correction_level)

    return final_bit_list, error_correction_level


def test_string_to_data():
    print('Testing string_to_data...', end='')
    assert [0,1,0,0,0,0,0,1] == string_to_data('A')
    assert [0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,1] == string_to_data('AC')
    foo = [0,1,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1]
    assert foo == string_to_data('foo')
    print(' OK')

def test_get_core_bit_list():
    print('Testing get_core_bit_list...', end='')
    arg = 'hei'
    expected_head = [0, 1, 0, 0]
    expected_len = [0, 0, 0, 0, 0, 0, 1, 1] # 3 in binary
    expected_data = [int(x) for x in '011010000110010101101001']
    expected_term = [0, 0, 0, 0]
    expected = expected_head + expected_len + expected_data + expected_term

    actual = get_core_bit_list(arg)
    assert expected == actual
    print(' OK')


def test_pad_bit_list():
    print('Testing pad_bit_list...', end='')
    PAD1 = (1, 1, 1, 0, 1, 1, 0, 0)
    PAD2 = (0, 0, 0, 1, 0, 0, 0, 1)

    arg = [1, 1, 1, 1, 1, 1, 1, 1]
    expected = arg + list(PAD1) + list(PAD2) + list(PAD1)
    pad_bit_list(arg, 4)
    assert expected == arg

    arg = [1, 1, 1, 1, 1, 1, 1, 1]
    expected = arg + list(PAD1) + list(PAD2) + list(PAD1) + list(PAD2)
    pad_bit_list(arg, 5)
    assert expected == arg

    arg = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
    expected = arg + list(PAD1) + list(PAD2) + list(PAD1) + list(PAD2)
    pad_bit_list(arg, 6)
    assert expected == arg
    print(' OK')


if __name__ == '__main__':
    test_string_to_data()
    test_get_core_bit_list()
    test_pad_bit_list()