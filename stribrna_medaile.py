# Seznam vysledky, který obsahuje jména a výsledky prvních čtyř běžců maratonu. 
# Seznam je vícerozměrný. Na nulté pozici každého z vnořených seznamů je jméno běžce 
# a na první pozici je seznam s časem běžce, který obsahuje počet hodin, minut a sekund, 
# které běžec potřeboval na překonání trati.

# Stříbrná medaile

# Stříbrná medaile je sice úžasný úspěch, ale kdo by nechtěl vyhrát? 
# Podívejme se, kolik chybělo stříbrnému běžci k vítězství.
# Nejprve si vytvoř dvě proměnné, do kterých ulož čas vítěze a čas závodníka se stříbrnou medailí. 
# Oba časy převeď na minuty a ulož jako číslo.
# Vypočti rozdíl obou proměnných. Tím zjistíš, kolik minut chybělo stříbrnému závodníku k vítězství.

vysledky = [
    ["Brunner Radek", [3, 0, 9]], 
    ["Urban Jaroslav", [3, 11, 44]], 
    ["Andrle Jakub", [3, 12, 21]], 
    ["Fiala Stanislav", [3, 13, 31]]
]


def cas_v_minutach(cas_vysledky):
    minuty = cas_vysledky[0] * 60 + cas_vysledky[1] + cas_vysledky[2] / 60
    return minuty


def rozdil_casu(cas_x, cas_y):
    rozdil = cas_v_minutach(cas_y) - cas_v_minutach(cas_x)
    return rozdil


cas_vitez = vysledky[0][1]
cas_stribry = vysledky[1][1]

print(f'Stříbrnému chybělo k vítězství {rozdil_casu(cas_vitez, cas_stribry)} minut.')

# Závody podruhé

# Zadání je podobné jako u předchozího příkladu, 
# ale nyní zkusíme výpočet provést pro všechny závodníky.

# Nejprve (pomocí cyklu a metody append()) vytvoř dvourozměrný seznam, 
# kde na nulté pozici vnořeného seznamu je číslo běžce 
# a na první pozici je čas běžce v minutách jako desetinné číslo.
# Ve druhém kroku (opět pomocí cyklu a metody append()) vytvoř další dvourozměrný seznam, 
# kde na nulté pozici vnořeného seznamu je číslo běžce a na první pozici 
# je rozdíl času běžce oproti času vítěze v minutách. Jinak řečeno, bude tam číslo, 
# které udává, o kolik by běžec musel být rychlejší, aby závod vyhrál.

vysledky_v_minutach = []
poradi_zavodnik_1 = 0

for zavodnik in vysledky:
    poradi_zavodnik_1 += 1
    cas_zavodnik = zavodnik[1]
    vysledky_v_minutach.append([poradi_zavodnik_1, cas_v_minutach(cas_zavodnik)])

minuty_do_vitezstvi = []
poradi_zavodnik_2 = 0

for zavodnik in vysledky:
    poradi_zavodnik_2 += 1
    cas_zavodnik = zavodnik[1]
    minuty_do_vitezstvi.append([poradi_zavodnik_2, rozdil_casu(cas_vitez, cas_zavodnik)])