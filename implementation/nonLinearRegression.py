"""
Author: Fernando Collado
Github: ForFer
"""

"""
Non-linear regression with plots
"""

import numpy as np
import matplotlib.pyplot as plt 


def Main():
    f, N = map(int, input().split())

    X = []
    y = []

    for _ in range(N):
        data = list(map(float, input().split()))
        X.append(data[0])
        y.append(data[1])    

    np_x = np.array(X)
    np_y = np.array(y)

    np_x = np.sort(np_x, kind='mergesort')


    n = int(input())
    predict = []
    for _ in range(n):
        predict.append(float(input()))

    plot(np_x, np_y, predict)

def plot(x,y,predicted):
    p1 = np.polyfit(np_x, np_y, deg=1)
    p2 = np.polyfit(np_x, np_y, deg=2)
    p3 = np.polyfit(np_x, np_y, deg=3)
    p4 = np.polyfit(np_x, np_y, deg=7)
    p5 = np.polyfit(np_x, np_y, deg=10)


    pl1 = plt.plot(np_x, np.polyval(p1,np_x), 'r-', label='Degree 1')
    pl2 = plt.plot(np_x, np.polyval(p2,np_x), 'b--', label='Degree 2')
    pl3 = plt.plot(np_x, np.polyval(p3,np_x), 'm:', label='Degree 3')
    pl4 = plt.plot(np_x, np.polyval(p4,np_x), 'g+', label='Degree 7')
    pl5 = plt.plot(np_x, np.polyval(p5,np_x), 'o--', label='Degree 10')
    
    plt.legend(['d1','d2','d3','d7','d10'])
    
    plt.show()

if __name__=="__main__":
    Main()
