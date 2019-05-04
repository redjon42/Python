
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as pl
import csv


class LV:

    def __init__(self, d,
                 p=np.array([2, .7, .8, .6]),
                 s=np.array([10, 10])):
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
        self.dat_x = self.data[0]
        self.dat_y = self.data[1]
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


def loss(m, d, n=101):
    """
    :param m: model data [x,y], t
    :param d: sample data [x,y], t
    :param n: sample size, length of data
    :return: MSE
    """
    mod = m.data[0]
    dat = d.data[0]
    dif_x = (mod[0] - dat[0])**2
    dif_y = (mod[1] - dat[1])**2
    dif = dif_x + dif_y
    mse = np.mean(dif)
    return mse


def data_lv():
    d = read_data()
    lv_out = LV(d)
    return lv_out


def ideal_model():
    model, t = solve(data_lv())
    return model, t


def ideal_fig():
    """
    dat[0]: x,y
    dat[1]: t
    """
    dat = ideal_model()
    rabbits, foxes = dat[0]
    fig = pl.figure()
    pl.plot(dat[1], rabbits, 'ro-', linewidth=.7, label='Prey')
    pl.plot(dat[1], foxes, 'bo-', linewidth=.7, label='Predator')
    pl.grid()
    pl.legend(loc='best')
    pl.xlabel('time')
    pl.ylabel('population')
    pl.title('Idealized Predator/Prey Model')
    return fig


def make_noise(sd=1, seed=12345):
    ideal = ideal_model()

    np.random.seed(seed)
    norm_1 = np.random.normal(0, sd, 101)
    np.random.seed(seed+1)
    norm_2 = np.random.normal(0, sd, 101)

    noise_x = ideal[0][0] + norm_1
    noise_y = ideal[0][1] + norm_2
    time = range(101)

    new_data = np.array([noise_x, noise_y, time])
    new_lv = LV(new_data)
    return new_lv


def noise_fig():
    fig = ideal_fig()
    new = make_noise().data

    new_x = new[0]
    new_y = new[1]

    pl.plot(new_x, 'c+--', linewidth=.5, label='Prey Noise')
    pl.plot(new_y, 'm+--', linewidth=.5, label='Pred Noise')
    return fig


def calculate_loss():
    lv1 = data_lv()
    lv2 = make_noise()
    temp = loss(lv1, lv2)
    return temp


#pl.show(noise_fig())
#print(calculate_loss())





