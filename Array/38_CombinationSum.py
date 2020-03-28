# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]

def combinationSum(candidates, target):
    ans = []
    candidates = sorted(candidates)
    def toFindCombinationSumToTarget(target, curr_combination, startIndex):
        if target == 0:
            ans.append(curr_combination.copy())
            return
        else:
            for i in range(startIndex, len(candidates)):
                if target < candidates[i]:
                    break
                else:
                    curr_combination.append(candidates[i])
                    toFindCombinationSumToTarget(target-candidates[i], curr_combination, i)
                    curr_combination.pop()

    toFindCombinationSumToTarget(target, [], 0)
    return ans

candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))