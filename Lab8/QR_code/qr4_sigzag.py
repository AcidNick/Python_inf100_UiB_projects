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

if __name__ == '__main__':
    test_get_next_pos_basic()