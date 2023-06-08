# Úkol 2
# V tomto úkolu budeš pracovat s datasetem netflix_titles.tsv. 
# Jedná se o textový soubor ve formátu TSV.
#                                                                                                                                                                                          Tvým úkolem bude soubor načíst, vytáhnout z něj některé údaje a uložit je ve formátu JSON.
# Z každého řádku nás budou zajímat tyto údaje: 
# PRIMARYTITLE (název),
# DIRECTOR (režisér/režiséři),
# CAST (herci),
# GENRES (seznam žánrů),
# STARTYEAR (rok vydani).
# Údaje o filmech převeď do seznamu, kde bude každý film reprezentován jako slovník obsahující 
# následující položky:
# title (název filmu),
# directors (seznam všech režisérů nebo prázdný seznam, pokud není režisér uveden),
# cast (seznam všech herců nebo prázdný seznam, pokud není žádný herec uveden),
# genres (seznam všech žánrů, do kterých byl film zařazen),
# decade (dekáda, ve které film vznikl).

# Protože formát TSV neumožňuje reprezentovat seznam, jsou herci a režiséři zadání jako 
# jeden řetězec a jednotlivé hodnoty jsou oddělené čárkami. 
# Ve formátu JSON použij pro větší přehlednost seznam, aby bylo například vidět, 
# kolik herců nebo režisérů v seznamu je.
# Může se stát, že film neobsahuje údaj o režisérech nebo hercích, ostatní jsou vždy uvedené.
# Dekáda je vždy první rok desetiletí, např. rok 1987 patří do dekády 1980 a rok 2017 do dekády 2010.
# Vytvořený seznam slovníků ulož do souboru movies.json.
# Pokud není uveden žádný režisér nebo herec, daná položka musí být prázdný seznam [], 
# nikoli seznam s řetězcem o nulové délce [“”].

import pandas as pd
import json

df = pd.read_csv('netflix_titles.tsv', sep='\t', usecols=['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR'])

df = df[['PRIMARYTITLE', 'DIRECTOR', 'CAST', 'GENRES', 'STARTYEAR']]

df.columns = ['title', 'directors', 'cast', 'genres', 'decade']

df['decade'] = df['decade']//10*10

df['genres'] = df['genres'].str.split(',')

print(((df['directors'].isna()) & (df['cast'].isna())).sum())

df_1 = df.dropna()
df_1['directors'] = df_1['directors'].str.split(', ')
df_1['cast'] = df_1['cast'].str.split(', ')

df_2 = df[df['directors'].isnull()]
df_2 = df_2.fillna('')
df_2['directors'] = df_2['directors'].str.split()
df_2['cast'] = df_2['cast'].str.split(', ')

df_3 = df[df['cast'].isnull()]
df_3 = df_3.fillna('')
df_3['cast'] = df_3['cast'].str.split()
df_3['directors'] = df_3['directors'].str.split(', ')

df_clean = pd.concat([df_1, df_2, df_3])
df_clean_sorted = df_clean.sort_index(axis=0, level=0)

df_output = df_clean_sorted.to_dict('records')

with open('movies.json', mode='w', encoding='utf') as output_file:
    output_file = json.dump(df_output, output_file, ensure_ascii=False, indent=4)