from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """accumulate profit, hold to profit when keep up, hold to buy in when keep down.
    """
    v = 0
    for i in range(1, len(prices)):
      v += max(0, prices[i] - prices[i - 1])
    return v

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,4,5],
    [7,6,4,3,1],
    [7,1,5,3,6,4],
  ]
  rslts = [solver.maxProfit(prices) for prices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")