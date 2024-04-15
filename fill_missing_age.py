import pandas as pd

titanic=pd.read_csv('titanic.csv')
mean_age=titanic['Age'].mean()
titanic['Age'].fillna(mean_age,inplace=True)
titanic.to_csv('titanic_filled.csv', index=False)
