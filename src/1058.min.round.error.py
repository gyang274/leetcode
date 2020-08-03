from typing import List

import math

class Solution:
  def minimizeError(self, prices: List[str], target: int) -> str:
    prices = list(map(float, prices))
    # xmin <= target <= xmax
    xmin, xmax = sum(map(math.floor, prices)), sum(map(math.ceil, prices))
    if not (xmin <= target <= xmax):
      return "-1"
    # cost of moving floor -> ceil
    move = sorted(map(lambda x: ((math.ceil(x) - x) - (x - math.floor(x)), x), prices))
    # cost of round to get the target
    cost = 0
    for i, (_, x) in enumerate(move):
      if i < target - xmin:
        cost += math.ceil(x) - x
      else:
        cost += x - math.floor(x)
    return f"{round(cost, 4):.3f}"

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["0.700","2.800","4.900"], 8),
    (["1.500","2.500","3.500"], 10),
    (["2.000","2.000","2.000","2.000","2.000"], 11),
  ]
  rslts = [solver.minimizeError(prices, target) for prices, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
