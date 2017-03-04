"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
Fred is a very predictable man. For instance, when he uses his laptop, all he
does is watch TV shows. He always watches until his battery dies. He is also a
very meticulous man. He has kept logs of every time he has charged his laptop,
which includes how long he charged his laptop for and how long he was able to
watch TV for afterwards. Now, Fred wants to use this log to predict how long he
will be able to watch TV for when he starts so that he can plan his activites
after watching his TV shows accordingly.

Challenge

You will be able to access Fred's laptop charging log by reading from the file
“trainingdata.txt”. The training data file will consist of 100 lines, each with
2 comma-separated numbers. The first number denotes the amount of time the
laptop was charged and the second denotes the amount of time the battery lasted.
The training data file can be downloaded here (this will be the same training
data used when your program is run). The input for each of the test cases will
consist of exactly 1 number rounded to 2 decimal places. For each input, output
1 number: the amount of time you predict his battery will last.

Sample Input

1.50

Sample Output

3.00

Scoring

Your score will be 10-X, where X is the sum of the distances you are from
expected answer of each test case. For instance if there are 2 test cases with
expected answer 4 and you print 3 for the first one and 6 for the second one
your score will be 10-(1+2) = 7.
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np

from sklearn.svm import SVR

#url = "laptopBatteryData.txt"
url= "https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt"
names = ["class", "hours"]
dataset = pandas.read_csv(url, names=names)

arr = sorted(dataset.values, key=lambda a:a[1])
X = np.array([x[0] for x in arr])
X.sort()
X = X.reshape(-1,1)
y = np.array([y[1] for y in arr]).ravel()

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
y_rbf = svr_rbf.fit(X, y).predict(X)

n = float(input())

print(svr_rbf.predict(np.array([n]).reshape(-1,1)))
"""
lw = 2
plt.scatter(X, y, color='darkorange', label='data')
plt.hold('on')
plt.plot(X, y_rbf, color='navy', lw=lw, label='RBF model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()
"""
