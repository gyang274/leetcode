class Solution:
  def numTrees(self, n: int) -> int:
    """dynamic programming with memo.
     f(n) = f(n - 1) + f(n - 1) + f(i) * f(j), where i + j = n - 1, and i, j >= 1
     where each of 3 entries represent BST of (L, X), (X, R), and (L, R) respectively.
    """
    if n < 2: return 1
    memo = [0 for _ in range(n + 1)]
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1):
      memo[i] = 2 * memo[i - 1]
      for j in range(1, i - 1):
        memo[i] += memo[j] * memo[i - 1 - j]
    return memo[n]

class Solution:
  def numTrees(self, n: int) -> int:
    """dynamic programming with memo.
     f(n) = f(i) * f(j), where i + j = n - 1, and i, j >= 0
    """
    if n < 2: return 1
    memo = [0 for _ in range(n + 1)]
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1):
      for j in range(i):
        memo[i] += memo[j] * memo[i - 1 - j]
    return memo[n]

class Solution:
  def numTrees(self, n: int) -> int:
    """math deduction
    """
    C = 1
    for i in range(0, n):
      C = C * 2 * (2 * i + 1) // (i + 2)
    return C

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0,
    1,
    2,
    3,
    4,
    5,
  ]
  rslts = [solver.numTrees(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
