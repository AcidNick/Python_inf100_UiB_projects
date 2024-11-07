def set_fixed_fields(matrix:list, qr_layout:dict) -> list:
    for row, col in qr_layout['fixed_positions']['zeros']:
        matrix[row][col] = 0
    for row, col in qr_layout['fixed_positions']['ones']:
        matrix[row][col] = 1
    return matrix

def set_meta_fields(matrix:list, err_corr:str, mask_no:int, qr_layout:dict) -> list:
    pattern = qr_layout['meta_patterns'][err_corr][mask_no]
    pattern_position_first = qr_layout['meta_positions']['first']
    pattern_position_second = qr_layout['meta_positions']['second']
    for i in range(len(pattern_position_first)):
        row, col = pattern_position_first[i]
        matrix[row][col] = pattern[i]
        row, col = pattern_position_second[i]
        matrix[row][col] = pattern[i]
    return matrix

def test_set_fixed_fields():
    print('Testing set_fixed_fields...', end='')
    matrix = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]
    sample_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 5,
        'fixed_positions': {
            'zeros': [
                [3, 2], [3, 3], [3, 4], [4, 2], [4, 3], [4, 4]
            ],
            'ones': [
                [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]
            ]
        }
        # skipping keys 'byte_capacity', 'meta_positions' and 'meta_patterns'
        # since they are irrelevant here
    }
    set_fixed_fields(matrix, sample_layout)
    assert matrix == [
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ]

    print(' OK')

def test_set_meta_fields():
    print('Testing set_meta_fields...', end='')
    # For easier visualization the test uses a matrix of strings rather
    # than 0's and 1's, but ultimately 1's and 0's should also work
    matrix = [
        ['-', '|', '-', '|', '-'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
    ]
    sample_layout = {
        'about': 'A fake and incomplete QR layout for testing only',
        'side_length': 5,
        # skipping key 'fixed_positions' since it is irrelevant here
        'meta_positions': {
            'first': [
                [0, 0], [0, 1], [0, 2]
            ],
            'second': [
                [0, 4], [4, 4], [3, 1]
            ]
        },
        'meta_patterns': {
            'L': [
                ['A', 'B', 'C'], # mask_no = 0
                ['a', 'b', 'c']  # mask_no = 1
            ],
            'Q': [
                ['Q', 'R', 'S'], # mask_no = 0
                ['q', 'r', 's']  # mask_no = 1
            ],
        }
    }
    err_corr = 'L'
    mask_no = 0
    set_meta_fields(matrix, err_corr, mask_no, sample_layout)
    assert matrix == [
        ['A', 'B', 'C', '|', 'A'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', 'C', '|', '-', '|'],
        ['-', '|', '-', '|', 'B'],
    ]

    err_corr = 'Q'
    mask_no = 1
    set_meta_fields(matrix, err_corr, mask_no, sample_layout)
    assert matrix == [
        ['q', 'r', 's', '|', 'q'],
        ['|', '-', '|', '-', '|'],
        ['-', '|', '-', '|', '-'],
        ['|', 's', '|', '-', '|'],
        ['-', '|', '-', '|', 'r'],
    ]

    print(' OK')


if __name__ == '__main__':
    test_set_fixed_fields()
    test_set_meta_fields()
    from qr_dummies import sample_masked_matrix
    from qr1_draw import display
    from pathlib import Path
    import json

    # Retrieve sample of premasked matrix without meta/fixed fields
    # and getting the matching config for it.
    matrix, error_correction_level, mask_no = sample_masked_matrix()
    qr_layout = json.loads(Path('qrv2_layout.json').read_text(encoding='utf-8'))

    # Try the functions we have created here
    set_meta_fields(matrix, error_correction_level, mask_no, qr_layout)
    set_fixed_fields(matrix, qr_layout)

    # Draw the picture
    display(matrix)