
import scipy as sp
import numpy as np
import matplotlib as plot
import pandas as pd

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

        self.model_pars = np.array([self.data[0] * (self.alpha - self.beta*self.data[1]),
                               self.data[1] * (self.gamma - self.delta*self.data[1])])


        def model(self):
            dx1 = self.data[0] * (self.alpha - self.beta * self.data[1])
            dx2 = self.data[1] * (self.gamma - self.delta * self.data[1])



        def solve(self):













