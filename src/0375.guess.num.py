from collections import deque

class Solution:
  def getMoneyAmount(self, n: int) -> int:
    """dynamic programing, O(N^3).
    """
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for L in range(n - 1, 0, -1):
      for R in range(L + 1, n + 1):
        dp[L][R] = min(
          k + max(dp[L][k - 1], dp[k + 1][R]) for k in range(L, R)
        )
    return dp[1][n]

class Solution:
  def getMoneyAmount(self, n: int) -> int:
    """dynamic programing + monotonic increase property of f(L, k), O(N^2)
    """
    # Key:
    # https://blog.csdn.net/Site1997/article/details/100168676
    # https://artofproblemsolving.com/community/c296841h1273742
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for R in range(2, n + 1):
      k, q = R - 1, deque([])
      for L in range(R - 1, 0, -1):
        # k_0 s.t. dp[L][k - 1] < dp[k + 1][R] and dp[L][(k + 1) - 1] > dp[(k + 1) + 1][R],
        # and then dp[L][R] = min(dp[L][k0] + k0 + 1, max(dp[k + 1][R] + k, k <= k0)), this k0 can be find in amortized O(1).
        while k > 0 and dp[L][k - 1] > dp[k + 1][R]:
          k -= 1
        # shrink the bounday indexed by k for (k + 1, R)
        while q and q[-1][0] > k:
          q.pop()
        # extend the boundary indexedy by k for (k + 1, R) due to extension/move of L
        v = dp[L + 1][R] + L
        while q and q[0][1] > v:
          q.popleft()
        q.appendleft((L, v))
        dp[L][R] = min(dp[L][k] + (k + 1), q[-1][1])
    return dp[1][n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
  ]
  rslts = [solver.getMoneyAmount(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")