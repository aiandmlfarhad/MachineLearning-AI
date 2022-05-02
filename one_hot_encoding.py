import pandas as pd
from sklearn import linear_model
import pickle
df = pd.read_csv('homeprices_ohe.csv')
dummy = pd.get_dummies(df)
X = dummy.drop(['price', 'town_west windsor'], axis='columns')
y = dummy.price
model = linear_model.LinearRegression()
model.fit(X, y)
with open('model_ohe', 'wb') as f:
    pickle.dump(model, f)
print(model.predict([[2600, 1, 0]]))
print(model.score(X,y))