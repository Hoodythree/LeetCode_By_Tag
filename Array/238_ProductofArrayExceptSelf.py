# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

def productExceptSelf(nums):
    res = 1
    temp = 1
    output = []
    for i in nums:
        res *= i
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i):
                temp *= nums[j]
            for k in range(i+1, len(nums)):
                temp *= nums[k]
            output.append(temp)
        else:
            output.append(res // nums[i]) 
    return output

def productExceptSelf2(nums):
    top_i = [1,]

    for i in range(1, len(nums)):
        top_i.append(nums[i-1]*top_i[i-1])
    
    nums = list(reversed(nums))
    top_i_resverse = [1, ]
    for i in range(1, len(nums)):
        top_i_resverse.append(nums[i-1]*top_i_resverse[i-1])
    
    top_i_resverse = list(reversed(top_i_resverse))
    for i in range(len(nums)):
        nums[i] = top_i[i] * top_i_resverse[i]
    return nums

def productExceptSelf3(nums):
    top_i = []
    temp = 1
    iter = len(nums)
    for i in range(iter):
        top_i.append(temp)
        # prepared for next
        temp *= nums[i]
    temp = 1
    while iter > 0:
        top_i[iter-1] *= temp
        temp *= nums[iter-1]
        iter-=1
    return top_i






nums = [1, 2, 3, 4]
print(productExceptSelf3(nums))