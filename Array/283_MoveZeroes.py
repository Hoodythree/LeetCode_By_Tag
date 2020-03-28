# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]


def findZeros(nums):
    counter = 0
    for i in nums:
        if i == 0:
            counter += 1
    return counter


def moveZeroes(nums):
    n_iter = findZeros(nums)
    index = 0
    for i in range(n_iter):
        for j in range(index,len(nums)):
            if nums[j] == 0:
                for k in range(j+1, len(nums)):
                    if nums[k] != 0:
                        nums[k], nums[j] = nums[j], nums[k]
                        index = k
                        break
    return nums

    
nums = [0,1,0,3,12]
print(moveZeroes(nums))
print('hello')

