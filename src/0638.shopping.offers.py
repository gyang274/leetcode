from typing import List

class Solution:
  def recursive(self, pay, needs):
    key = tuple(needs)
    if key not in self.memo:
      self.memo[key] = pay + sum([n * p for n, p in zip(needs, self.price)])
      for offer in self.special:
        rests = [n - o for n, o in zip(needs, offer)]
        if all([r >= 0 for r in rests]):
          self.memo[key] = min(self.memo[key], self.recursive(pay + offer[-1], rests))
    return self.memo[key]
  def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
    self.memo, self.price, self.special = {}, price, special
    return self.recursive(0, needs)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,5], [[3,0,5],[1,2,10]], [3,2]),
    ([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]),
  ]
  rslts = [solver.shoppingOffers(price, special, needs) for price, special, needs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
