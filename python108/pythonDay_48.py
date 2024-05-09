#All basics about pandas
import pandas as pd
data = {
    'Name':['Alice', 'Bob', 'Charlie'],
    'Age':[24,23,25],
    'city': ['New York', 'Los Angels', "US"]
}

df = pd.DataFrame(data)
print(df)

#accessing col
print(df['Name'])
print(df.age)

#access row
print(df.loc[0])
print(df.iloc[0])

#Adding New col 
df['Gender']=['female','male','male']