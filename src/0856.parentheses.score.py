class Solution:
  def scoreOfParentheses(self, S: str) -> int:
    stack = []
    for x in S:
      if x == '(':
        stack.append(x)
      else:
        if stack[-1] == '(':
          stack.pop()
          if stack and not stack[-1] == '(':
            stack[-1] += 1
          else:
            stack.append(1)
        else:
          v, _ = stack.pop(), stack.pop()
          if stack and not stack[-1] == '(':
            stack[-1] += v * 2
          else:
            stack.append(v * 2)
    return stack[0]

class Solution:
  def scoreOfParentheses(self, S: str) -> int:
    ans = bal = 0
    for i, x in enumerate(S):
      if x == '(':
        bal += 1
      else:
        bal -= 1
        if S[i - 1] == '(':
          ans += 1 << bal
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "()",
    "()()",
    "(())",
    "()(())",
    "(()(()))"
  ]
  rslts = [solver.scoreOfParentheses(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
