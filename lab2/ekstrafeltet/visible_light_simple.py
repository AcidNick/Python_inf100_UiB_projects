enhet = input('Angi enhet (nm eller THz):\n')
nm = 0
THz = 0

if enhet == 'nm':
  print('Angi verdi i nm')
  nm = int(input())
  if nm > 380 or nm > 750:
    print(f'{nm} nm er utenfor det synlige spekteret.')
    exit() #Stopper programmet fra å fortsette.
elif enhet == 'THz':
  print('Angi verdi i THz')
  THz = int(input())
  if THz < 400 or nm > 790:
    print(f'{THz} THz er utenfor det synlige spekteret.')
    exit()
  nm = (3e8 / THz*1e-12)*1e9 #Konverter THz til nm
  nm = round(nm)
else:
  print(f'Enheten må være i nm eller THz, det kan ikke være {enhet}.')
  exit()

print('')

if 380 <= nm < 450:
  print('Violet')
elif 450 <= nm < 485:
  print('Blue')
elif 485 <= nm < 500:
  print('Cyan')
elif 500 <= nm < 565:
  print('Green')
elif 565 <= nm < 590:
  print('Yellow')
elif 590 <= nm < 625:
  print('Orange')
elif 625 <= nm <= 750:
  print('Red')