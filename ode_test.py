from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as p

'''
LV system:

dx/dt = x*(a - b*y)
dy/dt = -1*y*(g - d*x)
'''


def pop(y, t, alp, bet, gam, dlt):
    x1, x2 = y
    dxy_dt = [x1 * (alp - (bet * x2)),
              -1 * x1 * (gam - (dlt * x2))]
    return dxy_dt


def d1(y, t, alp, bet, gam, dlt):
    dy_dt = np.array([alp * y[0] - bet * y[0] * y[1],
                     -gam * y[1] + dlt * y[0] * y[1]])
    return dy_dt


'''
We assume the constants are 
alpha = 2,
beta = .7,
gamma = .8,
delta = .6:
'''
alp = 2
bet = .7
gam = .8
dlt = .6

"""
with equilibrium points (0,0) and (g/d, a/b)

y_f0 = np.array([0.0, 0.0])
y_f1 = np.array([gam/dlt, alp/bet])
all(d1(y_f0, 0, alp, bet, gam, dlt) == np.zeros(2)) and all(
    d1(y_f1, 0, alp, bet, gam, dlt) == np.zeros(2))


def jaco(y, t, alp, bet, gam, dlt):
    #Return the Jacobian matrix evaluated in X. 
    d2y_dt2 = np.array([[alp - bet * y[1], -bet * y[0]],
                       bet * dlt * y[1], -gam + dlt * y[0]])
    return d2y_dt2


# saddle points near zeros
# sad_f1 = jaco(y_f1, 0, alp, bet, gam, dlt)
# eigen values
# lambda1, lambda2 = np.linalg.eigvals(sad_f1)
# period of cycle
# t_f1 = 2*np.pi/abs(lambda1)
"""

'''
For initial conditions, 
x1(0) = 10
x2(0) = 10.
'''
y0 = [10.0, 10.0]
'''
We will generate a solution at 101 evenly spaced samples 
in the interval 0 <= t <= 100. So our array of times is
'''
t = np.linspace(0, 100, 101)
'''
Call odeint to generate the solution. 
To pass the parameters a,b,g,d to pop, 
we give them to odeint using the args argument.
'''
#sol = odeint(pop, y0, t, args=(alp, bet, gam, dlt))
"""
From tutorial:
"""
y, info_dict = odeint(d1, y0, t, args=(alp, bet, gam, dlt), full_output=True)
print(info_dict['message'])

"""plots"""
rabbits, foxes = y.T
f1 = p.figure()
p.plot(t, rabbits, 'r-', label='Rabbits')
p.plot(t, foxes, 'b-', label='Foxes')
p.grid()
p.legend(loc='best')
p.xlabel('time')
p.ylabel('population')
p.title('Evolution of fox and rabbit populations')
p.show()

