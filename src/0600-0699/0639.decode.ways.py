class Solution:
  def numDecodings(self, s: str) -> int:
    """Q0091
    """
    n = len(s)
    if n == 0 or s[0] == 0:
      return 0
    dp = [0] * (n + 1)
    dp[n] = 1
    for i in range(n - 1, -1, -1):
      if s[i] == "0":
        continue
      elif s[i] == "*":
        dp[i] = 9 * dp[i + 1]
        if i + 1 < n:
          if s[i + 1] == "*":
            dp[i] += 15 * dp[i + 2]
          else:
            dp[i] += 2 * dp[i + 2] if int(s[i + 1]) <= 6 else dp[i + 2]
      else:
        dp[i] = dp[i + 1]
        if i + 1 < n:
          if s[i + 1] == "*":
            if s[i] == "1":
              dp[i] += 9 * dp[i + 2]
            elif s[i] == "2":
              dp[i] += 6 * dp[i + 2]
          elif int(s[i:(i + 2)]) <= 26:
            dp[i] += dp[i + 2]
      dp[i] %= (10 ** 9 + 7)
    return dp[0]

class Solution:
  def numDecodings(self, s: str) -> int:
    """Q0091
    """
    n = len(s)
    if n == 0 or s[0] == 0:
      return 0
    dp = [0] * (n + 2)
    dp[n], dp[n + 1] = 1, 0
    s += "9"
    for i in range(n - 1, -1, -1):
      if s[i] == "0":
        continue
      elif s[i] == "*":
        dp[i] = 9 * dp[i + 1]
        if s[i + 1] == "*":
          dp[i] += 15 * dp[i + 2]
        else:
          dp[i] += 2 * dp[i + 2] if int(s[i + 1]) <= 6 else dp[i + 2]
      else:
        dp[i] = dp[i + 1]
        if s[i + 1] == "*":
          if s[i] == "1":
            dp[i] += 9 * dp[i + 2]
          elif s[i] == "2":
            dp[i] += 6 * dp[i + 2]
        elif int(s[i:(i + 2)]) <= 26:
          dp[i] += dp[i + 2]
      dp[i] %= (10 ** 9 + 7)
    return dp[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "0",
    "1",
    "*",
    "**",
    "01",
    "10",
    "1*",
    "100",
    "10*",
    "1*0",
    "****",
    "11*223*4",
    "*********",
    "11*0*12*0*",
    "**********",
  ]
  rslts = [solver.numDecodings(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")