from pathlib import Path

# Hjelpefunkjson som returnerer en mengde med data fra filen.
def read_genetic_data(file_path: str) -> set:
    genetic_data = Path(file_path).read_text().splitlines()
    return set(genetic_data)


def count_overlap(path1: str, path2: str) -> int:
    first_genetic_set = read_genetic_data(path1)
    second_genetic_set = read_genetic_data(path2)
    overlap = first_genetic_set.intersection(second_genetic_set)
    return len(overlap)

# Lager en ny mengde med elementene som finnes i begge mengdene.
# Returnerer lengden av denne mengden.
# https://www.w3schools.com/python/ref_set_intersection.asp


def test_count_overlap_sample():
    print('Tester count_overlap... ', end='')
    assert 2 == count_overlap('sample1.txt', 'sample2.txt')

    # Tester effektivitet (testen tar laaang tid ved feil løsning):
    assert 100001 == count_overlap('id1.txt', 'id2.txt')
    print('OK')

if __name__ == "__main__":
    test_count_overlap_sample()