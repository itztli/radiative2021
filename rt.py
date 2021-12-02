#!/usr/bin/env python3

#author: vdelaluz@enesmorelia.unam.mx

# I = I exp(-K) + S (1-exp(-k))
from astropy.modeling import models
from astropy import units as u
import math

def k(x):
    return x

def K(x0,x,dx):
    return (dx/2.0)*(k(x)+k(x0))

def S(T,nu):
    S = models.BlackBody(temperature=T*u.K)
    return S(nu*u.Hz)

def T(x):
    return 5600 #K

nu = 12e9 #Hz
I = 0.0
N = 100
a = 0.0  #km
b = 10.0 #km
dx = (b-a)/float(N)

i=1
x0 = a
for layer in range(N):
    #x = x + dx
    x = a + i*dx
    I = I * math.exp(-K(x0,x,dx)) + S(T(x),nu)*(1.0 - math.exp(-K(x0,x,dx)))
    print(i,I)
    i = i + 1
    x0= x 


