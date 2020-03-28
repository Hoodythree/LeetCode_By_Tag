def findNumbers(nums):
    count = 0
    for n in nums:
        count += 1 if len(str(n)) % 2 == 0 else 0
    return count


print(findNumbers([12,345,2,6,7896]))