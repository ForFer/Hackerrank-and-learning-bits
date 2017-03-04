"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np

from sklearn import model_selection
from sklearn import linear_model

url = ""
names = ["", ""]
dataset = pandas.read_csv(url, names=names)

#dataset.hist()
#plt.show()

arr = dataset.values

#remove reshape if there are more than 1 attribute
X = np.array([x[0] for x in arr]).reshape(-1,1) 
Y = np.array([y[1] for y in arr]).reshape(-1,1)

reg = linear_model.LinearRegression()
reg.fit(X,Y)

print("Coefficients: ", reg.coef_)

print("Variance score: %.2f" % reg.score(X, Y))

plt.scatter(X,Y, color='black')
plt.plot(X,reg.predict(X), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()


