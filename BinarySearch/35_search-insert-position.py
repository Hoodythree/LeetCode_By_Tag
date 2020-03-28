# Input: [1,3,5,6], 5
# Output: 2
# Input: [1,3,5,6], 2
# Output: 1
def searchInsert(nums, target):
    low, high = 0, len(nums) - 1
    while low < high:
        if nums[low] > target:
            return low 
        elif nums[high] < target:
            return high
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low+1


nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))



