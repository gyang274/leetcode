from functools import lru_cache

class Solution:
  @lru_cache(None)
  def winnerSquareGame(self, n: int) -> bool:
    for i in range(int(n ** 0.5), 0, -1):
      if i * i == n:
        return True
      if not self.winnerSquareGame(n - i * i):
        return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.winnerSquareGame(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
