import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data={'Estudante': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
      'matematica': [85, 78, 92, 88, 76], 'historia': [74, 85, 89, 91, 77],
      'ciencias': [90, 88, 93, 85, 80], 'ingles': [80, 79, 85, 83, 88]}
df=pd.DataFrame(data)
print(df)

media_notas=df.mean(numeric_only=True)
mediana_notas=df.median(numeric_only=True)
variancia_notas=df.var(numeric_only=True)

print("\nMédia de Notas por disciplina:")
print(media_notas)
print("\nMediana de Notas:")
print(mediana_notas)
print("\nVariância de Notas:")
print(variancia_notas)

df['Media Geral']=df[['matematica', 'historia', 'ciencias', 'ingles']].mean(axis=1)
print("\nDataframe Atualizado com Média Geral:")
print(df)

disciplinas=['matematica', 'historia', 'ciencias', 'ingles']
plt.bar(disciplinas, media_notas, color=['blue', 'green', 'orange', 'purple'])
plt.xlabel("Disciplinas")
plt.ylabel("Média das Notas")
plt.title("Média de Notas por Disciplina")
plt.grid(axis='y', linestyle='--')
plt.show()
