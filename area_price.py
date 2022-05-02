"""import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
area_and_price = {'area':[65, 13, 217, 70, 128, 151, 65, 111, 170,
                          173, 75, 70, 50, 100, 65, 105, 30, 75, 225], 'price':[72000, 15500, 210000, 62000, 260000, 245000, 109000, 95000,
                                                                                250000, 650000, 78000, 114000, 51000, 177000, 90000, 135000, 60000, 36500, 279000]}
# A linear regression model

df = pd.DataFrame(area_and_price)
df = df[df.loc[:,'price'] < 650000]
plt.scatter(df.area,df.price, color='red', marker='+' )
plt.ylabel('price')
plt.xlabel('area')
#print(df.describe())

reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)
m = reg.coef_
b = reg.intercept_
x = df.area
plt.plot(df.area, reg.predict(df[['area']]), color='blue')
area_df = pd.read_csv('area.csv')
array = np.array(area_df['area'])
list_of_results = []
for number in array:
    list_of_results.append(reg.predict([[number]]))
list_of_results = pd.DataFrame(list_of_results)
list_of_results['areas'] = array
print(list_of_results)
#plt.axhline(y = 129000, color='red')
#plt.axhline(y = 213000, color='red')
#plt.axhline(y = 45000, color='red')
plt.show()"""
"""import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
df = pd.read_csv('canada_per_capita_income.csv')
reg = linear_model.LinearRegression()
reg.fit(df[['year']], df[['per capita income (US$)']])
df.plot.scatter('year', 'per capita income (US$)', color='red', marker='+')
plt.plot(df[['year']], reg.predict(df[['year']]), color='blue')
plt.show()
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle
# data according to tap.az (2020.04)
dict = {'area':[71,82,75.5,46,144.41,90,98,104,68,45,104,95,46,40,55,45,100,74,65,64,55,46,40,50,102,57,52,42,45,83,42,57,110,95,153,45,123,85,70,60,83],
        'location':['neftchiler','qarayev','shuvalan','khirdalan','new_yasamal','masazir','yasamal','nasimi','6th_micro','khirdalan','binaqadi','neftchiler','sumgayit','2nd_micro',
                    'khirdalan','nizami','ganja','4th_micro','ahmadli','nasimi','khirdalan','sumgayit','4th_micro','khirdalan','8th_micro','masazir','sumgayit','masazir','new_yasamal',
                    'khirdalan','khirdalan','ahmadli','9th_micro','binaqadi','ahmadli','mingachevir','nasimi','nasimi','mashtagha','binaqadi','hazi_aslanov'],
        'rooms':[2,2,3,1,3,3,2,3,2,1,3,2,2,2,3,2,4,2,2,2,3,2,2,2,4,2,2,1,1,2,2,2,3,2,3,2,3,2,2,2,3],
        'state_of_building':['new','new','old','new','new','new','new','new','old','new','new','new','old','old','new','old','old','new','new','new','new','old','old','new','new','new','old',
                             'new','new','new','old','new','new','new','new','old','new','new','old','old','new'],
        'price':[122000,93000,67000,16500,137900,100000,179000,185000,83000,34000,125000,123000,51000,59900,57000,48500,56000,13000,95000,98000,57000,50000,60000,45000,184000,62000,53000,
                 47000,58500,35000,43000,95000,173000,120000,140000,36500,190000,144000,22000,82000,119000]
        }
"""df = pd.DataFrame(dict)
reg = linear_model.LinearRegression()
reg.fit(df[['area']],df[['price']])
with open('reg_model_pickle', 'wb') as f:
    pickle.dump(reg, f)
print(reg.predict([[80]]))
plt.scatter(df[['area']],df[['price']], color='red', marker='+')
plt.plot(df[['area']], reg.predict(df[['area']]), color="blue")
plt.axhline(y=64000)
plt.show()"""
pd.set_option('max_columns', None)
df = pd.DataFrame(dict)
dummy = pd.get_dummies(df)
X = dummy.drop(['price', 'location_2nd_micro', 'state_of_building_old'], axis='columns')
y = df.price
model = linear_model.LinearRegression()
model.fit(X,y)
with open('model_area_price', 'wb') as f:
    pickle.dump(model, f)
print(X.head())
print(model.predict([[71,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]]))
print(model.score(X,y))
