# 1. 输出1000以内各位数字之和为10的素数。
from math import sqrt, ceil
count = 0
for n in range(1, 1000):
    ones = n % 10
    tens = (n // 10) % 10
    hundreds = (n // 100) % 10
    total = ones + tens + hundreds
    if total == 10:
        is_prime = True
        for i in range(2, ceil(sqrt(n))):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            print('prime No{}: {}'.format(count, n))
    else:
        continue
    
