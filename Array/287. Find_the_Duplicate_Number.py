def findDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        else:
            seen.add(n)
    return -1


def findDuplicate2(nums):
    nums = sorted(nums)
    l = 0
    r = len(nums)
    while l < r:
        m = (r + l) // 2
        count = 0
        for n in nums:
            if n <= m:
                count += 1
        if count > m:
            r = m
        else:
            l = m+1
    return l

            




nums = [3, 3, 2, 1, 1]
print(findDuplicate2(nums))