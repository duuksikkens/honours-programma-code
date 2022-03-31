c = 1

a = [c, -1/4*c]
iterations = 100
for k in range(0, iterations+1):
    a_new = (-k**2-2*k)*a[-2] +\
            (-3*k**2-11*k-9)*a[-1]
    a_new /= 2*k**2+10*k+12
    a.append(a_new)

eps = 0.9

print(a)

print(a[-1]/a[-1])

s = 0
for i in range(len(a)):
    s += a[i]*(1-eps)**i
print(s)


