from pathlib import Path

def get_stringsum(s: str) -> int:
    items = s.split(' ')
    summert: int = 0
    for item in items:
        try:
            number: int = int(item)
        except ValueError:
            continue
        else:
            summert += number
    return summert

def get_line_with_highest_stringsum(s: str) -> tuple:
    line = s.strip().splitlines()
    highest = get_stringsum(line[0])
    i = 1
    t = get_stringsum(line[0])
    r = line[0]
    for n in range(len(line)):
        current = get_stringsum(line[n])
        if current > highest:
            highest = current
            i = n+1
            t = current
            r = line[n]
    return i, t, r

def main():
    path = input('Filnavn: ')
    i, t, r = get_line_with_highest_stringsum(Path(path).read_text(encoding='utf-8'))
    print(f'Høyeste strengsum er {t}, funnet først på linje {i}: "{r}"')

if __name__ == '__main__':
    main()