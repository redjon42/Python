
import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as mplot
import pandas as pd
import csv

"""
def dX_dt(X, t=0): 
    return array([ a*X[0] -   b*X[0]*X[1] ,  
                  -c*X[1] + d*b*X[0]*X[1] ])
"""


class LV:

    def __init__(self, d, p, s):
        """
        :param d: a np array of [ [x1], [x2], and [time] ] sublist-vectors.
        :param p: a np array of parameters a,b , g,d.
        :param s: state np array
        """
        self.data = np.array(d)

        self.pars = np.array(p)
        self.alpha = self.pars.item(0)
        self.beta = self.pars.item(1)
        self.gamma = self.pars.item(2)
        self.delta = self.pars.item(3)

        self.x0 = s.item(0)
        self.y0 = s.item(1)


def model_x(t, x):
    """
    p = np.array([2, .7, .8, .6])  s = np.array([10, 10])
    """
    return x * (2 - .7*t)


def model_y(t, x):
    return -1*x * (.8 - .6*t)


def solve(lv_0):
    """
    :param lv_0: Class LV instance
    :return:
    """
    model_x1 = integrate.RK23(model_x,
                              t0=lv_0.data[2, 0],
                              t_bound=lv_0.data[2, -1],
                              y0=[lv_0.x0],
                              vectorized=True)
    model_x2 = integrate.RK23(model_y,
                              t0=lv_0.data[2, 0],
                              t_bound=lv_0.data[2, -1],
                              y0=[lv_0.y0],
                              vectorized=True)
    return model_x1, model_x2


def read_data():
    with open('/Users/geneva/Desktop/Thesis/out_x.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        out_x = list()
        for line in csv_reader:
            out_x.append(line[1])
        del out_x[0]
        for i in range(len(out_x)):
            out_x[i] = float(out_x[i])
    csv_file.close()

    with open('/Users/geneva/Desktop/Thesis/out_y.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        out_y = list()
        for line in csv_reader:
            out_y.append(line[1])
        del out_y[0]
        for i in range(len(out_y)):
            out_y[i] = float(out_y[i])
    csv_file.close()

    return np.array([out_x, out_y, range(101)])


def loss(m2, d0):
    """
    :param m2: output of solve() 2-part model
    :param d0: data output of read_data()
    :return: MSE
    """
    mx = m2[0]
    my = m2[1]
    dx = 0
    return mx


def lv_test():
    d = read_data()
    p = np.array([2, .7, .8, .6])
    s = np.array([10, 10])
    test = LV(d, p, s)
    return solve(test)





print(lv_test()[0])


sol = lv_test()[0]
print(sol.y[0])
mplot.plot(sol.t, sol.y[0])
mplot.show()


t0 = 0
tf = 10
x0 = 0


def F(t, x): return x*t + 2


sol = integrate.RK23(F, t0, [x0], tf)
for y in sol.y:
    print(y)
fig, ax = mplot.subplots()
ax.plot(sol.t, sol.y[0])
mplot.show()


'''
test = lv_test()
test = test[0]
test = test.y
for x in test:
    print(x)

d = read_data()
p = np.array([2, .7, .8, .6])
s = np.array([10, 10])
test = LV(d, p, s)
test = test.data
print(test[2, -1])
'''


