import pandas as pd

data={
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'Idade': [23, 35, 45, 29],
    'Salário': [5000, 7000, 6000, 6500]
}

df=pd.DataFrame(data)
df.index=df.index+1
df_sorted = df.sort_values(by='Idade')
print("\nDataframe ordenado pela idade: ")
print(df_sorted)

df_sorted_desc = df.sort_values(by='Salário', ascending=False)
print("\nDataframe ordenado em ordem decrescente: ")
print(df_sorted_desc)

