import copy
class Solution:
    def dfs(self, nums, results, templist, startIndex):
        results.append(templist)
        for i in range(startIndex, len(nums)):
            templist.append(nums[i])
            self.dfs(nums, results, copy.deepcopy(templist), i+1)
            templist.pop()

    def subsets(self, nums):
        results = []
        self.dfs(nums, results, [], 0)
        return results


def subsets2(nums):
    ans = []
    def dfs(temp, startIndex):
        ans.append(temp)
        for i in range(startIndex, len(nums)):
            temp.append(nums[i])
            dfs(temp.copy(), i+1)
            temp.pop()
    dfs([], 0)
    return ans


def subsets3(nums):
    ans = []
    def dfs(n, startIndex, curr):
        if n == len(curr):
            ans.append(curr.copy())
            return
        for i in range(startIndex, len(nums)):
            curr.append(nums[i])
            dfs(n, i+1, curr)
            curr.pop()
        
    for i in range(len(nums)+1):
        dfs(i, 0, [])
    return ans




# s = Solution()  
nums = [1, 2,3]
# print(s.subsets(nums))
print(subsets3(nums))