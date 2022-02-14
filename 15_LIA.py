def fac(x):
    if x == 1 or x == 0:
        return 1
    return fac(x-1)*x


def LIA(k, N):
    result = 0
    t = 2 ** k
    for i in range(N, t+1):
        result += (0.25 ** i ) * (0.75 ** (t - i)) * (fac(t) / fac(t-i) / fac(i))


    print(result)

LIA(5, 9)