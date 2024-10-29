import numpy as np
import pandas as pd

data={'Empresa':['NovaCar','NovaCar','CarNew','CarNew','TurboCar','TurboCar'], 'Vendedores':['Carla ','Pedro ','Maria ','Vanessa ','Lucas ','Fernanda '], 'vendas':[60000, 25000, 140000, 20000, 15000, 80000]}
df=pd.DataFrame(data)
print(df)
AgrEmpresa=df.groupby('Empresa')
print(AgrEmpresa.sum())
print(df.groupby(["Empresa"])["vendas"].sum().sort_values())
print(df.groupby(["Empresa"])["vendas"].mean().sort_values())
print(df.groupby(["Empresa"])["vendas"].max().sort_values())
print(df.groupby(["Empresa"])["vendas"].min().sort_values())
