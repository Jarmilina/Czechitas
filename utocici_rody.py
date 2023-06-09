# Zadání příkladu
# V rámci této lekce si vyzkoušíme vyřešit příklad, ve kterém využijeme koncepty, které jsme si ukazovali v předchozích lekcích.

# Zadání příkazu je následující:

# Ze souboru battles.tsv si načti informace o bitvách, které se odehrály ve knižní sérii Písně ohně a ledu, 
# jejímž autorem je spisovatel George R. R. Martin a podle níž byl natočen slavný seriál Hra o trůny. 
# Naším úkolem je ze zadaných dat zjistit následující:

# Statistiku, kolikrát byl který rod v pozici útočníků. Výsledná data ulož do CSV souboru attackers.csv.
# Pokud je zadaná síla obou armád (sloupce attacker_size a defender_size, indexy sloupců jsou 17 a 18), 
# vytvoř seznam velitelů, kteří v boji porazili silnější armádu (vítěze poznáš podle sloupce attacker_outcome, 
# který obsahuje hodnoty win a loss, platí vždy z pohledu útočníka). Kolik takových bitev je?


import json
ATTACKER_COL_START = 5
ATTACKER_COL_END = 8

with open('battles.tsv', mode='r', encoding='utf8') as file:
    next(file)
    text = file.readlines()

utocici_rody_dict = {}
utocici_rody = []
for line in text:
    line = line.strip('\n')
    line = line.split('\t')
    line = line[ATTACKER_COL_START:ATTACKER_COL_END + 1]
    for x in line:
        if x:    # if x != '':
            if x not in utocici_rody_dict:
                utocici_rody_dict[x] = 1
            else:
                utocici_rody_dict[x] += 1
print(utocici_rody_dict)

with open('attackers.csv', mode='w', encoding='utf-8') as output_file:
    for attacker, count in utocici_rody_dict.items():
        output_file.write(f'{attacker},{count}\n')