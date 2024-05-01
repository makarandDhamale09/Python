import pandas as pd

df = pd.read_csv("pokemon_data.csv")

# print(df.head()) print top 5 rows
# print(df.tail()) print last 5 rows

# Read Headers
# print(df.columns)

# Read each column
# print(df['Name'][0:5])
# print(df[['Name', "Type 1", "HP"]])

# Read Each Row
# print(df.iloc[1:4])
# for index, row in df.iterrows():
#     print(index, row)

df_fire = df.loc[df['Type 1'] == "Fire"]
print(df_fire)
