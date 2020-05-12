# 1. 输出1000以内各位数字之和为10的素数。
from math import sqrt, ceil

def is_prime(n):
    assert isinstance(n, int), print('Integer only')
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False
    return True

def sum_digit(n):
    assert isinstance(n, int), print('Integer only')
    ones = n % 10
    tens = (n // 10) % 10
    hundreds = (n // 100) % 10
    total = ones + tens + hundreds
    return total

def main():
    count = 0
    for n in range(1, 1000):
        if sum_digit(n) == 10 and is_prime(n):
            count += 1
            print('prime No{}: {}'.format(count, n))
        else:
            continue

if __name__ == '__main__':
    main()
    
