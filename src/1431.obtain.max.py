from typing import List

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    m = max(candies)
    return list(map(lambda x: x + extraCandies >= m, candies))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,5,1,4], 3),
  ]
  rslts = [solver.kidsWithCandies(candies, extraCandies) for candies, extraCandies in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
