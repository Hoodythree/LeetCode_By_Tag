# selection sort
# O(n^2)+O(1)
def findUnsortedSubarray(nums):
    l = len(nums)
    r = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] < nums[i]:
                r = max(r, j)
                l = min(i, l)
    return r-l+1 if l<r else 0
# using sorting
# O(nlogn)+O(n)
def findUnsortedSubarray2(nums):
    nums_sorted = sorted(nums)
    start = len(nums)
    end = 0
    for i in range(len(nums)):
        if nums[i] != nums_sorted[i]:
            start = min(start, i)
            end = max(end, i)
    return end-start+1 if end > start else 0

# using stack
# O(n)+O(n)
def findUnsortedSubarray3(nums):
    stack = []
    l = len(nums)
    r = 0
    for i in range(len(nums)):
        while stack and nums[i] < nums[stack[-1]]:
            l = min(l, stack.pop())
        stack.append(i)

    stack = []
    for i,e in reversed(list(enumerate(nums))):
        while stack and nums[i] > nums[stack[-1]]:
            r = max(r, stack.pop())
        stack.append(i)
    return r-l+1 if l<r else 0
        




nums = [2,6,4,8,10,9,15]
print(findUnsortedSubarray3(nums))
    