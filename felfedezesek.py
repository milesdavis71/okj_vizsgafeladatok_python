import pandas as pd

header_names = ['ev', 'elem', 'vegyjel', 'rendszam', 'felfedezo']
df = pd.read_csv('src/felfedezesek.csv', sep=';', encoding='windows-1250', header=0, names=header_names)
print(f'Elemek szama: {len(df)}')
felfedezesek_okorban = df[df['ev'].str.contains('kor')]
print(f'Felfedezeek szama az okorban: {len(felfedezesek_okorban)}')
input_vegyjel = input('Adj egy vegyjelet')
while not input_vegyjel.isascii() and not len(input_vegyjel)<2:
    input_vegyjel = input('Nem jo, adj egy masik karaktert')

df_lower = df['vegyjel'].str.lower()
beirt_elem = df[df_lower.str.contains(input_vegyjel.lower())]