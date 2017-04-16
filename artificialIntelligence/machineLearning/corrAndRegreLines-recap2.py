"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/correlation-and-regression-lines-7
"""

from sklearn import linear_model
import numpy as np

# Hardcoded arrays
n_phy = np.array([15, 12, 8, 8, 7, 7, 7, 6, 5, 3])
n_his = np.array([10, 25, 17, 11, 13, 17, 20, 13, 9, 15])

reg = linear_model.LinearRegression()
reg.fit(n_phy.reshape(-1, 1), n_his.reshape(-1, 1))
print('{0:.3f}'.format(reg.coef_[0][0])) # 0.208
