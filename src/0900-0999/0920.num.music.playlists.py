from math import comb

class Solution:
  def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
    M = 10 ** 9 + 7
    if K == 0 or N == L:
      return sum(((-1) ** (i & 1)) * comb(N, i) * ((N - i) ** L) for i in range(N)) % M
    # dynamic programming: O(NL)
    # dp[i][j]: num of playlist of length i with exactly j musics
    # dp[i][1] = 1, dp[i][j] = dp[i - 1][j - 1] * (N - (j - 1)) + dp[i - 1][j] * max(j - K, 0)
    # NOTE: it can be shown that the above dp can be derived within O(NlogL) using generating functions
    dp = [[0] * (N + 1) for _ in range(L + 1)]
    dp[0][0] = 1
    for i in range(1, L + 1):
      for j in range(1, N + 1):
        dp[i][j] = (dp[i - 1][j - 1] * (N - (j - 1)) + dp[i - 1][j] * max(j - K, 0)) % M
    return dp[L][N]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3, 0),
    (5, 8, 0),
    (23, 42, 0),
    (2, 3, 1),
    (5, 8, 3),
    (23, 42, 14),
  ]
  rslts = [solver.numMusicPlaylists(N, L, K) for N, L, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")