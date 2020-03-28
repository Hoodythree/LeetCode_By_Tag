# k=0
# 将none-zero元素移动到k,
# k++
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(nums):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
        else:
            fast += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    return nums


nums =  [0,1,0,3,12]
print(moveZeroes(nums))
