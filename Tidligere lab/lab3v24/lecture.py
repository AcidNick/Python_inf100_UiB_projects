num_of_students = 0
just_arrived = 1

while just_arrived != 0:
  just_arrived = int(input('Hvor mange kom inn døren? '))
  num_of_students += just_arrived
  print(f'Det har kommet {num_of_students} studenter på forelesning.')