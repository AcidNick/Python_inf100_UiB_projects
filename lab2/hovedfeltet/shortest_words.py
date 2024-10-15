ord1 = input('Skriv et ord: \n')
ord2 = input('Skriv et annet ord: \n')
ord3 = input('Skriv et siste ord: \n')
print('')

shortest = min(len(ord1), len(ord2), len(ord3))

if shortest == len(ord1):
  print(ord1)
if shortest == len(ord2):
  print(ord2)
if shortest == len(ord3):
  print(ord3)