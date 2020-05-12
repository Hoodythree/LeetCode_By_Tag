# 1 1 1 1
# 1 2 2 2
# 1 2 3 3
# 1 2 3 4

n = 5
nums = []
for i in range(n):
    temp = [0] * n
    for j in range(i + 1):
        temp[j] = j + 1
    nums.append(temp)

for i in range(len(nums)):
    for j in range(len(nums[i])):
        nums[i][j] = nums[j][i]
print(nums)
