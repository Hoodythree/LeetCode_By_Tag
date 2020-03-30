def med(nums):
    l = len(nums)
    nums.sort()
    return nums[l // 2] if l%2 != 0 else (nums[l // 2] + nums[l // 2 - 1])/2

def variance(nums):
    average = sum(nums) / len(nums)
    s = 0
    for n in nums:
        s += (n - average) ** 2
    return s / len(nums)

nums = input('please input: ').split()
nums = [int(n) for n in nums]
print('median : {}\nvariance : {}'.format(med(nums), variance(nums)))