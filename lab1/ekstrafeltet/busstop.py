husnummer = int(input('Husnummer:\n'))
husnummer += husnummer % 7
husnummer = husnummer // 7
nærmeste = husnummer * 7
print(f'Nærmeste busstopp er ved nummer {nærmeste}')
