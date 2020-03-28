# fast slow pointer
# 1,1,1,1,2,3,4,4,4,5,5,6,7


def removeDuplicates(nums):
    l = len(nums)
    slow = 0
    fast = 0
    while fast < l:
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            fast += 1
            nums[slow] = nums[fast-1]
    return nums[:slow+1]

nums = [1,1,1,1,2,3,4,4,4,5,5,6,7]
print(removeDuplicates(nums))