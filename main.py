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
df = pd.read_csv('eredmenyek.csv', delimiter='')
# User list comprehension to create a list of lists from Dataframe rows
list_of_rows = [list(row) for row in df.values]
# Print list of lists i.e. rows
print(list_of_rows)