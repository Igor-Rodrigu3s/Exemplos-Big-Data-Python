import pandas as pd
import matplotlib.pyplot as plt

dados={'Mes':['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'], 'Vendas': [305, 356, 389, 412, 450, 478, 520, 550, 600, 610, 700, 750]}
df=pd.DataFrame(dados)
print(df)

plt.figure(figsize=(10,6))
plt.title("Vendas mensais em 2023")
plt.plot(df['Mes'], df['Vendas'], marker="o", linestyle="-")
plt.xlabel("Mes")
plt.ylabel("Vendas")
plt.show()
