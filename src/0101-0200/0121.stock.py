from typing import List

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """maintain a minimum prices ever seen, and max profit ever seen.
    """
    xmin, vmax = 2147483647, 0
    for x in prices:
      xmin = min(x, xmin)
      vmax = max(vmax, x - xmin)
    return vmax

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """status machine: s1 buy or hold, s2 sell previous brought or hold, one transaction.
    """
    s1, s2 = -2147483648, 0
    for x in prices:
      # buy or hold, money in pocket
      s1 = max(s1, -x)
      # hold or sell, money in pocket
      s2 = max(s2, s1 + x)
    return s2

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [7,6,4,3,1],
    [7,1,5,3,6,4],
  ]
  rslts = [solver.maxProfit(prices) for prices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  