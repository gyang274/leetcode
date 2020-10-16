class Solution:
  def recursive(self, n, m, k):
    if not (n, m, k) in self.memo:
      if n < k or m < k:
        self.memo[(n, m, k)] = 0
      elif k == 1:
        self.memo[(n, m, k)] = 0
        for j in range(1, m + 1):
          self.memo[(n, m, k)] += j ** (n - 1)
      else:
        self.memo[(n, m, k)] = 0
        # recursive over last (k-th) update index and value.
        for i in range(k - 1, n):
          for j in range(k, m + 1):
            self.memo[(n, m, k)] += self.recursive(i, j - 1, k - 1) * (j ** (n - 1 - i))
      self.memo[(n, m, k)] %= (10 ** 9 + 7)
    return self.memo[(n, m, k)]
  def numOfArrays(self, n: int, m: int, k: int) -> int:
    self.memo = {}
    return self.recursive(n, m, k)

import itertools

class Solution:
  def numOfArrays(self, n: int, m: int, k: int) -> int:
    # dynamic programming
    # dp[u][v][w] means:
    #  1. u: length of the array is u, u = 1,..,n
    #  2. v: the cost of the algo is v, v = 1,..,k
    #  3. w: the max value in the array is w, w = 1,..,m
    dp = [[[0 for _ in range(m + 1)] for _ in range(k + 1)] for _ in range(n + 1)]
    # the array has length of 1, and 1 jump, only 1 way to do that, for any k
    for w in range(1, m + 1):
      dp[1][1][w] = 1
    for u, v, w in itertools.product(range(1, n + 1), range(1, k + 1), range(m + 1)):
      # extend without extra cost with max value w
      #  so the new value can be any value of 1,..,w
      dp[u][v][w] += dp[u - 1][v][w] * w
      # extend with an extra cost with max value w
      #  the max value from previous must be 1,..,w-1
      dp[u][v][w] += sum(dp[u - 1][v - 1][1:w])
    # valid case are max value of all 1:m with array length n and cost k
    return sum(dp[n][k][1:]) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, 3, 1),
    (5, 2, 3),
    (37, 17, 7),
    (50, 100, 25),
  ]
  rslts = [solver.numOfArrays(n, m, k) for n, m, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
