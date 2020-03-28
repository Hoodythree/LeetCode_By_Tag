def maxSubArray(nums):
    nums_len = len(nums)
    if nums_len == 0:
        return 0
    dp = [0 for _ in range(nums_len)]
    dp[0] = nums[0]
    for i in range(1, nums_len):
        if dp[i - 1] >= 0:
            dp[i] = dp[i - 1] + nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)


n = int(input())
lines = input().split()
nums = []
for i in range(n):
    nums.append(int(lines[i]))
print(maxSubArray(nums))

