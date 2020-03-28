# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

def letterCombinations(digits):
    if not digits or digits == ' ':
        return []
    d = [' ','', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ans = []
    def dfs(d, l, curr):
        if l == len(digits):
            ans.append(''.join(curr.copy()))
            return
        else:
            for c in d[int(digits[l])]:
                curr.append(c)
                dfs(d, l+1, curr)
                curr.pop()
    dfs(d, 0, [])
    return ans

print(letterCombinations(' '))