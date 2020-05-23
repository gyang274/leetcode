from typing import List

class Solution:
  def maxProfit(self, prices: List[int], fee: int) -> int:
    # status machine
    hold, sold = -2147483648, 0
    for price in prices:
      hold = max(hold, sold - price)
      sold = max(sold, hold + price - fee)
    return max(hold, sold)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,3,2,8,4,9], 2),
  ]
  rslts = [solver.maxProfit(prices, fee) for prices, fee in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
