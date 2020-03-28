# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] 
# in ascending order to make the whole array sorted in ascending order.

def findUnsortedSubarray(nums):
    if sorted(nums) == nums:
        return 0
    nums_len = len(nums)
    min_len = nums_len
    for i in range(nums_len):
        for j in range(i+1, nums_len):
            # if sorted(nums[i:j+1]) == nums[i:j+1]:
            #     continue
            min_of_subarr = min(nums[i:j+1])
            max_of_subarr = max(nums[i:j+1])
            max_left = max(nums[0:i]) if i!=0 else float('-inf')
            min_right = min(nums[j+1:]) if j!=nums_len-1 else float('inf')
            if max_left <= min_of_subarr and min_right >= max_of_subarr:
                if sorted(nums[0:i+1]) == nums[0:i+1] and sorted(nums[j+1:]) == nums[j+1:]:
                    min_len = min(min_len, j-i+1)
                else:
                    continue
            else:
                continue
    return min_len


nums1 = [1, 3, 2, 2, 2]
nums2 = [2,6,4,8,10,9,15, 13, 12]
print(findUnsortedSubarray(nums1))
print(findUnsortedSubarray(nums2))