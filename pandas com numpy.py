import pandas as pd
import numpy as np

d={'A':[1,2,np.nan], 'B':[5,np.nan, np.nan], 'C':[1,2,3]}
df=pd.DataFrame(d)
print(df)
print(df.dropna(axis=1))
df=pd.DataFrame(d)
df['A'].fillna(value=999, inplace=True)
df['B'].fillna(value=999, inplace=True)
df['A'].fillna(value=df['A'].mean(), inplace=True)
df['B'].fillna(value=df['B'].mean(), inplace=True)
print(df)
