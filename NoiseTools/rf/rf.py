import numpy as np
import scipy.constants as C

def gamma(z0,zL):
    """
    Computes the reflexion coefficient gamma
    going from impedance z0 to impedance zL.
    """

    return (zL-z0)/(zL+z0)

def transmission(z0,zL):

    """
    Computes the transmission coefficient
    going from impedance z0 to impedance zL.
    This function does not consider voltage
    dividers which needs to be done manually.
    """

    return 2*zL/(zL+z0)

def votlageDivider(z1,z2):
    """
    Computes the voltage divider coefficient
    for impedances z1 and z2.
    """

    return z2/(z1+z2)

def parallelImpedance(z1,z2):
    """
    Computes the total impedance of two parallel
    impedances.
    """
    return z1*z2/(z1+z2)

def gamma2impedance(gamma,z0):
    """
    Computes the imedance zL given gamma and
    z0.
    """

    return (1+gamma)/(1-gamma)*z0

def impedanceOfTerminatedLine(f,l,v,zL,z0):
    """
    Computes the impedance of a tranmission line of
    length l, propagation speed of v and characteristic
    impedance z0 terminated by an impedance zL at
    frequency f.
    """
    f = np.asarray(f)
    zL = np.asarray(zL)
    assert f.ndim <= 1, "f must be at most a 1d array."
    assert zL.ndim <= 1, "zL must be at most a 1d array."

    if((f.ndim != zL.ndim) and (zL.size != 1)):
        raise RuntimeError("f and zL must be of same size unless zL has size 1.")

    return z0*(zL+1j*z0*np.tan(2*np.pi*f*l/v))/(z0+1j*zL*np.tan(2*np.pi*f*l/v))

def impedanceOfCapacitor(f,c):
    """
    Returns the impedance of capacitor c
    at frequency f.
    """

    return 1.0/(1j*2*np.pi*f*c)

def impedanceOfInductor(f,L):
    """
    Returns the impedance of inductor L
    at frequency f.
    """

    return 1j*2*np.pi*f*L

def transmissionLineDelay(f,l,v):
    """
    Computes the accumulated delay, in radians
    at frequency f through a transmission line
    of length l and propagation speed v.
    """

    return 2*np.pi*f*l/v

def phaseUnwrap(signal):
    """
    Given a complex signal returns the unwrapped phase
    in radians
    """

    return np.unwrap(2.0*np.arctan(signal.imag/signal.real))/2.0
