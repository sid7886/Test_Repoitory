a=3
b=4
print(a+b)
import pandas as pd

data = pd.read_csv('Electric_Vehicle_Population_Data.csv')
print(data.head())
data.isnull().sum()
data= data.dropan()
data.info()