class Solution:
  def longestValidParentheses(self, s: str) -> int:
    """Dynamic Programming.
    """
    n = len(s)
    memo = [0 for _ in range(n + 1)]
    for i in range(n - 2, -1, -1):
      if s[i] == '(':
        if s[i + 1] == ')':
          memo[i] = 2 + memo[i + 2]
        else:
          k = memo[i + 1]
          if k > 0 and i + k + 1 < n and s[i + k + 1] == ')':
            memo[i] = 2 + k + memo[i + k + 2]
      # print(f"{i=}, {memo=}")
    return max(memo)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "(",
    "()",
    ")",
    ")(",
    "(()",
    ")()())",
    "((()))())",
  ]
  rslts = [solver.longestValidParentheses(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")