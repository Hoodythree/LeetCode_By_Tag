import math

def get_uncertainty(tp, N):
    k = len(N)
    avarage = sum(N) / k
    s = 0
    for n in N:
        s += (n - avarage) ** 2
    res = math.sqrt(s / (k * (k - 1)))
    return tp * res

N = [i for i in range(5)]
print(get_uncertainty(0.1, N))