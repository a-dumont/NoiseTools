import numpy as np
import scipy.constants as C

def linear(x,a,b):
    """
    Simple linear equation
    """
    return a*x+b

def quadratic(x,a,b,c):
    """
    Simple quadratic equation
    """
    return a*x**2+b*x+c

def gaussian(x,mu,sigma):
    """
    Gaussian distribution function
    """
    return 1.0/np.sqrt(2*np.pi*sigma**2)*np.exp(-1.0*(x-mu)**2/(2*sigma**2))

def xcoth(x):
    """
    This functions returns the x/tanh(x) and does the proper thing
    when x=0.
    Borrowed from pyHegel
    """
    x = np.asanyarray(x)
    nx = np.where(x==0, 1e-16, x)
    return nx/np.tanh(nx)

def voltageNoiseTunnelJunction(V,f,T,R):
    """
    Returns the expected voltage fluctuations of a tunnel junction
    for the given parameters.
    """
    # Positive eV
    Sf = 4*C.k*T*R*xcoth((C.h*f+C.e*V)/2/C.k/T)

    # Negative eV
    Sff = 4*C.k*T*R*xcoth((C.h*f-C.e*V)/2/C.k/T)

    # Return symmetrized noise
    return 0.5*(Sf+Sff)

def voltageNoiseResistor(f,T,R):
    return voltageNoiseTunnelJunction(0,f,T,R)

def currentNoiseTunnelJunction(V,f,T,R):
    """
    Returns the expected voltage fluctuations of a tunnel junction
    for the given parameters.
    """
    # Positive eV
    Sf = 4*C.k*T/R*xcoth((C.h*f+C.e*V)/2/C.k/T)

    # Negative eV
    Sff = 4*C.k*T/R*xcoth((C.h*f-C.e*V)/2/C.k/T)

    # Return symmetrized noise
    return 0.5*(Sf+Sff)

def currentNoiseResistor(f,T,R):
    return currentNoiseTunnelJunction(0,f,T,R)
