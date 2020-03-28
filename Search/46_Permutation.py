# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

def permute(nums):
    ans = []
    prelist = []
    used = [0 for _ in range(len(nums))]
    def dfs(d=0):
        if d == len(nums):
            ans.append(prelist.copy())
            return
        else:
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i-1] == nums[i] and used[i-1]:
                    continue
                used[i] = 1
                prelist.append(nums[i])
                dfs(d+1)
                prelist.pop()
                used[i] = 0
    dfs()
    return ans

nums = [1, 1,1, 2]
print(permute(nums))