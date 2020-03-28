# monotonic stack
# from top to bottom,elements are monotonically increasing
# Example 2:

# Input: [2,7,4,3,5]
# Output: [7,0,5,5,0]

def nextLargerNodes(nums):
    # convert to list
    if not nums:
        return
    l = len(nums)
    res = [0] * l 
    stack = []
    for i in range(l):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    return res


if __name__ == '__main__':
    nums = [2, 7, 4, 3, 5]
    print(nextLargerNodes(nums))
