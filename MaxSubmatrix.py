import bisect
def maxSumSubmatrix(matrix, k):
    def maxSumSubarray(arr):
        sub_s_max = float('-inf')
        s_curr = 0
        prefix_sums = [float('inf')]
        for x in arr:
            bisect.insort(prefix_sums, s_curr)
            s_curr += x
            i = bisect.bisect_left(prefix_sums, s_curr - k)
            sub_s_max = max(sub_s_max, s_curr - prefix_sums[i])
        return sub_s_max
    
    m, n = len(matrix), len(matrix[0])
    for x in range(m):
        for y in range(n - 1):
            matrix[x][y+1] += matrix[x][y]
    res = float('-inf')
    for y1 in range(n):
        for y2 in range(y1, n):
            arr = [matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0) for x in range(m)]
            res = max(res, maxSumSubarray(arr))
    return res


matrix = [[1,0,1],[0,-2,3]]
[[60 3 -65 -92 32 -70],
[-41 14 -38 54 2 29],
[69 88 54 -77 -46 -49],
[97 -32 44 29 60 64],
[49 -48 -96 59 -52 25]]
k = 2
print(maxSumSubmatrix(matrix, k))