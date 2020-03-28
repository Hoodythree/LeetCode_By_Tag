# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# brute force + prefixSum
# def maxSubArray(nums):
#     n = len(nums)
#     max_sum = 0
#     for i in range(n):
#         sum = 0
#         for j in range(i, n):
#             sum += nums[j]
#             max_sum = max(sum, max_sum)
#     return max_sum

# optimized prefixSum
def maxSubArray(nums):
    n = len(nums)
    max_sum = nums[0]
    min_sum = 0
    prefixSum = 0
    for i in range(n):
        # prefix sum
        prefixSum += nums[i]
        # update max_sum
        max_sum = max(max_sum, prefixSum - min_sum)
        # update min_sum
        min_sum = min(min_sum, prefixSum)
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))