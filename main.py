# class Eredmenyek:
#
#     def __init__(
#             self,
#         hazai,
#         idegen,
#         hazai_pont,
#         idegen_pont,
#         helyszin,
#         idopont
#     ):
#         self.hazai = hazai,
#         self.idegen = idegen,
#         self.hazai_pont = hazai_pont,
#         self.idegen_pont = idegen_pont,
#         self.helyszin = helyszin,
#         self.idopont = idopont


import pandas as pd
col_list=["név", "","" ]
data = pd.read_csv("balkezesek.csv", sep=",", encoding="ISO-8859-1", usecols=col)
# Preview the first 5 lines of the loaded data
print(data["név"])