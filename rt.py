#!/usr/bin/env python3

#author: vdelaluz@enesmorelia.unam.mx

# I = I exp(-K) + S (1-exp(-k))
#from astropy.modeling import models
#from astropy import units as u
import math

def k_H20_4mm(x): #cm-1
    return 1.0

def k_H20_100micas(x): #cm-1
    return 120.0 #cm-1

#Bremsstrahlung
def k(n_e,nu,T,n_H):
    A = 9.78e-3*(n_e/((nu**2) * (T**(3/2))))*n_H
    if t< 2e5:
        return  A*(18.2+math.log(T**(3/2)) - math.log(nu)) 
    else:
        return  A*(24.5+math.log(T) - math.log(nu)) 
    

def Tau(dx,nu,n_e0,T0,n_H0,n_e1,T1,n_H1):
    return (dx/2.0)*(k(n_e0,nu,T0,n_H0)+k(n_e1,nu,T1,n_H1))

def S(T,nu):
    S = models.BlackBody(temperature=T*u.K)
    return S(nu*u.Hz)

#def T(x):
#    return 5600 #K

nu = 12e9 #Hz
I = 0.0
N = 100
a = 0.0  #km
b = 10.0 #km
dx = (b-a)/float(N)

with open('dummy.dat') as f:
    model = f.readlines();

x=[]
T=[]
n_H=[]
n_e=[]
    
for data in model:
    if data[0] == '#': continue
    data_str = data.split()
    x.append(float(data_str[0]))
    T.append(float(data_str[1]))
    n_H.append(float(data_str[2]))
    n_e.append(float(data_str[3]))
i=1
x0 = a
print(0,I)

for layer in range(N):
    #x = x + dx
    x = a + i*dx
    n_e0= n_e[i-1]
    T0= T[i-1]
    n_H0= n_H[i-1]
    n_e1= n_e[i]
    T1= T[i]
    n_H1= n_H[i]
    tau = Tau(dx,nu,n_e0,T0,n_H0,n_e1,T1,n_H1)
    I = I * math.exp(-tau) + S( (T0+T1)/2.0  ,nu)*(1.0 - math.exp(-tau))
    print(i,I)
    i = i + 1
    x0= x 


