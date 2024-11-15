def key_value_getter(d: dict) -> None:
    print('Dictionary keys:')
    for key in d.keys():
        print(key)
    print('\nDictionary values:')
    for value in d.values():
        print(value)
    print('\nDictionary keys/values:')
    for key, value in d.items():
        print(f"{key} {value}")
    return None

def index_value_getter(a: list) -> None:
    print('List indices:')
    for i in range(len(a)):
        print(i)
    print('\nList values:')
    for value in a:
        print(value)
    print('\nList indices/value:')
    for i in range(len(a)):
        print(f"{i} {a[i]}")
    return None

if __name__ == '__main__':
    key_value_getter({
        "monday": 0,
        "tuesday": 0.7,
        "wednesday": 0,
        "thursday": 4.7,
        "friday": 10
    })
    index_value_getter([7.0, 8.0, 10.0, 9.0, 10.0])
