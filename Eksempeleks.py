#EksempelEksamen oppgave A
"""
# Åpner CSV-filen
with open("Eksempeleksamen22.csv", encoding='utf-8') as file:
    lines = file.readlines()

# Fjerner overskriften og eventuelle tomme linjer
lines = [line.strip() for line in lines if line.strip()]

# Oppretter en ordbok for å lagre data
startlokasjoner = {}  # Struktur: {startlokasjon: antall turer}

# Behandler hver linje i filen
for line in lines[1:]:  # Starter fra andre linje for å hoppe over overskriften
    elements = line.split(',')
    startlokasjon = elements[4]

    # Oppdaterer ordboken med data
    if startlokasjon not in startlokasjoner:
        startlokasjoner[startlokasjon] = 0
    startlokasjoner[startlokasjon] += 1

# Sorterer startlokasjonene basert på antall turer
sorterte_lokasjoner = sorted(startlokasjoner.items(), key=lambda x: x[1], reverse=True)

# Velger de tre mest og minst brukte startlokasjonene
mest_brukte = sorterte_lokasjoner[:3]
minst_brukte = sorterte_lokasjoner[-3:]

# Skriver ut resultatene
print("De tre mest brukte startlokasjonene:")
for lokasjon, antall in mest_brukte:
    print(f"{lokasjon}: {antall} turer")

print("\nDe tre minst brukte startlokasjonene:")
for lokasjon, antall in minst_brukte:
    print(f"{lokasjon}: {antall} turer")
"""
#EksempelEksamen oppgave B
"""
import matplotlib.pyplot as plt
from datetime import datetime

# Åpner CSV-filen
with open("Eksempeleksamen22.csv", encoding='utf-8') as file:
    lines = file.readlines()

# Fjerner overskrift og eventuelle tomme linjer
lines = [line.strip() for line in lines if line.strip()]

# Oppretter en ordbok for å lagre data, initialiserer med null for hver ukedag
ukedager = {'mandag': 0, 'tirsdag': 0, 'onsdag': 0, 'torsdag': 0, 'fredag': 0, 'lørdag': 0, 'søndag': 0}

# Behandler hver linje i filen
for line in lines[1:]:  # Starter fra andre linje for å hoppe over overskriften
    elements = line.split(',')
    dato = elements[0]
    try:               #brukte KI for å gjøre om dataen til datoer og deretter sortere de fra mandag - søndag
        # Konverterer datostring til et datetime-objekt
        dato_objekt = datetime.fromisoformat(dato)
        # Henter ukedagen (0 = mandag, 6 = søndag)
        ukedag_index = dato_objekt.weekday()
        # Mapper indeksen til en ukedag på norsk
        ukedag_navn = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag', 'søndag'][ukedag_index]
    except ValueError:
        # Hopper over linjer med feil datoformat
        continue

    # Oppdaterer ordboken med data
    ukedager[ukedag_navn] += 1

# Forbereder data for plotting
ukedager_navn = list(ukedager.keys())
antall_turer = list(ukedager.values())

# Plotter diagrammet
plt.bar(ukedager_navn, antall_turer)
plt.xlabel('Ukedag')
plt.ylabel('Antall turer')
plt.title('Totalt antall turer per ukedag')
plt.show()
"""