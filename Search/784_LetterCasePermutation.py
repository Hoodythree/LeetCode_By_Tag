# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
def letterCasePermutation(s):
    ans = []
    def dfs(l, curr=[]):
        if l == len(s):
            ans.append(curr[:])
            return
        else:

            if s[l].isalpha():
                dfs(l+1, curr)
                curr.append(s[l].lower() if s[l].islower() else s[l].upper())
                dfs(l+1, curr)
            else:
                dfs(l+1, curr)
    dfs(0)
    return ans

s = '3z5'
print(letterCasePermutation(s))
    