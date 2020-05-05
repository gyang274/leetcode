class Solution:
  def minWindow(self, S: str, T: str) -> str:
    """dynamic programming
    """
    n, m = len(S), len(T)
    # dp[j] = s at i-th iteration: s = argmin_t S[t:j] has T[:(i + 1)] as subsequence.
    dp = [i if x == T[0] else None for i, x in enumerate(S)]
    for i in range(1, m):
      seen = dp[0]
      dp[0] = None
      for j in range(1, n):
        # prev: seen T[j-1]
        prev = dp[j]
        dp[j] = seen if S[j] == T[i] else None
        if prev is not None:
          seen = prev
    dp = sorted([(e - s, s, e) for e, s in enumerate(dp) if s is not None])
    return S[dp[0][1]:(dp[0][2] + 1)] if dp else ""

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcdebdde", "bde"),
    ("fgrqsqsnodwmxzkzxwqegkndaa", "fnok"),
  ]
  rslts = [solver.minWindow(S, T) for S, T in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")