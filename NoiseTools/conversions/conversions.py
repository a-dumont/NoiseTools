import numpy as np
import scipy.constants as C

def dBm2Volts(dBm,R):
    return np.sqrt(10**(1.0*dBm/10)*1e-3*R)

def dBm2Amperes(dBm,R):
    return np.sqrt(10**(1.0*dBm/10)*1e-3/R)

def dBm2Watts(dBm):
    return 10**(1.0*dBm/10)*1e-3

def volts2dBm(V,R):
    return 10*np.log10((V**2/R)/1e-3)

def amperes2dBm(I,R):
    return 10*np.log10((I**2*R)/1e-3)

def watts2dBm(P):
    return 10*np.log10(P/1e-3)

def excessNoiseRatio22NoisePower(ENR,T=290):
    return (1+10**(1.0*ENR/10))*2*C.k*T

def excessNoiseRatio2Temperature(ENR,T=290):
    return (1+10**(1.0*ENR/10))*T

def noiseFigure2NoisePower(NF,T=290):
    return (10**(1.0*NF/10)-1)*2*C.k*T

def noiseFigure2Temperature(NF,T=290):
    return (10**(1.0*NF/10)-1)*T
