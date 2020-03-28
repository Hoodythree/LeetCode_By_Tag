# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# brute force -> binary search

def countNegatives(grid):
    count = 0
    for i in range(len(grid)):
        start, end = 0, len(grid[0]) - 1
        while start <= end:
            mid = (start + end) // 2
            if grid[i][mid] < 0:
                count += (end - mid + 1)
                end = mid - 1
            else:
                start = mid + 1
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))