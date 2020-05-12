'''
编写函数，有一个参数（数列的长度n），返回该数列（以元组或列表的方式返回）
数列描述：k(0)=1,k(1)=1,…k(n)=（k(n-1))^2+(k(n-2))^2,
其中，k(n)表示该数列的第n个元素。在主函数中用户输入n, 调用子函数，接收返回结果并输出。

'''

# Recursion
def get_series(n):
    assert isinstance(n, int) and n >= 0, 'Input Error!'
    if n < 2:
        return 1
    else:
        return pow(get_series(n - 1), 2) + pow(get_series(n - 2), 2)

# Iteration
def get_series_by_iteration(n):
    assert isinstance(n, int) and n >= 0, 'Input Error!'
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    series = [1, 1]
    for i in range(2, n+1):
        series.append(pow(series[i-1], 2) + pow(series[i-2], 2))
    return series

def main():
    n = input('Please input n : ')
    n = int(n)
    # series = []
    # for i in range(n+1):
    #     series.append(get_series(i))
    # print(series)
    print(get_series_by_iteration(n))


if __name__ == '__main__':
    main()