#Program: Calculate the circumference of an ellipse with different methods
#Author: Duuk Sikkens
#Created: 30/3/2021
#Last edited: 30/3/2021 by Duuk Sikkens

from math import sqrt, pi

#FUNCTIONS==================================

def dubbelfact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*dubbelfact(n-2)

#DECLARATION CONSTANTS======================

a = 2 #major axis
b = 1 #minor axis

N = 100

#===========================================

#Ramanujans empirically found formula
L = (a-b)/(a+b)
E = (1 + (3*L**2)/(10+sqrt(4-3*L**2)))*pi*(a+b)
print(E)

#simple geometric-arithmetic mean approximation (N=2)
E = 2*pi*((a+b)/(sqrt(a)+sqrt(b)))**2
print(E)

#series from report (N=N)
eps = sqrt(1 - b**2/a**2)
s = 1
for k in range(1,N+1):
    addend = (dubbelfact(2*k-1)/dubbelfact(2*k))**2 * eps**(2*k)/(1-2*k)
    s += addend
E = 4*a*pi/2*s
print(E)

#geometric-arithmetic mean approximation (N=N)
geom = [b]
arit = [a]
c = [sqrt(a**2-b**2)]
for _ in range(N):
    geom.append(sqrt(geom[-1]*arit[-1]))
    arit.append((geom[-1]+arit[-1])/2)
    c.append(sqrt(arit[-1]**2-geom[-1]**2))

M = arit[-1]
print(M)

S = 0
for i in range(N+1):
    S += 2**i*c[i]**2

E = 2*pi/M*(a**2-1/2*S)
print(E)
