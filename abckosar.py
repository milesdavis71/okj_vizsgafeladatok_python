import pandas as pd

header_names = ['haz', 'ideg', 'hazpont', 'idegpont', 'helysz', 'datum']
df = pd.read_csv('src/eredmenyek.csv', encoding='windows-1250', sep=';', header=0, names=header_names)

real_hazai = df[df['haz'].str.contains('Real Madrid')]
real_idegen = df[df['ideg'].str.contains('Real Madrid')]
print('3. feladat: ', 'Real Madrid: Hazai: ' + str(len(real_hazai)) + ' Idegen: ' + str(len(real_idegen)))
egyenlo = df['hazpont'] == df['idegpont']
print("4. feladat:  Volt döntetlen?", "Volt." if egyenlo.any() else "Nem volt")

barcelona_teljes_nev = df[df['haz'].str.contains('Barcelona')]
print('5. feladat: ', (barcelona_teljes_nev['haz']).head(1).to_string(index=False))
jateknap = df[df['datum'].str.contains('2004-11-21')]
print('6. feladat:')

print((jateknap['haz'] + " - " + jateknap['ideg'] + ' ' + jateknap['idegpont'].map(str) + ' : ' + jateknap[
    'hazpont'].map(str)).to_string(index=False))
print(df['haz'].value_counts().loc[lambda x: x > 20])


