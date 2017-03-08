"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
The Problem

Charlie wants to purchase office-space. He does a detailed survey of the offices
and corporate complexes in the area, and tries to quantify a lot of factors,
such as the distance of the offices from residential and other commercial areas,
schools and workplaces; the reputation of the construction companies and
builders involved in constructing the apartments; the distance of the offices
from highways, freeways and important roads; the facilities around the office
space and so on.

Each of these factors are quantified, normalized and mapped to values on a scale
of 0 to 1. Charlie then makes a table. Each row in the table corresponds to
Charlie's observations for a particular house. If Charlie has observed and noted
F features, the row contains F values separated by a single space, followed by
the office-space price in dollars/square-foot. If Charlie makes observations for
H houses, his observation table has (F+1) columns and H rows, and a total of
(F+1) * H entries.

Charlie does several such surveys and provides you with the tabulated data. At
the end of these tables are some rows which have just F columns (the price per
square foot is missing). Your task is to predict these prices. F can be any
integer number between 1 and 5, both inclusive.

There is one important observation which Charlie has made.

    The prices per square foot, are (approximately) a polynomial function of the
features in the observation table. This polynomial always has an order less than
4

Input Format

The first line contains two space separated integers, F and N. Over here, F is
the number of observed features. N is the number of rows for which features as
well as price per square-foot have been noted.
This is followed by a table having F+1 columns and N rows with each row in a new
line and each column separated by a single space. The last column is the price
per square foot.

The table is immediately followed by integer T followed by T rows containing F
columns.

Constraints

1 <= F <= 5
5 <= N <= 100
1 <= T <= 100
0 <= Price Per Square Foot <= 10^6 0 <= Factor Values <= 1

Output Format

T lines. Each line 'i' contains the predicted price for the 'i'th test case. 
"""

import numpy as np
import matplotlib.pyplot as plt 


from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures as polyF
from sklearn.pipeline import make_pipeline

f, N = map(int, input().split())

X = []
y = []

for _ in range(N):
    data = list(map(float, input().split()))
    x = [data[i] for i in range(f)]
    X.append(x)
    y.append(data[len(data)-1])    

n = int(input())
predict = []
for _ in range(n):
    data = list(map(float, input().split()))
    predict.append(data)

poly = polyF(degree=3)

#Shape and sort data
X.sort() 
X = np.array(X)

y = np.array(y).ravel()

x = poly.fit_transform(X)

clf = linear_model.LinearRegression()
clf.fit(x, y)



print("X = ", x)
print("Predict= ", predict)
print("Prediction= ", clf.predict(predict))

