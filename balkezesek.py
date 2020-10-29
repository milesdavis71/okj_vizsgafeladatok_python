import pandas as pd


df = pd.read_csv("balkezesek.csv", sep=';', header=0)
print(len(df))
oktoberbenPalyaraLeptek = df[df['utolso'].str.contains("1999-10")]
print((oktoberbenPalyaraLeptek['nev'].map(str) +", "+ ((oktoberbenPalyaraLeptek['magassag'].astype(float)*2.54).round(1)).map(str)+" cm").to_string(index=False))

