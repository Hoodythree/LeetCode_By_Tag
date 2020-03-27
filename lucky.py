# 123456
# 233008
def is_lucky(num):
    temp = num
    a = []
    b = []
    i = 0
    j = 0
    while(i < 3):
        last = temp % 10
        a.append(last)
        temp //= 10
        i += 1
    while(j < 3):
        first = temp % 10
        b.append(first)
        temp //= 10
        j += 1
    return sum(a) == sum(b)


if __name__ == '__main__': 
    n = int(input()) 
    res = []
    for i in range(n): 
        x = int(input()) 
        res.append(x)
    for r in res:
        if is_lucky(r):
            print('You are lucky!')
        else:
            print('Wish you good luck.')

