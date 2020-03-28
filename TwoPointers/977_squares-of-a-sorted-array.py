def sortedSquares(A):
    l = len(A)
    res = [0] * l
    left, right = 0, (l - 1)
    while left <= right:
        if A[left] ** 2 > A[right] ** 2:
            res[l - 1] = A[left] ** 2
            left += 1
        else:
            res[l - 1] = A[right] ** 2
            right -= 1
        l -= 1
    return res

if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    print(sortedSquares(nums))