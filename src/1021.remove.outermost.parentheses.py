class Solution:
  def removeOuterParentheses(self, S: str) -> str:
    lvl, cur, ans = 0, '', ''
    for s in S:
      cur += s
      if s == '(':
        lvl += 1
      else:
        lvl -= 1
      if lvl == 0:
        ans += cur[1:-1]
        cur = ''
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "()()",
    "(()())(())",
    "(()())(())(()(()))",
  ]
  rslts = [solver.removeOuterParentheses(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
