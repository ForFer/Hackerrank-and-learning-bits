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

You will be able to access Fred’s laptop charging log by reading from the file
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
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

url = "laptopBatteryData.txt"
names = ["class", "hours"]
dataset = pandas.read_csv(url, names=names)

#print(dataset.shape)
#print(dataset.describe())
#print(dataset.head(20))

#dataset.hist()
#plt.show()

arr = dataset.values
X = [x[0] for x in arr]
Y = [y[1] for y in arr]
validation_size = 20
seed = 13

X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

scoring='accuracy'

model = DecisionTreeClassifier()
name = 'CART'

kfold = model_selection.KFold(n_splits=10, random_state=seed)
cv_results = model_selection.cross_val_score(model, X_train, Y_train,
cv=kfold, scoring=scoring)
results.append(cv_results)
names.append(name)
msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
print(msg)



