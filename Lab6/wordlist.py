from pathlib import Path

def filter_wordlist(path, search_string):
    word_list = Path(path).read_text(encoding='utf-8').splitlines()
    matching_words = [word for word in word_list if search_string in word]
    return matching_words


def test_filter_wordlist():
    print('Tester filter_wordlist... ', end='')

    # Test 1
    expected = ['database', 'baser']
    actual = filter_wordlist('sample.txt', 'base')
    assert expected == actual

    # Test 2
    expected = [
        'småstad', 'småstaden', 'småstas', 'småstasen', 'småstat', 'småstaten',
        'småstatene', 'småstater',
    ]
    actual = filter_wordlist('nsf2022.txt', 'småsta')
    assert expected == actual

    # Test 3
    expected = [
        'stjerneskudd', 'stjerneskudda', 'stjerneskuddene', 'stjerneskuddet',
    ]
    actual = filter_wordlist('nsf2022.txt', 'stjerneskudd')
    assert expected == actual

    print('OK')

if __name__ == '__main__':
    test_filter_wordlist()