from pathlib import Path

def get_word_count(path:str) -> dict:
    count_dict = {}
    word_list = Path(path).read_text(encoding='utf-8')
    word_list = cleaned_text(word_list.lower()).split(' ')
    for word in word_list:
        count_dict[word] = word_list.count(word)
    return count_dict

def cleaned_text(text:str) -> str:
    legal_chars = 'abcdefghijklmnopqrstuvwxyzæøå \n'
    for char in text:
        if char not in legal_chars:
            text = text.replace(char, '')
    return text

def pop_most_common_word(word_count: dict) -> str:
    max_word = list(word_count.keys())[0]
    for word in word_count.keys():
        if word_count[word] > word_count[max_word]:
            max_word = word
        if word_count[word] == word_count[max_word]:
            if word < max_word:
                max_word = word
    word_count.pop(max_word)
    return max_word

def n_common_words(word_count: dict, n:int) -> list:
    common_words = []
    for i in range(n):
        common_words.append(pop_most_common_word(word_count))
    return common_words

def common_words(path:str, n:int) -> list:
    get_word_count(path)
    return n_common_words(get_word_count(path), n)

def test_get_word_count():
    print('Tester get_word_count... ', end='')
    expected = {
        'det': 1,
        'var': 3,
        'en': 2,
        'katt': 2,
        'som': 1,
        'het': 1,
        'pusur': 3,
        'snill': 1
    }
    actual = get_word_count('pusur.txt')
    assert(actual == expected)
    print('OK')

def test_pop_most_common_word():
    print('Tester pop_most_common_word... ', end='')
    my_word_count = {
        'som': 1,
        'pusur': 3,
        'var': 3,
        'katt': 2,
        'het': 1,
        'snill': 1,
        'en': 2,
        'det': 1
    }

    # Test 1
    expected = 'pusur'
    actual = pop_most_common_word(my_word_count)
    assert actual == expected, f'returnerte {actual}, forventet {expected}'
    assert 'pusur' not in my_word_count, "'pusur' fortsatt her etter test 1"

    # Test 2
    expected = 'var'
    actual = pop_most_common_word(my_word_count)
    assert actual == expected, f'returnerte {actual}, forventet {expected}'
    assert 'var' not in my_word_count, "'var' fortsatt her etter test 2"

    # Test 3
    expected = 'en'
    actual = pop_most_common_word(my_word_count)
    assert actual == expected, f'returnerte {actual}, forventet {expected}'
    assert 'en' not in my_word_count, "'en' fortsatt her etter test 3"

    print('OK')

def test_n_common_words():
    print('Tester n_common_words... ', end='')
    my_word_count = {
        'som': 1,
        'pusur': 3,
        'var': 3,
        'katt': 2,
        'het': 1,
        'snill': 1,
        'en': 2,
        'det': 1
    }

    # Test 1
    expected = ['pusur', 'var']
    # Vi bruker en kopi (lages med dict()) for å unngå mutasjon
    actual = n_common_words(dict(my_word_count), 2)
    assert actual == expected

    # Test 2
    expected = ['pusur', 'var', 'en', 'katt', 'det', 'het', 'snill', 'som']
    actual = n_common_words(dict(my_word_count), 8)
    assert actual == expected

    print('OK')

def test_common_words():
    print('Tester common_words... ', end='')
    # Test 1
    expected = ['pusur', 'var']
    actual = common_words('pusur.txt', 2)
    assert actual == expected

    # Test 2
    expected = ['pusur', 'var', 'en', 'katt', 'det', 'het', 'snill', 'som']
    actual = common_words('pusur.txt', 8)
    assert actual == expected

    print('OK')


if __name__ == "__main__":
    test_get_word_count()
    test_pop_most_common_word()
    test_n_common_words()
    test_common_words()