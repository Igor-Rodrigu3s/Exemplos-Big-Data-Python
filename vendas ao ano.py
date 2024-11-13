import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados={'Mes':['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], 'Vendas': [305, 356, 389, 412, 450, 478, 520, 550, 600, 610, 700, 750]}
df=pd.DataFrame(dados)
print(df)

media_vendas=np.mean(df["Vendas"])
mediana_vendas=np.median(df["Vendas"])
dsp_vendas=np.std(df["Vendas"])

print("\nMédia de vendas:", f"{media_vendas:.2f}")
print("Mediana de vendas:", mediana_vendas)
print("Desvio padrão de vendas:", f"{dsp_vendas:.2f}")

df['Diferença da Média']=df["Vendas"] - media_vendas
print("\nDataframe Atualizado com Diferença de Média:")
print(df)

plt.plot(df['Mes'], df['Vendas'], marker="o", linestyle="-", label="Vendas")
plt.axhline(y=media_vendas, color="r", linestyle="--", label=f"Média({media_vendas:.2f})")
plt.legend()
plt.xlabel("Mes")
plt.ylabel("Vendas")
plt.title("Vendas Mensais")
plt.show()
