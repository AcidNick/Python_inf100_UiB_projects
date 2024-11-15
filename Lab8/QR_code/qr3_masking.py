def should_flip(row:int, col:int, mask_no:int) -> bool:
    mask_list = [
        (row + col) % 2 == 0,
        row % 2 == 0,
        col % 3 == 0,
        (row + col) % 3 == 0,
        (row // 2 + col // 3) % 2 == 0,
        (row * col) % 2 + (row * col) % 3 == 0,
        ((row * col) % 2 + (row * col) % 3) % 2 == 0,
        ((row + col) % 2 + (row * col) % 3) % 2 == 0
    ]
    return mask_list[mask_no]

def get_masked_matrix(matrix: list, mask_no: int) -> list:
    masked_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            masked_matrix[row][col] = 1 - matrix[row][col] if\
                should_flip(row, col, mask_no) else matrix[row][col]
    return masked_matrix

def score_matrix(matrix:list) -> int:
    score = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            score += 1 if matrix[row][col] == 1 else -1
    return abs(score)

def get_refined_matrix(raw_matrix:list, error_correction_level: str, qr_layout:dict) -> list:
    from qr2_matrix_completion import set_fixed_fields, set_meta_fields
    best_matrix = get_masked_matrix(raw_matrix, 0)
    set_meta_fields(best_matrix, error_correction_level, 0, qr_layout)
    set_fixed_fields(best_matrix, qr_layout)
    best_score = score_matrix(best_matrix)
    for mask in range(8):
        masked_matrix = get_masked_matrix(raw_matrix, mask)
        set_meta_fields(masked_matrix, error_correction_level, mask, qr_layout)
        set_fixed_fields(masked_matrix, qr_layout)
        score = score_matrix(masked_matrix)
        if score < best_score:
            best_score = score
            best_matrix = masked_matrix
    return best_matrix

def test_get_masked_matrix():
    print('Testing get_masked_matrix...', end='')
    blank_5x5_matrix = [[0] * 5 for _ in range(5)]

    actual = get_masked_matrix(blank_5x5_matrix, 0)
    expected = [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
    ]
    assert expected == actual
    assert blank_5x5_matrix == [[0] * 5 for _ in range(5)]

    actual = get_masked_matrix(expected, 1)
    expected = [
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
    ]
    assert expected == actual
    print(' OK')

def test_score_matrix():
    arg = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert 5 == score_matrix(arg)

    arg = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    assert 1 == score_matrix(arg)


if __name__ == '__main__':
    test_get_masked_matrix()
    test_score_matrix()