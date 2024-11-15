def is_leap_year(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
  year = int(input('Skriv inn eit årstal:\n'))
  if is_leap_year(year):
    print(f'{year} er eit skotår')
  else:
    print(f'{year} er ikkje eit skotår')

if __name__ == "__main__":
  main()