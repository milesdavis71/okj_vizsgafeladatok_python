import pandas as pd

header_names = ['ev', 'elem', 'vegyjel', 'rendszam', 'felfedezo']
df = pd.read_csv('src/felfedezesek.csv', sep=';', encoding='windows-1250', header=0, names=header_names)
print(f'Elemek szama: {len(df)}')
felfedezesek_okorban = df[df['ev'].str.contains('kor')]
print(f'Felfedezeek szama az okorban: {len(felfedezesek_okorban)}')
input_vegyjel = input('Adj egy vegyjelet')

def bevittvegyjelvalidalas(vegyjel):
    hossz = True
    angolkarakterek = True
    if len(vegyjel) > 2:
        joe = False
        if vegyjel.contains65 & vegyjel