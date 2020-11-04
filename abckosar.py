import pandas as pd

header_names = ['haz', 'ideg', 'hazpont', 'idegpont', 'helysz', 'datum']
df = pd.read_csv('eredmenyek.csv', encoding='windows-1250', sep=';', header=0, skiprows=1, names=header_names)
# \xed
# \xf5


real_hazai = df[df['haz'].str.contains('Real Madrid')]
real_idegen = df[df['ideg'].str.contains('Real Madrid')]

print('Real Madrid: Hazai: ' + str(len(real_hazai)) + ' Idegen: ' + str(len(real_idegen)))

barcelona_teljes_nev = df[df['haz'].str.contains('Barcelona')]
jateknap = df[df['datum'].str.contains('2004-11-21')]
print((jateknap['haz']+" - " + jateknap['ideg']+' ' + jateknap['idegpont'].map(str)+' : '+jateknap['hazpont'].map(str)).to_string(index=False))
