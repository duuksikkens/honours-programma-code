from math import log, sqrt, pi
from numpy import arange

# Module: functions calculating Etilde and E
# Author: Duuk Sikkens
# Created: idk
# Last edited: 16/03/2022 by Duuk Sikkens


def Etilde(eta, iterations = 200, a_0 = 1., b_1 = 0., printterms = False, yieldlastterms = False):
    a_nm1 = a_0
    a_n = 3/8*a_0

    b_0 = -2*a_0
    b_n = b_1

    s_1 = a_0*eta**2 + a_n*eta**4
    s_2 = b_0 + b_1*eta**2

    for n in range(2, iterations):
        b_n = ((4*n-4)*a_nm1-(4*n-2)*a_n+(4*n**2-8*n+3)*b_n)/(4*n**2-4*n)
        s_2 += b_n*eta**(2*n)

        a_nm1 = a_n
        a_n = (2*n+1)*(2*n-1)/(2*n+2)/(2*n)*a_n
        s_1 += a_n*eta**(2*n+2)

        if printterms:
            print(f'voor n = {n}: term b = {b_n*eta**(2*n)}')
            print(f'voor n = {n}: term a = {a_n*eta**(2*n+2)}')


    beta = 1/b_0
    alpha = 1/a_0*(log(2)-1/4-beta*b_1)

    E = alpha*s_1 + beta*log(eta)*s_1 + beta*s_2

    if yieldlastterms:
        return E, a_n*eta**(2*n), b_n*eta**(2*n+2)
    else:
        return E

def E(eps, iterations = 200, printterms = False, yieldlastterm = False):
    c_n = pi/2
    E = c_n

    for n in range(1, iterations):
        c_n = (n-1.5)*(2*n-1)/(2*n**2)*c_n
        E += c_n*eps**(2*n)
        if printterms:
            print(f'voor n = {n}: term c = {c_n*eps**(2*n)}')
            
    if yieldlastterm:
        return E, c_n*eps**(2*n)
    else:
        return E

if __name__ == '__main__':
    #E = Etilde(eta, 1000)
    #print(E)
    epslst = arange(0, 1, 0.001)
    N = 1000
    firsttime = True
    for eps in epslst:
        """
        print('===================================================')
        print(f'eps = {eps}')
        print('===================================================')
        """
        eta = sqrt(1-eps**2)
        
        ETilde, aterm, bterm = Etilde(eta, N, 1., 0., False, True)
        Ee, cterm = E(eps, N, False, True)
        """
        print('Etilde:')
        print(f'E({round(eps, 3)}) = {ETilde}')
        print(f'Last a*eta^n term after {N} iterations: {aterm}')
        print(f'Last b*eta^n term after {N} iterations: {bterm}')
        print('')

        print('E:')
        print(f'E({round(eps, 3)}) = {Ee}')
        print(f'Last c*eta^n term after {N} iterations: {cterm}')
        print('')
        """
        if abs(aterm) < abs(cterm) and abs(bterm) < abs(cterm) and firsttime:
            firsttime = False
            epsfirsttime = eps

    print(f'epsilon first time that E tilde is better: {epsfirsttime}')
