from typing import List

class Solution:
  def maxCoins(self, piles: List[int]) -> int:
    piles.sort(reverse=True)
    return sum(piles[i] for i in range(1, len(piles) - len(piles) // 3, 2))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,4,1,2,7,8],
    [9,8,7,6,5,4,2],
    [9,8,7,6,5,4,2,3],
    [9,8,7,6,5,4,2,3,1],
  ]
  rslts = [solver.maxCoins(piles) for piles in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
