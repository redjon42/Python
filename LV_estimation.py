
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as pl
import csv


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

        self.y0 = [s[0], s[1]]
        self.t = np.array(self.data[2])


def d1(y, t, alp, bet, gam, dlt):
    dy_dt = np.array([alp * y[0] - bet * y[0] * y[1],
                     -gam * y[1] + dlt * y[0] * y[1]])
    return dy_dt


def solve(lv):
    """
    :param lv: Class LV instance
    :return:
    """
    y0 = lv.y0
    t = lv.t
    sol, info_dict = odeint(d1, y0, t,
                            args=(lv.alpha, lv.beta, lv.gamma, lv.delta),
                            full_output=True)
    return sol.T, t


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


def make_lv():
    d = read_data()
    p = np.array([2, .7, .8, .6])
    s = np.array([10, 10])
    lv_out = LV(d, p, s)
    return lv_out


def make_model():
    model, t = solve(make_lv())
    return model, t


def model_plot():
    dat = make_model()
    rabbits, foxes = dat[0]
    f1 = pl.figure()
    pl.plot(dat[1], rabbits, 'r-', label='Prey')
    pl.plot(dat[1], foxes, 'b-', label='Predator')
    pl.grid()
    pl.legend(loc='best')
    pl.xlabel('time')
    pl.ylabel('population')
    pl.title('Idealized Predator/Prey Model')
    return f1


pl.show(model_plot())




