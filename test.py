
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
    n,m=map(int,raw_input().split()) #如果没有限制，即m<=n即可，则将下一行中的m改成n即可
    print(dfs(n, m))
