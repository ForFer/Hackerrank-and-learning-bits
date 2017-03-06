"""
Author: Fernando Collado (Following scikit-learn.org tutorials)
Github: ForFer
"""
import pandas
import matplotlib.pyplot as plt
import numpy as np

from sklearn.svm import SVR


#Obtain data
url= ""
names = ["", ""]
dataset = pandas.read_csv(url, names=names)

#Shape and sort data 
arr = sorted(dataset.values, key=lambda a:a[1])
X = np.array([x[0] for x in arr])
X.sort()
X = X.reshape(-1,1)
y = np.array([y[1] for y in arr]).ravel()

#Calculate SVregression
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
y_rbf = svr_rbf.fit(X, y).predict(X)


#Change this number to predict one specific value, or values
predict = 0

#Print specific predictions
print(svr_rbf.predict(np.array([predict]).reshape(-1,1)))

#Plot data and regression
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.hold('on')
plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
