from pathlib import Path

def possible_words_from_file(path: str, letters:str) -> list:
    words = Path(path).read_text(encoding='utf-8').splitlines()
    # Samler frekvensen av hver bokstav i et dictionary
    letter_count = {}
    for char in letters:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    def legal_word(word):
        count = letter_count.copy()
        for char in word:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True

    return [word for word in words if legal_word(word)]

def test_possible_words_from_file():
    print('Tester possible_words_from_file... ', end='')
    assert(['du', 'dun', 'hu', 'hud', 'hun', 'hund', 'nu', 'uh']
            == possible_words_from_file('nsf2022.txt', 'hund'))

    # Ekstra test for varianten hvor det er wildcard i bokstavene
    # assert(['a', 'cd', 'cv', 'e', 'i', 'pc', 'wc', 'æ', 'å']
    #         == possible_words_from_file('nsf2022.txt', 'c*'))
    print('OK')

if __name__ == '__main__':
    test_possible_words_from_file()
