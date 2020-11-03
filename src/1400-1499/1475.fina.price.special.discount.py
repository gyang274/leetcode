from typing import List

class Solution:
  def finalPrices(self, prices: List[int]) -> List[int]:
    # stack, TC: O(N), SC: O(N), refr Q0503.
    stack = []
    for i, x in enumerate(prices):
      while stack and prices[stack[-1]] >= x:
        prices[stack.pop()] -= x
      stack.append(i)
    return prices

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [1,2,3,4,5],
    [8,4,6,2,3],
  ]
  rslts = [solver.finalPrices(prices) for prices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
