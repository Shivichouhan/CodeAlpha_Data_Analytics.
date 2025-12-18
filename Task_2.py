import pandas as pd
# Sample code for Task 2
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print("Data Loaded Successfully!")
print(df.head())
