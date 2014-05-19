import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linearEq(x, m, c):
    return m*x + c

def linearRegression(vals):
    x = np.array(vals)
    y = linearEq(x, 2.0, 1.0)
    yn = y + 0.001*np.random.normal(size=len(x))
    popt, pcov = curve_fit(linearEq, x, yn)
    print popt, pcov
    plt.figure()
    plt.plot(x, yn, 'ko', label="Original Noised Data")
    plt.plot(x, linearEq(x, *popt), 'r-', label="Fitted Curve")
    plt.legend()
    plt.show()




linearRegression([i for i in range(50)])