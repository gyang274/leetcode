class Solution:
  def numDecodings(self, s: str) -> int:
    """dynamic programming, no memo no efficiency.
    """
    if len(s) == 0 or int(s[0]) == 0:
      return 0
    elif len(s) == 1:
      return 1
    elif len(s) == 2:
      if int(s) <= 26:
        return 1 if int(s[1]) == 0 else 2
      else:
        return 0 if int(s[1]) == 0 else 1
    elif int(s[:2]) <= 26:
      return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
    else:
      return self.numDecodings(s[1:])

class Solution:
  def numDecodings(self, s: str) -> int:
    """dynamic programming with memo.
    """
    n = len(s)
    if len(s) == 0 or s[0] == '0':
      return 0
    memo = [0 for _ in range(n + 2)]
    memo[n], memo[n + 1] = 1, 0   
    for i in range(n - 1, -1, -1):
      if s[i] == '0':
        continue
      memo[i] = memo[i + 1] + memo[i + 2] if int(s[i:(i + 2)]) <= 26 else memo[i + 1]
    return memo[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "0",
    "1",
    "01",
    "10",
    "100",
    "110120",
    "112234",
  ]
  rslts = [solver.numDecodings(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")