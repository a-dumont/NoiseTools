import numpy as np
import scipy.constants as C
from NoiseTools import fitFunctions as ff
from NoiseTools import rf

class Resistor(object):
    """
    Class containing static methods that are
    useful for dealing with resistors.
    """
    def __init__(self):
        return

    @staticmethod
    def VI(I,R):
        """
        Computes V(I) for a given R
        """
        return R*I

    @staticmethod
    def IV(V,R):
        """
        Computes I(V) for a given R
        """
        return 1.0*V/R

    @staticmethod
    def voltageNoise(f,T,R):
        """
        Computes ther voltage noise at frequency
        f,temperature T for a resistor of value R.
        """
        return ff.voltageNoiseResistor(f,T,R)

    @staticmethod
    def currentNoise(f,T,R):
        """
        Computes ther current noise at frequency
        f,temperature T for a resistor of value R.
        """
        return ff.currentNoiseResistor(f,T,R)

class Capacitor(object):
    """
    Class containing static methods that are
    useful for dealing with capacitors.
    """
    def __init__(self):
        return

    @staticmethod
    def Z(f,c):
        return 0.0-1.0j/(2*np.pi*f*c)

    @staticmethod
    def VI(I,f,c):
        """
        Computes V(I) for a given frequency f
        and capacity c.
        """
        return Capacitor.Z(f,c)*I

    @staticmethod
    def IV(V,R):
        """
        Computes I(V) for a given frequency f
        and capacity c.
        """
        return 1.0*V/Capacitor.Z(f,c)

class Inductor(object):
    """
    Class containing static methods that are
    useful for dealing with inductors.
    """
    def __init__(self):
        return

    @staticmethod
    def Z(f,L):
        return 0.0+1.0j*2*np.pi*f*L

    @staticmethod
    def VI(I,f,L):
        """
        Computes V(I) for a given frequency f
        and inductance L.
        """
        return Inductor.Z(f,L)*I

    @staticmethod
    def IV(V,R):
        """
        Computes I(V) for a given frequency f
        and inductance L.
        """
        return 1.0*V/Inductor.L(f,L)


class TunnelJunction(object):
    """
    Class containing static methods that are
    useful for dealing with tunnel junction.
    """
    def __init__(self):
        return

    @staticmethod
    def VI(dVdI,dI):
        """
        Computes V(I) for a given dV/dI and dI.
        """
        assert type(dVdI) is np.ndarray, "dVdI must be a 1d array"
        assert dVdI.ndim == 1, "dVdI must be a 1d array"
        dI = np.asarray(dI)
        if(dI.ndim==0):
            dI = dI*np.ones(dVdI.shape[0])
        V  = np.array([(dVdI[0:i]).sum()*dI[i] for i in range(dVdI.shape[0])])
        return V

    @staticmethod
    def IV(dIdV,dV):
        """
        Computes I(V) for a given dI/dV and dV.
        """
        assert type(dIdV) is np.ndarray, "dVdI must be a 1d array"
        assert dIdV.ndim == 1, "dVdI must be a 1d array"
        dV = np.asarray(dV)
        if(dV.ndim==0):
            dV = dV*np.ones(dIdV.shape[0])
        I  = np.array([(dIdV[0:i]).sum()*dV[i] for i in range(dIdV.shape[0])])
        return I

    @staticmethod
    def voltageNoise(V,f,T,R):
        """
        Computes ther voltage noise at bias voltage V
        frequency f, temperature T for a resistor of
        value R.
        """
        return ff.voltageNoiseTunnelJunction(V,f,T,R)

    @staticmethod
    def currentNoise(V,f,T,R):
        """
        Computes ther current noise at bias voltage V,
        frequency f, temperature T for a resistor of
        value R.
        """
        return ff.currentNoiseTunnelJunction(V,f,T,R)
