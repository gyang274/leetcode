class Solution:
  def distinctSubseqII(self, S: str) -> int:
    # dynamic programming, O(N)
    # dp[0] = {""}
    # dp[1] = {"", "s"}, s = S[0]
    # dp[i + 1] = dp[i] * 2 - dp[(k + 1) - 1], k = argmax_j(S[j] == S[i], j < i)
    n = len(S)
    dp, seen = [0] * (n + 1), {}
    dp[0] = 1
    for i, x in enumerate(S):
      dp[i + 1] = dp[i] * 2
      if x in seen:
         dp[i + 1] -= dp[seen[x]]
      seen[x] = i
    return (dp[n] - 1) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aaa",
    "aab",
    "aba",
    "abb",
    "abc",
  ]
  rslts = [solver.distinctSubseqII(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
