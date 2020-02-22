from typing import List

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    """Binary xor `^` operator, x ^ x = 0, so (~(x ^ x)) & x = x.
    """
    seen_once = seen_twice = 0
    for x in nums:
      seen_once = ~seen_twice & (seen_once ^ x)
      seen_twice = ~seen_once & (seen_twice ^ x)
    return seen_once

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [0],
    [2,1,2,2],
    [1,2,1,4,2,1,2]
  ]
  rslts = [solver.singleNumber(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  