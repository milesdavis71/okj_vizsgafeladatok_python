import pandas as pd

df = pd.read_csv("src/balkezesek.csv", sep=';', header=0)


print(len(df))
oktoberbenPalyaraLeptek = df[df['utolso'].str.contains("1999-10")]
print((oktoberbenPalyaraLeptek['nev'].map(str) + ", " + (
    (oktoberbenPalyaraLeptek['magassag'].astype(float) * 2.54).round(1)).map(str) + " cm").to_string(index=False))

input_ev = input('Adj meg egy számot!')
print('Köszi!')
while not 1990 <= int(input_ev) <= 1999:
    print('szar')
    input('Adj másik számot...')

input_ev_jatszott = df[(df['elsoev'].astype(int) >= int(input_ev)) & (df['utolsoev'].astype(int) <= int(input_ev))].mean()
print(str(round(input_ev_jatszott['suly'], 2))+' font')
