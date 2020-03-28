# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]

def findDisappearedNumbers(nums):
    iter_end = len(nums) + 1
    ordered_nums = set([i for i in range(1, iter_end)])
    nums = set(nums)
    return list(ordered_nums - nums)    


nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))