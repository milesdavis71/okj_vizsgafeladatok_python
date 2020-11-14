import pandas as pd
header_names = ['nev', 'orsz', 'tech', 'komp', 'lev']

df = pd.read_csv('src/rovidprogram.csv', sep=';', header=0, names=header_names)
van_e_magyar = df['orsz'] == 'HUN'
print('3. feladat: Volt magyar?', 'Volt.' if van_e_magyar.any() else 'Nem volt')
