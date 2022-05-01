import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

"""df = pd.read_csv('homeprices.csv')
median = int(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(median)

reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df.price)
print(df)
print(reg.predict([[2000,4,12]]))"""
"""df = pd.read_csv('hiring.csv')
median = df['test_score(out of 10)'].median()
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(median)
df.experience = [0,0,5,2,7,3,10,11]
reg = linear_model.LinearRegression()
reg.fit(df[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], df['salary($)'])
print(df)
print(reg.predict([[2,9,6]]))"""
