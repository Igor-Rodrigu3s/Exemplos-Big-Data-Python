import pandas as pd
dados={'Estados':['Rio de Janeiro','São Paulo','Minas Gerais','Espírito Santo'], 'Ano':['2021','2021','2021','2021'], 'População':[3.8,4.8,3.5,3.2]}

df=pd.DataFrame(dados)
print(df)

df.head()
df.describe()
df["Estados"]
df["População"].sum() #faz a soma da lista população
df["População"].max() #pega o maior valor na lista
df["População"].min() #pega o menor valor
df["População"].mean() #faz a média
df["População"].std() #retorna o desvio padrão
df["População"].prod() #pega o produto dos valores
df["População"].median() #faz a mediana
