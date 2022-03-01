""" Raised Incidence Model 

import raised_incidence as ri

ri.f(1, 1, 1)

"""

import numpy as np

def f(d, alpha, beta):
    """ Return f(d, alpha, beta) """
    return 1 + alpha * np.exp(-((d/beta)**2))

def p(d, alpha, beta, rho):
    """ Probability for the raised incidence model """
    fd = f(d, alpha, beta)
    return (rho*fd)/(1+rho*fd)

def map(d):
    """ write this """
    print("Make a map here!")
    return None

def dist(d, xyinc):
    distance_to_incinerator = None
    return distance_to_incinerator
