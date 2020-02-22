from typing import List

class Solution:
  def maxProfit(self, k: int, prices: List[int]) -> int:
    """status machine, ref. 0121, 0122, 0123.
    """
    if k > len(prices) // 2:
      # kind like as many as transactions needed, simply accumulate profit, ref. 0122.
      profit = 0
      for i in range(1, len(prices)):
        profit += max(0, prices[i] - prices[i - 1])
      return profit
    # number of status, constraint by k transactions
    n = 2 * k + 1
    # status stack: 
    # 0 transaction, then each buy-sell transaction are split across time to status: buy and hold, sell and hold, ..
    status = [-2147483648 for _ in range(n)]
    # this is kind like the init status w.o. any transaction
    for i in range(0, n, 2):
      status[i] = 0
    for x in prices:
      for i in range(1, n):
        # buy and hold of (i - 1) / 2 -th transaction
        if i % 2 == 1:
          status[i] = max(status[i], status[i - 1] - x)
        # sell and hold of i / 2 -th transaction
        else:
          status[i] = max(status[i], status[i - 1] + x)
    return status[k * 2]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, []),
    (3, [1,2,3,4,5]),
    (3, [7,6,4,3,1]),
    (2, [3,2,6,5,0,3]),
    (2, [7,1,5,3,6,4]),
    (3, [3,3,5,0,0,3,1,4]),
  ]
  rslts = [solver.maxProfit(k, prices) for k, prices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 