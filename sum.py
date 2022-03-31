from math import log, sqrt
import numpy as np

def choose(a, k):
    if not type(k) == int or k < 0:
        raise ValueError

    if k == 0:
        return 1

    else:
        return (a-k+1)/k*choose(a, k-1)

N = 1000000
s = 0

for k in range(2, N+2):
    if k == 2:
        choose = choose(1/2, k)
    else:
        choose = choose*(1/2-k+1)/k
    s += choose/(k-1)

print(s)
print(2*log(2) + 3/2 - np.arcsinh(1) + 1/2*sqrt(2))
