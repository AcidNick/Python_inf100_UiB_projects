initial_population = int(input('Befolkning: '))
annual_growth = float(input('Årlig vekstrate (i prosent): '))
years = int(input('Antall år: '))

population = initial_population

for i in range(years):
  population += int(population*annual_growth/100)
  print(f'Befolkningen etter {i+1} år er {population}')

total_growth = round(100*(population-initial_population)/initial_population, 2)
print(f'Total vekst etter {years} år er (i prosent) {total_growth}')