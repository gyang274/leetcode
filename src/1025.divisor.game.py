from functools import lru_cache

class Solution:
  @lru_cache(None)
  def divisorGame(self, N: int) -> bool:
    if N == 1:
      return False
    for x in range(1, int(N ** 0.5) + 1):
      if N % x == 0:
        if not self.divisorGame(N - x):
          return True
        if x > 1:
          y = N // x
          if not self.divisorGame(N - y):
            return True
    return False

class Solution:
  def divisorGame(self, N: int) -> bool:
    return N & 1 == 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.divisorGame(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
