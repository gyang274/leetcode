class Solution:
  def maxA(self, N: int) -> int:
    """O(N): dynamic programming.
    """
    if N < 7:
      return N
    # dp[i][0]: num of A on screen and num of A in buffer, w.r.t max num of A on screen
    # dp[i][1]: num of A on screen and num of A in buffer, w.r.t max num of A in buffer
    dp = [[[0,0],[0,0]] for _ in range(N + 1)]
    for i in range(1, 4):
      dp[i] = [[i,0], [i,0]]
    dp[4] = [[4,0],[2,1]]
    dp[5] = [[5,0],[4,2]]
    dp[6] = [[6,3],[6,3]]
    dp[7] = [[9,3],[8,4]]
    # no more typing..
    for i in range(8, N + 1):
      # max num of A on screen
      x1 = dp[i - 1][0][0] + dp[i - 1][0][1]
      x2 = dp[i - 1][1][0] + dp[i - 1][1][1]
      x3 = dp[i - 3][0][0] * 2
      if x1 > x2 and x1 > x3:
        dp[i][0] = [x1, dp[i - 1][0][1]]
      elif x2 > x3:
        dp[i][0] = [x2, dp[i - 1][1][1]]
      else:
        dp[i][0] = [x3, dp[i - 3][0][0]]
      # max num of A in buffer
      dp[i][1] = [x3, dp[i - 3][0][0]]
    return dp[N][0][0]

class Solution:
  def maxA(self, N: int) -> int:
    """O(1): math.
      f(N) -> k^{N/(k + 1)} as N -> inf, k + 1 actions to select, copy and paste k - 1 times.
      argmax_k(k^{N/(k + 1)}) = 4 for k in 2, 3, 4, 5
      never add after 5 or after any paste/multiplying
      num of multiply by 2, 3 or 5 are bounded:
      - 4^1 cost 5 while 2^2 cost 6
      - 4^4 > 3^5, while both cost 20
      - 4^6 > 5^5, while both cost 30
      so, at most 5 addition and 9 = 1 + 4 + 4 multiplication by a num other than 4.
    """
    xmax = [0, 1, 2, 3, 4, 5, 6, 9, 12, 16, 20, 27, 36, 48, 64, 81]
    q = (N - 11) / 5 if N > 15 else 0
    # return xmax[N - 5*q] * 4**q
    return xmax[N - 5*q] << (2*q)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 9, 42, 85,
  ]
  rslts = [solver.maxA(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        