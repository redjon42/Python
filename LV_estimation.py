
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

    def __init__(self, d, p):
        """
        :param d: a list of [ [x1], [x2], and [time] ] sublist-vectors.
        :param p: a list of parameters a,b , g,d.
        """
        self.data = np.array(d)

        self.pars = np.array(p)
        self.alpha = self.pars[0]
        self.beta = self.pars[1]
        self.gamma = self.pars[2]
        self.delta = self.pars[3]

        self.x0 = np.mean(self.data[0])
        self.y0 = np.mean(self.data[1])

    def model(self):
        dx1 = self.x0 * (self.alpha - self.beta * self.y0)
        dx2 = self.y0 * (self.gamma - self.delta * self.x0)
        return np.array([dx1, dx2])

    def solve(self):
        model_x1 = integrate.RK23(self.model()[0], t0=self.data[2,0],
                                  t_bound=self.data[2,-1],
                                  y0=self.x0)
        model_x2 = integrate.RK23(self.model()[1], t0=self.data[2, 0],
                                  t_bound=self.data[2,-1],
                                  y0=self.y0)
        return np.array([model_x1, model_x2])


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

    return np.array([out_x, out_y])

def LV_test():



print(read_data())
