import pandas as pd

df = pd.read_csv('src/fuvar.csv', decimal=',', sep=';')
df.columns = ['taxiid', 'start', 'idotart', 'tavolsag', 'viteldij', 'borravalo', 'fizmod']
print('3. feladat: ' + str(len(df)) + ' fuvar')

taxi6185 = df[df['taxiid'] == 6185]
taxi6185bevetel = taxi6185['viteldij'].astype(float).sum()
print('4. feladat: ' + str(len(taxi6185)) + ' fuvar alatt ' + str(taxi6185bevetel) + '$')

print('5. feladat: ')
print(df['fizmod'].value_counts())

print(str(((df['tavolsag'] * 1.6).sum()).round(2)) + ' km')

legmagasabb = df.loc[df['idotart'].idxmax()]
print('7. feladat: leghosszabb fuver:\n' + 'Fuvar hossza: ' + str(legmagasabb['idotart'])+'\nTaxi azonosito:'+str(legmagasabb['taxiid']))
print('Megtett tavolsag: '+str(legmagasabb['tavolsag'])+'\nViteldij: ' + str(legmagasabb['viteldij'])+'$')
hibak = df[(df['idotart'] > 0) & (df['viteldij'] > 0) & (df['tavolsag'] == 0)].sort_values('start')
hibak.to_csv('huhu.txt')