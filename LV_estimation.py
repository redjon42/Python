
import scipy.integrate as integrate
import numpy as np
import matplotlib as plot
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

    def model_x(self, x, t):
        return x * (self.alpha - self.beta*t)

    def model_y(self, x, t):
        return -1 * x * (self.gamma - self.delta * t)

    def solve(self):
        model_x1 = integrate.RK23(self.model_x(x=self.data[0], t=self.data[2]),
                                  t0=self.data[2, 0],
                                  t_bound=self.data[2, -1],
                                  y0=[self.x0])
        model_x2 = integrate.RK23(self.model_x(x=self.data[1], t=self.data[2]),
                                  t0=self.data[2, 0],
                                  t_bound=self.data[2, -1],
                                  y0=[self.y0])
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


def lv_test():
    d = read_data()
    p = np.array([2, .7, .8, .6])
    s = np.array([10, 10])
    test = LV(d, p, s)
    return test.solve()


print(lv_test())
