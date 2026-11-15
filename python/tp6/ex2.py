#CAS1
#1-le programe simyle un lance d'une piece de monaie
#2-
def simul_X():
    nbr=0
    for i in range(3):
        x=rd.random()
        if x<1/3:
            nbr+=1
    return nbr
#3-

import numpy.random as rd
import matplotlib.pyplot as plt
Labs=[simul_X() for i in range(0,10000)]
bins=[-0.5+k for k in range(5)]
plt.hist(Labs,bins,edgecolor='k')
plt.show()
#CAS2
import numpy as numpy
import numpy.random as rd
def T(n):
    S=0
    T=0
    while S<n:
        tirage=rd.randint(1,n+1)
        S+=tirage
        T+=1
    return T