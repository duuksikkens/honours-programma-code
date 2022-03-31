from math import sqrt

def choose(r, k):
    if k == 0:
        return 1
    return (r-k+1) / k * choose(r, k-1)

r = 1/2
maxiter = 10000
choose = 1
s = 1
for k in range(1,maxiter+1):
    choose *= (1.5-k)/k
    s += choose
print(s)
print(sqrt(2))
