import numpy as np
import matplotlib.pyplot as plt
import pickle
import sklearn

def gradient_descent(x, y):
    m_curr = b_curr = 0
    iterations = 100
    learning_rate = 0.08
    n = len(x)
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n)*sum([value**2 for value in (y - y_predicted)])
        md = -(1/n) * sum(x * (y - y_predicted))
        bd = -(1/n) * sum(y - y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        plt.plot(x, (m_curr*x + b_curr), color='red')

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])
with open('reg_model_pickle', 'rb') as f:
    reg_model = pickle.load(f)
print(reg_model.predict([[12]])) # loading another model from pickle file
gradient_descent(x, y)
# plt.show()

