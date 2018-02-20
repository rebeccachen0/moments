import numpy as np
from scipy.interpolate import interp1d

def W_ell(l, theta):
    return np.exp(-(l**2)*(theta**2)/4)


def moment(ell, C_ell):
    f = interp1d(ell, C_ell)
    int_ell = np.arange(np.min(ell), np.max(ell), 1)
    theta = np.linspace(0, 2*np.pi*(1./360), num=10)
    moment = []
    for t in theta:
        moment.append(np.sum((2*int_ell+1)*f(int_ell)*(W_ell(int_ell, t)**2))/(4*np.pi))
    return theta, moment

	