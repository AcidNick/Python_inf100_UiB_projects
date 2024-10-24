# Destruktiv funksjon:
def append_item(lst, item):
    lst.append(item)  # Endrer original liste

# Ikke-destruktiv funksjon:
def add_item(lst, item):
    return lst + [item]  # Lager en ny liste, endrer ikke den originale

# Eksempel:
a = [1, 2, 3]
b = add_item(a, 4)
print(a)  # Output: [1, 2, 3] (uendret)
print(b)  # Output: [1, 2, 3, 4] (ny liste)
