from typing import List

class Solution:
  def recursive(self, i: int, j: int) -> int:
    # piles[i:(j + 1)] return 1st player - 2nd player, both play optimally
    if (i, j) not in self.memo:
      if i + 1 == j:
        self.memo[(i, j)] = abs(self.piles[i] - self.piles[j])
      else:
        self.memo[(i, j)] = max(
          self.piles[i] - self.recursive(i + 1, j), self.piles[j] - self.recursive(i, j - 1)
        )
    return self.memo[(i, j)]
  def stoneGame(self, piles: List[int]) -> bool:
    self.memo, self.piles = {}, piles
    return self.recursive(0, len(piles) - 1) > 0

class Solution:
  def stoneGame(self, piles: List[int]) -> bool:
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [5,3,4,5],
  ]
  rslts = [solver.stoneGame(piles) for piles in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
