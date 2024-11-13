import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data={'Piloto':['Verstappen', 'Norris', 'Leclerc', 'Piastri', 'Sainz', 'Russell', 'Hamilton'],
      'Vitórias':[8, 3, 3, 2, 2, 1, 1],
      'Pódios':[13, 12, 11, 7, 7, 3, 4]}
df=pd.DataFrame(data)
df.index = df.index + 1
print(df)

media_Pódios=np.mean(df["Pódios"])
mediana_Pódios=np.median(df["Pódios"])
dsp_Pódios=np.std(df["Pódios"])

print("\nMédia de pódios:", f"{media_Pódios:.2f}")
print("Mediana de pódios:", mediana_Pódios)
print("Desvio padrão de pódios:", f"{dsp_Pódios:.2f}")


plt.pie(df['Vitórias'], labels=df['Piloto'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.axis('equal')
plt.title('Vitórias por Piloto')
