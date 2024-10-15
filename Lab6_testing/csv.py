from pathlib import Path

###########################################
### LESE INPUT OG OPPRETTE DATASTRUKTUR ###
###########################################

# Les inn innholdet i filen 'people.csv' som en streng
content_string = Path('people.csv').read_text(encoding='utf-8')

# .strip fjerner whitespace på begynnelsen og slutten av strengen
content_string = content_string.strip()

# .split('\n') klipper opp strengen ved linjeskift, og gir oss en
# liste med bitene som er igjen; altså radene i tabellen
content_lines = content_string.split('\n')

# Vi oppretter en 2D-liste (en liste av lister) som skal inneholde
# tabellen vår
table = []
for line in content_lines:
    # .split(',') klipper opp strengen ved komma, og gir oss en
    # liste med bitene som er igjen
    row = line.split(',')
    table.append(row)

# Vi kan nå aksessere enkeltverdier i tabellen vår ved å bruke
# indeksering på samme måte som vi gjør med andre 2D-lister
print(table[0][1])  # Alder
print(table[1][0])  # Ola
print(table[3][2])  # 1.73

# Ofte gir det mening å ha overskriftene og selve dataene i separate
# variabler.
headers = table[0]  # første rad
data = table[1:]  # alle rader unntatt den første

##############################################
### UTFØR SELVE DATABEHANDLINGEN VI ØNSKER ###
##############################################

# Et år har passert! Øk alle aldre med 1 i datasettet.
for row in data:
    row[1] = 1 + int(row[1])  # PS: dette endrer typen til int

############################
### PRESENTER RESULTATET ###
############################

result_headers = headers
result_headers_string = ','.join(result_headers)
result_lines = [result_headers_string]
for row in data:
    string_row = [str(x) for x in row]
    line_string = ','.join(string_row)
    result_lines.append(line_string)
result_string = '\n'.join(result_lines) + '\n'

Path('people_one_year_later.csv').write_text(result_string, encoding='utf-8')
