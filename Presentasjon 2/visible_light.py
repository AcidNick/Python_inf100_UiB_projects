enhet = input('Angi enhet (nm eller THz):\n')
enhet = enhet.lower()

if enhet not in ('nm', 'thz'):
  print(f'Enheten må være i nm eller THz, det kan ikke være {enhet}.')
  exit()

if enhet == 'nm':
  nm = int(input('Angi verdi i nm:\n'))
  if nm not in range(380, 751):
    print(f'{nm} nm er utenfor det synlige spekteret.')
    exit()
else:
  thz = int(input('Angi verdi i thz:\n'))
  if thz not in range(400, 791):
    print(f'{thz} THz er utenfor det synlige spekteret.')
    exit()
  else:
    nm = (3e8 / thz*1e-12)*1e9
    nm = round(nm)

print('')

farger = [[380, 450, 'Violet'],
          [450, 485, 'Blue'],
          [485, 500, 'Cyan'],
          [500, 565, 'Green'],
          [565, 590, 'Yellow'],
          [590, 625, 'Orange'],
          [625, 751, 'Red']]

for e in farger:
  if nm in range(e[0], e[1]):
    print(e[2])