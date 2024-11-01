from pathlib import Path

def best_alignment(genome: str, pattern: str) -> int:
    last_difference = alignment_difference(genome, pattern, 0)
    position = 0
    maks = len(genome) - len(pattern) + 1
    for n in range(maks):
        current_difference = alignment_difference(genome, pattern, n)
        if current_difference <= last_difference:
            last_difference = current_difference
            position = n
    return position

def alignment_difference(genome: str, pattern: str, i: int) -> int:
    difference = 0
    genome_piece = genome[i:]
    for n in range(len(pattern)):
        if pattern[n] != genome_piece[n]:
            difference += 1
    return difference

def best_alignment_to_file(path: str, sequence: str) -> int:
    genome = Path(path).read_text(encoding="utf-8")
    return best_alignment(genome, sequence)

def test_best_alignment_to_file():
    print('Testing best_alignment_to_file...', end='')
    path = 'human_genome_excerpt.txt'
    assert 30864 == best_alignment_to_file(path, 'AAACAAAGAA')
    assert 2097 == best_alignment_to_file(path, 'GAGTGGGATGAGCCATTGTTCATCT')
    assert 0 == best_alignment_to_file(path, 'TAACCC' * 18)
    assert 49913 == best_alignment_to_file(path, 'CATTTCAGTAGTAATAGGAATCTCCAC')
    print(' OK')

if __name__ == '__main__':
    test_best_alignment_to_file()