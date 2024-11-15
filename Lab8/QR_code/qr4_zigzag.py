def get_next_pos(row:int, column:int, size:int) -> tuple:
    if column % 2 == 0:
        # Hvis partallskolonne, flytt venstre med mindre
        # man er i første kolonne, da flytt opp
        return (row, column - 1) if column > 0 else (row - 1, column)
    # Resten vil være oddetallskolonne
    elif column % 4 == 1:
        # Hvis én mer enn delelig med fire, flytt ned og høgre
        # om mulig, ellers flytt venstre
        return (row + 1, column + 1) if row < size - 1 else (row, column - 1)
    else:
        # Flytt opp til høgre om mulig, ellers flytt venstre
        return (row - 1, column + 1) if row > 0 else (row, column - 1)

def bit_list_to_raw_matrix(bit_list:list, qr_layout:dict) -> list:
    matrix = [[0]*qr_layout['side_length'] for _ in range(qr_layout['side_length'])]
    illegal_positions = set()
    for row, col in qr_layout['fixed_positions']['zeros']:
        illegal_positions.add((row, col))
    for row, col in qr_layout['fixed_positions']['ones']:
        illegal_positions.add((row, col))
    pattern_position_first = qr_layout['meta_positions']['first']
    pattern_position_second = qr_layout['meta_positions']['second']
    for i in range(len(pattern_position_first)):
        row, col = pattern_position_first[i]
        illegal_positions.add((row, col))
        row, col = pattern_position_second[i]
        illegal_positions.add((row, col))

    size = qr_layout['side_length']
    current_pos = (size-1, size-1)
    possible_bit_length = size * size - len(illegal_positions)
    if len(bit_list) > possible_bit_length:
        raise ValueError(
            f'Too many bits ({len(bit_list)}) for a {size}x{size} matrix (max: {possible_bit_length})'
        )
    for i in range(size * size):
        if current_pos in illegal_positions:
            current_pos = get_next_pos(current_pos[0], current_pos[1], size)
            continue
        if bit_list:
            bit = bit_list.pop(0)
        else:
            bit = 0
        matrix[current_pos[0]][current_pos[1]] = bit
        current_pos = get_next_pos(current_pos[0], current_pos[1], size)
    return matrix



def test_get_next_pos_basic():
    print('Testing get_next_pos (basic)...', end='')
    size = 25
    # De første flyttene
    assert (24, 23) == get_next_pos(24, 24, size)
    assert (23, 24) == get_next_pos(24, 23, size)
    assert (23, 23) == get_next_pos(23, 24, size)
    ...
    # Når vi har sikksakket helt til topps
    assert (0, 23) == get_next_pos(0, 24, size)
    assert (0, 22) == get_next_pos(0, 23, size)
    assert (0, 21) == get_next_pos(0, 22, size)
    assert (1, 22) == get_next_pos(0, 21, size)
    assert (1, 21) == get_next_pos(1, 22, size)
    assert (2, 22) == get_next_pos(1, 21, size)
    ...
    # Når vi har ned helt til bunns igjen
    assert (24, 20) == get_next_pos(24, 21, size)
    assert (24, 19) == get_next_pos(24, 20, size)
    ...
    # Siste kolonne
    assert (24, 0) == get_next_pos(24, 1, size)
    assert (23, 0) == get_next_pos(24, 0, size)
    assert (22, 0) == get_next_pos(23, 0, size)
    print(' OK')

def test_bit_list_to_raw_matrix():
    print('Testing bit_list_to_raw_matrix...', end='')
    # To make the test easier to read, bit_list contain distinct elements here
    # (in actual applications, bit_list would only have 0's and 1's)
    arg_bit_list = list(range(1, 72))
    arg_qr_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 9,
        'fixed_positions': {
            'ones': [
                [1, 3], [1, 4],
            ],
            'zeros': [
                [2, 3], [2, 4],
            ]
        },
        'meta_positions': {
            'first': [
                [5, 2], [5, 3]
            ],
            'second': [
                [6, 2], [6, 3]
            ]
        }
        # key 'meta_patterns' skipped, since it is irrelevant for this task
    }

    expected = [
        [ 0, 50, 49, 48, 47, 20, 19, 18, 17],
        [ 0, 52, 51,  0,  0, 22, 21, 16, 15],
        [71, 54, 53,  0,  0, 24, 23, 14, 13],
        [70, 56, 55, 46, 45, 26, 25, 12, 11],
        [69, 58, 57, 44, 43, 28, 27, 10,  9],
        [68, 59,  0,  0, 42, 30, 29,  8,  7],
        [67, 60,  0,  0, 41, 32, 31,  6,  5],
        [66, 62, 61, 40, 39, 34, 33,  4,  3],
        [65, 64, 63, 38, 37, 36, 35,  2,  1]
    ]
    actual = bit_list_to_raw_matrix(arg_bit_list, arg_qr_layout)
    assert expected == actual
    print(' OK')


if __name__ == '__main__':
    test_get_next_pos_basic()
    test_bit_list_to_raw_matrix()