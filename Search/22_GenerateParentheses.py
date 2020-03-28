# n =3
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

def valid(str):
    if not str:
        return True
    if str[0] == ')':
        return False
    stack = [str[0]]
    for s in str[1:]:
        if s == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s)
    return stack == []

def generateParenthesis(n):
    ans = []
    res = []
    parenthesis = ['(', ')']
    def generateAll(l, curr, parenthesis):
        if l == 2*n:
            ans.append(''.join(curr.copy()))
        else:
            for p in parenthesis:
                curr.append(p)
                generateAll(l+1, curr, parenthesis)
                curr.pop()
    generateAll(0, [], parenthesis)
    for s in ans:
        if valid(s):
            res.append(s)
    return res
    

def dfs(left, right, curr, ans):
    if right == 0 and left == 0:
        ans.append(curr)
        return
    if right < left:
        return
    if left > 0:
        dfs(left-1, right, curr+'(', ans)
    if right > 0:
        dfs(left, right-1, curr+')', ans)
    return ans

def generateParenthesis2(n):
    if n == 0:
        return []
    return dfs(n, n, '', [])

print(generateParenthesis2(3))




# n = 3
# print(generateParenthesis(3))
# print(valid('()(()('))