# Input: [2,2,1,1,1,2,2]
# Output: 2
def majorityElement(nums):
    res = sorted(nums)
    return res[len(nums)//2]


nums = [3,2,3]
print(majorityElement(nums))