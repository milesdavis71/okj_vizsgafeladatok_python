import pandas as pd

header_names = ['nev', 'orsz', 'tech', 'komp', 'lev']
df_rovid = pd.read_csv('src/rovidprogram.csv', sep=';', header=0, names=header_names)
df_donto = pd.read_csv('src/donto.csv', sep=';', header=0, names=header_names)
df_donto['foo'] = 'bar'

van_e_magyar = df_rovid['orsz'] == 'HUN'
print('3. feladat: Volt magyar?', 'Volt.' if van_e_magyar.any() else 'Nem volt')
nev = input('Adj meg egy nevet')
nemdontos_nev = df_rovid[df_rovid['nev'] == nev]
dontos_nev = df_donto[df_donto['nev'] == nev]
if nemdontos_nev.empty & dontos_nev.empty:
    print('Ilyen nevu indulo nem volt.')
else:
    def osszpontszam(neve):
        input_nev_dontos = df_donto[df_donto['nev'] == neve]
        input_nev_nemdontos = df_rovid[df_rovid['nev'] == neve]
        rovidprogram_pontok = input_nev_nemdontos['tech'].iloc[0] + input_nev_nemdontos['komp'].iloc[0] - \
                              input_nev_nemdontos['lev'].iloc[0]
        if input_nev_dontos.empty:
            return rovidprogram_pontok
        else:
            donto_pontok = input_nev_dontos['tech'].iloc[0] + input_nev_dontos['komp'].iloc[0] - \
                           input_nev_dontos['lev'].iloc[0]
            return rovidprogram_pontok + donto_pontok


    print(osszpontszam(nev))

orszagonkent_tovabjutott_versenyzok = df_donto[df_donto['orsz'].value_counts().loc[lambda x: x > 1]]
print(orszagonkent_tovabjutott_versenyzok.add_suffix(', versenyzok szama: '))
df_donto.insert(0, 'sorrend', df_donto.index+1)
df_donto.insert(5, 'egybe', df_donto['tech']+df_donto['komp']-df_donto['lev'].round(1))
nev = df_donto[['sorrend', 'nev', 'orsz', 'egybe']]
nev.to_csv('vegeredmeny.csv', index=False)
