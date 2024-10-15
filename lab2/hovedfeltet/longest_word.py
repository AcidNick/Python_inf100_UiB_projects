ord1 = input('Skriv et ord: \n')
ord2 = input('Skriv et annet ord: \n')
ord3 = input('Skriv et siste ord: \n')
print('')

longest = max(len(ord1), len(ord2), len(ord3))

if longest == len(ord1):
  print(ord1)
elif longest == len(ord2):
  print(ord2)
else:
  print(ord3)