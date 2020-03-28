       
def integer_breaking(num):
    dynamic_programming = [1 for i in range(num + 1)]
    for i in range(1, num + 1):
        if i % 2 == 1:
            dynamic_programming[i] = dynamic_programming[i - 1]
        else:
            dynamic_programming[i] = dynamic_programming[i - 1] + dynamic_programming[i // 2]
    return dynamic_programming[-1] % 10000000


def dfs(n,m):
    if n==0:
        return 1
    elif m==0:
        return 0
    elif n==1 or m==1:
        return 1
    elif n<m:
        return dfs(n,n)
    elif n==m:
        return dfs(n,m-1)+1
    else:
        return dfs(n,m-1)+dfs(n-m,m)

if __name__ == '__main__': 
    n = int(input()) 
    res = []
    for i in range(n): 
        x = int(input()) 
        res.append(x)
    for r in res:
        print(dfs(r, r))