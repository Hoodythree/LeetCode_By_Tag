def power(base,exp):
    res = 1  # 保存结果
    while exp:  # 当指数不为0
        if exp & 1:  # 判断二进制最低位是否为1，如果为1，就把之前的幂乘到结果中。
            res *= base
        base *= base  # 一直累乘，构造 base^2 -> base^4 -> base^8 -> base^16 -> ...
        exp = exp >> 1  # 去掉指数的二进制最低位，继续判断
    return res


n = input()
print('2^{0} = {1}'.format(int(n), power(2, int(n))))