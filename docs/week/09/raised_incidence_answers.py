""" Raised Incidence Model 

import this as "ri", then you can switch
between this and your raised_incidence.py 
functions easily:

import ri_answers as ri
ri.f(1, 1, 1)

"""

import numpy as np
import matplotlib

def f(d, alpha, beta):
    """ Return f(d, alpha, beta) """
    return 1 + alpha * np.exp(-((d/beta)**2))

def p(d, alpha, beta, rho):
    """ Probability for the raised incidence model """
    fd = f(d, alpha, beta)
    return (rho*fd)/(1+rho*fd)

def map(d, xyinc):
    xi = xyinc['x']
    yi = xyinc['y']
    cmap = matplotlib.colors.ListedColormap(["grey", "black"])
    p = d.plot.scatter(x="x",y="y",c="cc", colormap=cmap, marker="+")
    p.plot(xi, yi, marker="D", color="red")
    p.set_aspect(1.0)
    return None


def dist(d, xyinc):
    dx = d["x"] - xyinc["x"]
    dy = d["y"] - xyinc["y"]
    d = np.sqrt(dx**2 + dy**2)
    return d


def loglik(distance, cc, alpha, beta, rho):
    ppp = p(distance, alpha, beta, rho)
    ppp[cc==0] = 1 - ppp[cc==0]
    return np.log(ppp).sum()

